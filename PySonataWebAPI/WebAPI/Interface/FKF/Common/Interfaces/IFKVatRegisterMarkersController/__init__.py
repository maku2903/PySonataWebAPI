from ......Client import (
    AsyncAPI,
    ClientResponse,
    IHttpActionResult,
)
from ......Constants import (
    Unset,
)
from ...ViewModels import (
    VatRegisterMarker,
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
) -> IHttpActionResult[List[VatRegisterMarker]]:
    """
    ['List[VatRegisterMarker]']
    :param api:
    :type api: AsyncAPI
    :returns: List[VatRegisterMarker]
    :rtype: List[VatRegisterMarker]
    """
    path = "/api/FKVatRegisterMarkers"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[VatRegisterMarker])
    return result
