from .....Client import (
    AsyncAPI,
    ClientResponse,
    IHttpActionResult,
)
from .....Constants import (
    Unset,
)
from ...ViewModels import (
    PriceType,
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


async def GetSalePriceTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[PriceType]]:
    """
    ['List[PriceType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[PriceType]
    :rtype: List[PriceType]
    """
    path = "/api/Prices/SalePriceTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[PriceType])
    return result
