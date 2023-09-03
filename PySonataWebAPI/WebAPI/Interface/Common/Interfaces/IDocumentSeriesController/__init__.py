from .....Client import (
    AsyncAPI,
    ClientResponse,
    IHttpActionResult,
)
from .....Constants import (
    Unset,
)
from ...ViewModels import (
    DocumentSeries,
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
    api: AsyncAPI, documentTypeId: int
) -> IHttpActionResult[List[DocumentSeries]]:
    """
    ['List[DocumentSeries]']
    :param api:
    :type api: AsyncAPI
    :param documentTypeId:
    :type documentTypeId: int
    :returns: List[DocumentSeries]
    :rtype: List[DocumentSeries]
    """
    path = "/api/DocumentSeries"
    params = dict()
    data = None
    params["documentTypeId"] = documentTypeId

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentSeries])
    return result
