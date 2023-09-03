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
from ...ViewModels import (
    Document,
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


async def GetAccountChartByIdAndYear(
    api: AsyncAPI, id: int, yearId: int
) -> IHttpActionResult[List[Dimension]]:
    """
    ['List[Dimension]']
    :param api:
    :type api: AsyncAPI
    :param id:
    :type id: int
    :param yearId:
    :type yearId: int
    :returns: List[Dimension]
    :rtype: List[Dimension]
    """
    path = "/api/FKDimensions/AccountChart"
    params = dict()
    data = None
    params["id"] = id

    params["yearId"] = yearId

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
    path = "/api/FKDimensions/Classification"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DimensionClassification])
    return result


async def GetDocumentByIdAndYear(
    api: AsyncAPI, id: int, yearId: int
) -> IHttpActionResult[Document]:
    """
    ['Document']
    :param api:
    :type api: AsyncAPI
    :param id:
    :type id: int
    :param yearId:
    :type yearId: int
    :returns: Document
    :rtype: Document
    """
    path = "/api/FKDimensions/Document"
    params = dict()
    data = None
    params["id"] = id

    params["yearId"] = yearId

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, Document)
    return result
