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


async def GetByCode(
    api: AsyncAPI, contractorCode: str
) -> IHttpActionResult[List[Dimension]]:
    """
    ['List[Dimension]']
    :param api:
    :type api: AsyncAPI
    :param contractorCode:
    :type contractorCode: str
    :returns: List[Dimension]
    :rtype: List[Dimension]
    """
    path = "/api/v2/FKContractorDimensions"
    params = dict()
    data = None
    params["contractorCode"] = contractorCode

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[Dimension])
    return result


async def GetById(
    api: AsyncAPI, contractorId: int
) -> IHttpActionResult[List[Dimension]]:
    """
    ['List[Dimension]']
    :param api:
    :type api: AsyncAPI
    :param contractorId:
    :type contractorId: int
    :returns: List[Dimension]
    :rtype: List[Dimension]
    """
    path = "/api/v2/FKContractorDimensions"
    params = dict()
    data = None
    params["contractorId"] = contractorId

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[Dimension])
    return result


async def GetByPosition(
    api: AsyncAPI, contractorPosition: int
) -> IHttpActionResult[List[Dimension]]:
    """
    ['List[Dimension]']
    :param api:
    :type api: AsyncAPI
    :param contractorPosition:
    :type contractorPosition: int
    :returns: List[Dimension]
    :rtype: List[Dimension]
    """
    path = "/api/v2/FKContractorDimensions"
    params = dict()
    data = None
    params["contractorPosition"] = contractorPosition

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[Dimension])
    return result
