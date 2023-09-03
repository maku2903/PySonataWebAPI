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
    documentId: int = Unset(),
    documentNumber: str = Unset()
) -> IHttpActionResult[AspectDocument]:
    match buffer, documentId, documentNumber:
        case bool(), Unset(), str():
            path = "/api/PurchasesDimensions/Aspects"
            params = dict()
            data = None
            params["buffer"] = buffer
            params["documentNumber"] = documentNumber
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, AspectDocument)
            return result
        case Unset(), int(), Unset():
            path = "/api/PurchasesDimensions/Aspects"
            params = dict()
            data = None
            params["documentId"] = documentId
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
    path = "/api/PurchasesDimensions/Classification"
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
    path = "/api/PurchasesDimensions/PositionClassification"
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
    documentDimension: Dimension = Unset(),
    documentDimensions: List[Dimension] = Unset(),
    documentId: int = Unset(),
    documentNumber: str = Unset()
) -> IHttpActionResult[None]:
    match buffer, documentDimension, documentDimensions, documentId, documentNumber:
        case bool(), Unset(), list(_), Unset(), str() if all(isinstance(item, Dimension) for item in documentDimensions):
            path = "/api/PurchasesDimensions/UpdateList"
            params = dict()
            params["buffer"] = buffer
            data = f"[{','.join([elem.model_dump_json(exclude_unset=True) for elem in documentDimensions])}]"
            params["documentNumber"] = documentNumber
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result
        case Unset(), Unset(), list(_), int(), Unset() if all(isinstance(item, Dimension) for item in documentDimensions):
            path = "/api/PurchasesDimensions/UpdateList"
            params = dict()
            data = f"[{','.join([elem.model_dump_json(exclude_unset=True) for elem in documentDimensions])}]"
            params["documentId"] = documentId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result
        case bool(), Dimension(), Unset(), Unset(), str():
            path = "/api/PurchasesDimensions/Update"
            params = dict()
            params["buffer"] = buffer
            data = documentDimension.model_dump_json(exclude_unset=True)
            params["documentNumber"] = documentNumber
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result
        case Unset(), Dimension(), Unset(), int(), Unset():
            path = "/api/PurchasesDimensions/Update"
            params = dict()
            data = documentDimension.model_dump_json(exclude_unset=True)
            params["documentId"] = documentId
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
    path = "/api/PurchasesDimensions/Aspects"
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
            path = "/api/PurchasesDimensions/UpdateMultiPositionsList"
            params = dict()
            data = f"[{','.join([elem.model_dump_json(exclude_unset=True) for elem in positionDimension])}]"
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result
        case Unset(), list(_), int() if all(isinstance(item, Dimension) for item in positionDimensions):
            path = "/api/PurchasesDimensions/UpdatePositionList"
            params = dict()
            data = f"[{','.join([elem.model_dump_json(exclude_unset=True) for elem in positionDimensions])}]"
            params["positionId"] = positionId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result
        case Dimension(), Unset(), int():
            path = "/api/PurchasesDimensions/UpdatePosition"
            params = dict()
            data = positionDimension.model_dump_json(exclude_unset=True)
            params["positionId"] = positionId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result
