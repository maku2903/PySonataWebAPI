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
    api: AsyncAPI, deliveryId: int
) -> IHttpActionResult[List[Dimension]]:
    """
    ['List[Dimension]']
    :param api:
    :type api: AsyncAPI
    :param deliveryId:
    :type deliveryId: int
    :returns: List[Dimension]
    :rtype: List[Dimension]
    """
    path = "/api/DeliveryDimensions"
    params = dict()
    data = None
    params["deliveryId"] = deliveryId

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[Dimension])
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
    path = "/api/DeliveryDimensions/Classification"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DimensionClassification])
    return result


async def Update(
    api: AsyncAPI,
    deliveryDimension: Dimension = Unset(),
    deliveryDimensions: List[Dimension] = Unset(),
    deliveryId: int = Unset()
) -> IHttpActionResult[None]:
    match deliveryDimension, deliveryDimensions, deliveryId:
        case Dimension(), Unset(), int():
            path = "/api/DeliveryDimensions/Update"
            params = dict()
            data = deliveryDimension.model_dump_json(exclude_unset=True)
            params["deliveryId"] = deliveryId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result
        case Unset(), list(_), int() if all(isinstance(item, Dimension) for item in deliveryDimensions):
            path = "/api/DeliveryDimensions/UpdateList"
            params = dict()
            data = f"[{','.join([elem.model_dump_json(exclude_unset=True) for elem in deliveryDimensions])}]"
            params["deliveryId"] = deliveryId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result
