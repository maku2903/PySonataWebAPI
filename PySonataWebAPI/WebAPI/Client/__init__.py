import logging
import re
import aiohttp
import typing
import asyncio
from pydantic import TypeAdapter
from aiohttp import ClientResponse
from pydantic.types import SecretStr
from typing import Union, List, Type, Generic, TypeVar
from .. import Interface

T = TypeVar("T")


class IHttpActionResult(Generic[T]):
    def __init__(self, response: ClientResponse, model: T):
        self.response = response
        self.model = model

    @classmethod
    async def create(cls, response: ClientResponse, model_type: Type[T]) -> 'IHttpActionResult[T]':
        if model_type is None:
            return cls(response, None)

        raw_data = await response.text()
        # Check if the model_type is meant to be a list of Pydantic models
        if hasattr(model_type, "__origin__") and issubclass(model_type.__origin__, list):
            inner_model = model_type.__args__[0]
            parsed_model = TypeAdapter(List[inner_model]).validate_json(raw_data)
        else:
            parsed_model = model_type.model_validate_json(raw_data)

        return cls(response, parsed_model)

    def get_model(self) -> T:
        return self.model

    def get_response(self) -> ClientResponse:
        return self.response


class AsyncAPI:
    def __init__(
        self
        , domain: str
        , https: bool
        , device_name: str
        , key: str
    ):
        self._domain = domain
        self._protocol = 'http' if not https else 'https'
        self._key: SecretStr = SecretStr(key)
        self._device_name: SecretStr = SecretStr(device_name)
        self._session: typing.Optional[Union[aiohttp.ClientSession]] = None
        self._lock: typing.Optional[typing.Union[asyncio.Lock]] = asyncio.Lock()
        self.session_is_open: bool = False

    @property
    def domain(self):
        return self._domain

    @property
    def protocol(self):
        return self._protocol

    @property
    def key(self):
        return self._key

    @property
    def device_name(self):
        return self._device_name

    async def connect(self):
        # todo check if not already connected
        # todo
        self._session = aiohttp.ClientSession()
        GUID_pattern = r'[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'
        if not bool(re.fullmatch(GUID_pattern, self.key.get_secret_value())):
            msg = 'Passed API key is not in GUID match pattern.'
            logging.error(msg=msg)
            raise AssertionError(msg)
        self._session.headers.add(key='Authorization', value=f'Application {self.key.get_secret_value()}')
        new_session = await Interface.Interfaces.ISessionController.OpenNewSession(api=self, deviceName=self.device_name.get_secret_value())
        response = new_session.get_response()
        assert response.ok, response.status
        session_token = await response.text()
        session_token = session_token.strip('"')
        if not bool(re.fullmatch(GUID_pattern, session_token)):
            msg = 'Received API token is not in GUID match pattern.'
            logging.error(msg=msg)
            raise AssertionError(msg)
        self._session.headers.clear()
        self._session.headers.add(key='Authorization', value=f'Session {session_token}')
        self.session_is_open = True

    async def disconnect(self):
        if not self.session_is_open:
            logging.warning(msg='There was an attempt to close session that is already closed.')
        else:
            response = await Interface.Interfaces.ISessionController.CloseSession(api=self)
            if not response.get_response().ok:
                logging.warning(msg='WebAPI session could not be closed gracefully.')
            else:
                logging.debug(msg='WebAPI session closed gracefully.')
            await self._session.close()
            self._session = None
        return True

    # def __del__(self):
    #     if self.session_is_open:
    #         logging.warning(msg='There was an attempt to delete client object without closing open session.')
    #         loop = asyncio.get_running_loop()
    #         loop.create_task(self.disconnect())
    #         self.session_is_open = False
    #     self.__del__()

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # todo wait for all before close
        await self.disconnect()

    async def request(
        self
        , method: str
        , path: str
        , data: Union[str, None] = None
        , params: Union[dict, None] = None
        , headers: Union[dict, None] = None
    ) -> ClientResponse:
        async with self._lock:
            full_url = f"{self._protocol}://{self._domain}{path}"
            logging.debug(msg=f'Path: {path}; Headers: {headers}; Params: {params}; Data: {data}')
            response = await self._session.request(method, full_url, data=data, params=params, headers=headers)
            return response