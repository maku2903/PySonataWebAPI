from .....Client import (
    AsyncAPI,
    ClientResponse,
    IHttpActionResult,
)
from .....Constants import (
    Unset,
)
from ....Common.ViewModels import (
    Dimension,
    PositionDimension,
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


async def Get(
    api: AsyncAPI,
    buffer: bool = Unset(),
    orderId: int = Unset(),
    orderNumber: str = Unset()
) -> IHttpActionResult[List[Dimension]]:
    match buffer, orderId, orderNumber:
        case bool(), Unset(), str():
            path = "/api/v2/OwnOrderDimensions"
            params = dict()
            data = None
            params["buffer"] = buffer
            params["orderNumber"] = orderNumber
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[Dimension])
            return result
        case Unset(), int(), Unset():
            path = "/api/v2/OwnOrderDimensions"
            params = dict()
            data = None
            params["orderId"] = orderId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[Dimension])
            return result


async def GetPosition(
    api: AsyncAPI, positionId: int
) -> IHttpActionResult[List[Dimension]]:
    """
    ['List[Dimension]']
    :param api:
    :type api: AsyncAPI
    :param positionId:
    :type positionId: int
    :returns: List[Dimension]
    :rtype: List[Dimension]
    """
    path = "/api/v2/OwnOrderDimensions/Positions"
    params = dict()
    data = None
    params["positionId"] = positionId

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[Dimension])
    return result


async def GetPositionsByOrderId(
    api: AsyncAPI, orderId: int
) -> IHttpActionResult[List[PositionDimension]]:
    """
    ['List[PositionDimension]']
    :param api:
    :type api: AsyncAPI
    :param orderId:
    :type orderId: int
    :returns: List[PositionDimension]
    :rtype: List[PositionDimension]
    """
    path = "/api/v2/OwnOrderDimensions/Positions"
    params = dict()
    data = None
    params["orderId"] = orderId

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[PositionDimension])
    return result


async def GetPositionsByOrderNumber(
    api: AsyncAPI, buffer: bool, orderNumber: str
) -> IHttpActionResult[List[PositionDimension]]:
    """
    ['List[PositionDimension]']
    :param api:
    :type api: AsyncAPI
    :param buffer:
    :type buffer: bool
    :param orderNumber:
    :type orderNumber: str
    :returns: List[PositionDimension]
    :rtype: List[PositionDimension]
    """
    path = "/api/v2/OwnOrderDimensions/Positions"
    params = dict()
    data = None
    params["buffer"] = buffer

    params["orderNumber"] = orderNumber

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[PositionDimension])
    return result
