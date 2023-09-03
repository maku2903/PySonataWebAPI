from .....Client import (
    AsyncAPI,
    ClientResponse,
    IHttpActionResult,
)
from .....Constants import (
    Unset,
)
from ...ViewModels import (
    AgriculturalPromotionFund,
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
) -> IHttpActionResult[List[AgriculturalPromotionFund]]:
    """
    ['List[AgriculturalPromotionFund]']
    :param api:
    :type api: AsyncAPI
    :returns: List[AgriculturalPromotionFund]
    :rtype: List[AgriculturalPromotionFund]
    """
    path = "/api/AgriculturalPromotionFunds"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[AgriculturalPromotionFund])
    return result
