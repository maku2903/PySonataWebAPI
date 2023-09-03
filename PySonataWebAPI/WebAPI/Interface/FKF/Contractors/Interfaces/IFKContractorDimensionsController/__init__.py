from ......Client import (
    AsyncAPI,
    ClientResponse,
    IHttpActionResult,
)
from ......Constants import (
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
    path = "/api/FKContractorDimensions/Classification"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DimensionClassification])
    return result


async def UpdateByCode(
    api: AsyncAPI,
    contractorCode: str = Unset(),
    contractorDimension: Dimension = Unset(),
    contractorDimensions: List[Dimension] = Unset()
) -> IHttpActionResult[None]:
    match contractorCode, contractorDimension, contractorDimensions:
        case str(), Dimension(), Unset():
            path = "/api/FKContractorDimensions/Update"
            params = dict()
            params["contractorCode"] = contractorCode
            data = contractorDimension.model_dump_json(exclude_unset=True)
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result
        case str(), Unset(), list(_) if all(isinstance(item, Dimension) for item in contractorDimensions):
            path = "/api/FKContractorDimensions/UpdateList"
            params = dict()
            params["contractorCode"] = contractorCode
            data = f"[{','.join([elem.model_dump_json(exclude_unset=True) for elem in contractorDimensions])}]"
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result


async def UpdateById(
    api: AsyncAPI,
    contractorDimension: Dimension = Unset(),
    contractorDimensions: List[Dimension] = Unset(),
    contractorId: int = Unset()
) -> IHttpActionResult[None]:
    match contractorDimension, contractorDimensions, contractorId:
        case Unset(), list(_), int() if all(isinstance(item, Dimension) for item in contractorDimensions):
            path = "/api/FKContractorDimensions/UpdateList"
            params = dict()
            data = f"[{','.join([elem.model_dump_json(exclude_unset=True) for elem in contractorDimensions])}]"
            params["contractorId"] = contractorId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result
        case Dimension(), Unset(), int():
            path = "/api/FKContractorDimensions/Update"
            params = dict()
            data = contractorDimension.model_dump_json(exclude_unset=True)
            params["contractorId"] = contractorId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result


async def UpdateByPosition(
    api: AsyncAPI,
    contractorDimension: Dimension = Unset(),
    contractorDimensions: List[Dimension] = Unset(),
    contractorPosition: int = Unset()
) -> IHttpActionResult[None]:
    match contractorDimension, contractorDimensions, contractorPosition:
        case Dimension(), Unset(), int():
            path = "/api/FKContractorDimensions/Update"
            params = dict()
            data = contractorDimension.model_dump_json(exclude_unset=True)
            params["contractorPosition"] = contractorPosition
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result
        case Unset(), list(_), int() if all(isinstance(item, Dimension) for item in contractorDimensions):
            path = "/api/FKContractorDimensions/UpdateList"
            params = dict()
            data = f"[{','.join([elem.model_dump_json(exclude_unset=True) for elem in contractorDimensions])}]"
            params["contractorPosition"] = contractorPosition
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result
