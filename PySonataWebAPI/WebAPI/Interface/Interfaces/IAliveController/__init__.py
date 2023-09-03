from ....Client import (
    AsyncAPI,
    ClientResponse,
    IHttpActionResult,
)
from ....Constants import (
    Unset,
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
) -> IHttpActionResult[None]:
    """
    []
    :param api:
    :type api: AsyncAPI
    :returns: 
    :rtype: 
    """
    path = "/api/Alive"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    # no return
    result = await IHttpActionResult.create(response, None)
    return result
