from ....Client import (
    AsyncAPI,
    ClientResponse,
    IHttpActionResult,
)
from ....Constants import (
    Unset,
)
from ...ViewModels import (
    SessionInformation,
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


async def CloseSession(
    api: AsyncAPI, 
) -> IHttpActionResult[None]:
    """
    []
    :param api:
    :type api: AsyncAPI
    :returns: 
    :rtype: 
    """
    path = "/api/Sessions/CloseSession"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    # no return
    result = await IHttpActionResult.create(response, None)
    return result


async def OpenNewSession(
    api: AsyncAPI, deviceName: str
) -> IHttpActionResult[None]:
    """
    []
    :param api:
    :type api: AsyncAPI
    :param deviceName:
    :type deviceName: str
    :returns: 
    :rtype: 
    """
    path = "/api/Sessions/OpenNewSession"
    params = dict()
    data = None
    params["deviceName"] = deviceName

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    # no return
    result = await IHttpActionResult.create(response, None)
    return result


async def SessionInformation(
    api: AsyncAPI, 
) -> IHttpActionResult[SessionInformation]:
    """
    ['SessionInformation']
    :param api:
    :type api: AsyncAPI
    :returns: SessionInformation
    :rtype: SessionInformation
    """
    path = "/api/Sessions/SessionInformation"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, SessionInformation)
    return result
