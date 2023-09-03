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
    DimensionClassification,
    PositionDimension,
)
from ....Common.ViewModels.Aspects import (
    AspectDocument,
    AspectPositionEdit,
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


async def GetAspects(
    api: AsyncAPI,
    buffer: bool = Unset(),
    orderId: int = Unset(),
    orderNumber: str = Unset()
) -> IHttpActionResult[AspectDocument]:
    match buffer, orderId, orderNumber:
        case bool(), Unset(), str():
            path = "/api/OwnOrderDimensions/Aspects"
            params = dict()
            data = None
            params["buffer"] = buffer
            params["orderNumber"] = orderNumber
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, AspectDocument)
            return result
        case Unset(), int(), Unset():
            path = "/api/OwnOrderDimensions/Aspects"
            params = dict()
            data = None
            params["orderId"] = orderId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, AspectDocument)
            return result


async def GetClassification(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DimensionClassification]]:
    """
    ['List[DimensionClassification]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DimensionClassification]
    :rtype: List[DimensionClassification]
    """
    path = "/api/OrderDimensions/Classification"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DimensionClassification])
    return result


async def GetPositionClassification(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DimensionClassification]]:
    """
    ['List[DimensionClassification]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DimensionClassification]
    :rtype: List[DimensionClassification]
    """
    path = "/api/OrderDimensions/PositionClassification"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DimensionClassification])
    return result


async def Update(
    api: AsyncAPI,
    buffer: bool = Unset(),
    orderDimension: Dimension = Unset(),
    orderDimensions: List[Dimension] = Unset(),
    orderId: int = Unset(),
    orderNumber: str = Unset()
) -> IHttpActionResult[None]:
    match buffer, orderDimension, orderDimensions, orderId, orderNumber:
        case Unset(), Unset(), list(_), int(), Unset() if all(isinstance(item, Dimension) for item in orderDimensions):
            path = "/api/OrderDimensions/UpdateList"
            params = dict()
            data = f"[{','.join([elem.model_dump_json(exclude_unset=True) for elem in orderDimensions])}]"
            params["orderId"] = orderId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result
        case bool(), Unset(), list(_), Unset(), str() if all(isinstance(item, Dimension) for item in orderDimensions):
            path = "/api/OrderDimensions/UpdateList"
            params = dict()
            params["buffer"] = buffer
            data = f"[{','.join([elem.model_dump_json(exclude_unset=True) for elem in orderDimensions])}]"
            params["orderNumber"] = orderNumber
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result
        case bool(), Dimension(), Unset(), Unset(), str():
            path = "/api/OrderDimensions/Update"
            params = dict()
            params["buffer"] = buffer
            data = orderDimension.model_dump_json(exclude_unset=True)
            params["orderNumber"] = orderNumber
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result
        case Unset(), Dimension(), Unset(), int(), Unset():
            path = "/api/OrderDimensions/Update"
            params = dict()
            data = orderDimension.model_dump_json(exclude_unset=True)
            params["orderId"] = orderId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result


async def UpdateAspect(
    api: AsyncAPI, aspectPosition: AspectPositionEdit
) -> IHttpActionResult[None]:
    """
    []
    :param api:
    :type api: AsyncAPI
    :param aspectPosition:
    :type aspectPosition: AspectPositionEdit
    :returns: 
    :rtype: 
    """
    path = "/api/OwnOrderDimensions/Aspects"
    params = dict()
    data = aspectPosition.model_dump_json(exclude_unset=True)
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
    # no return
    result = await IHttpActionResult.create(response, None)
    return result


async def UpdatePosition(
    api: AsyncAPI,
    positionDimension: Union[Dimension, List[PositionDimension]] = Unset(),
    positionDimensions: List[Dimension] = Unset(),
    positionId: int = Unset()
) -> IHttpActionResult[None]:
    match positionDimension, positionDimensions, positionId:
        case list(_), Unset(), Unset() if all(isinstance(item, PositionDimension) for item in positionDimension):
            path = "/api/OrderDimensions/UpdateMultiPositionsList"
            params = dict()
            data = f"[{','.join([elem.model_dump_json(exclude_unset=True) for elem in positionDimension])}]"
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result
        case Dimension(), Unset(), int():
            path = "/api/OrderDimensions/UpdatePosition"
            params = dict()
            data = positionDimension.model_dump_json(exclude_unset=True)
            params["positionId"] = positionId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result
        case Unset(), list(_), int() if all(isinstance(item, Dimension) for item in positionDimensions):
            path = "/api/OrderDimensions/UpdatePositionList"
            params = dict()
            data = f"[{','.join([elem.model_dump_json(exclude_unset=True) for elem in positionDimensions])}]"
            params["positionId"] = positionId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result
