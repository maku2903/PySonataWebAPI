from ......Client import (
    AsyncAPI,
    ClientResponse,
    IHttpActionResult,
)
from ......Constants import (
    Unset,
)
from ...ViewModels import (
    Year,
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


Get_T = TypeVar('Get_T', IHttpActionResult[Year], IHttpActionResult[List[Year]])


@overload
async def Get(
    api: AsyncAPI, date: datetime
) -> IHttpActionResult[Year]: ...


@overload
async def Get(
    api: AsyncAPI, 
) -> IHttpActionResult[List[Year]]: ...


async def Get(
    api: AsyncAPI,
    date: datetime = Unset()
) -> Get_T:
    match date:
        case datetime():
            path = "/api/FKYears"
            params = dict()
            data = None
            params["date"] = date
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, Year)
            return result
        case Unset():
            path = "/api/FKYears"
            params = dict()
            data = None
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[Year])
            return result
