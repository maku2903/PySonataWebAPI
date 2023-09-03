from .....Client import (
    AsyncAPI,
    ClientResponse,
    IHttpActionResult,
)
from .....Constants import (
    Unset,
)
from ...ViewModels.PriceLists import (
    PriceList,
    PriceListListElement,
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


Get_T = TypeVar('Get_T', IHttpActionResult[PriceList], IHttpActionResult[List[PriceListListElement]])


@overload
async def Get(
    api: AsyncAPI, 
) -> IHttpActionResult[List[PriceListListElement]]: ...


@overload
async def Get(
    api: AsyncAPI, id: int
) -> IHttpActionResult[PriceList]: ...


@overload
async def Get(
    api: AsyncAPI, code: str
) -> IHttpActionResult[PriceList]: ...


async def Get(
    api: AsyncAPI,
    code: str = Unset(),
    id: int = Unset()
) -> Get_T:
    match code, id:
        case Unset(), Unset():
            path = "/api/PriceLists"
            params = dict()
            data = None
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[PriceListListElement])
            return result
        case Unset(), int():
            path = "/api/PriceLists"
            params = dict()
            data = None
            params["id"] = id
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, PriceList)
            return result
        case str(), Unset():
            path = "/api/PriceLists"
            params = dict()
            data = None
            params["code"] = code
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, PriceList)
            return result


async def IncrementalSync(
    api: AsyncAPI, dateFrom: datetime
) -> IHttpActionResult[None]:
    """
    []
    :param api:
    :type api: AsyncAPI
    :param dateFrom:
    :type dateFrom: datetime
    :returns: 
    :rtype: 
    """
    path = "/api/PriceLists/IncrementalSync"
    params = dict()
    data = None
    params["dateFrom"] = dateFrom

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    # no return
    result = await IHttpActionResult.create(response, None)
    return result
