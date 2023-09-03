from .....Client import (
    AsyncAPI,
    ClientResponse,
    IHttpActionResult,
)
from .....Constants import (
    Unset,
)
from ...ViewModels import (
    ContractorDeliveryAddress,
)

from datetime import (
    datetime,
)
from pydantic import (
    BaseModel,
)
from typing import (
    Type,
    TypeVar,
    Optional,
    Tuple,
    List,
    Union,
    overload,
)


async def AddNew(
    api: AsyncAPI,
    contractorCode: str = Unset(),
    contractorDeliveryAddress: ContractorDeliveryAddress = Unset(),
    contractorId: int = Unset()
) -> IHttpActionResult[List[ContractorDeliveryAddress]]:
    match contractorCode, contractorDeliveryAddress, contractorId:
        case str(), ContractorDeliveryAddress(), Unset():
            path = "/api/ContractorDeliveryAddresses/Create"
            params = dict()
            params["contractorCode"] = contractorCode
            data = contractorDeliveryAddress.model_dump_json(exclude_unset=True)
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="POST", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[ContractorDeliveryAddress])
            return result
        case Unset(), ContractorDeliveryAddress(), int():
            path = "/api/ContractorDeliveryAddresses/Create"
            params = dict()
            data = contractorDeliveryAddress.model_dump_json(exclude_unset=True)
            params["contractorId"] = contractorId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="POST", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[ContractorDeliveryAddress])
            return result


async def Get(
    api: AsyncAPI,
    contractorCode: str = Unset(),
    contractorId: int = Unset()
) -> IHttpActionResult[List[ContractorDeliveryAddress]]:
    match contractorCode, contractorId:
        case Unset(), int():
            path = "/api/ContractorDeliveryAddresses"
            params = dict()
            data = None
            params["contractorId"] = contractorId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[ContractorDeliveryAddress])
            return result
        case str(), Unset():
            path = "/api/ContractorDeliveryAddresses"
            params = dict()
            data = None
            params["contractorCode"] = contractorCode
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[ContractorDeliveryAddress])
            return result


async def Update(
    api: AsyncAPI,
    contractorCode: str = Unset(),
    contractorDeliveryAddress: ContractorDeliveryAddress = Unset(),
    contractorId: int = Unset()
) -> IHttpActionResult[None]:
    match contractorCode, contractorDeliveryAddress, contractorId:
        case str(), ContractorDeliveryAddress(), Unset():
            path = "/api/ContractorDeliveryAddresses/Update"
            params = dict()
            params["contractorCode"] = contractorCode
            data = contractorDeliveryAddress.model_dump_json(exclude_unset=True)
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result
        case Unset(), ContractorDeliveryAddress(), int():
            path = "/api/ContractorDeliveryAddresses/Update"
            params = dict()
            data = contractorDeliveryAddress.model_dump_json(exclude_unset=True)
            params["contractorId"] = contractorId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result
