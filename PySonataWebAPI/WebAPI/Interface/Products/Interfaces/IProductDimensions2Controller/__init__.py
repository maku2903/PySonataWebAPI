from .....Client import (
    AsyncAPI,
    ClientResponse,
    IHttpActionResult,
)
from .....Constants import (
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


async def Get(
    api: AsyncAPI,
    productCode: str = Unset(),
    productId: int = Unset()
) -> IHttpActionResult[List[Dimension]]:
    match productCode, productId:
        case str(), Unset():
            path = "/api/v2/ProductDimensions"
            params = dict()
            data = None
            params["productCode"] = productCode
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[Dimension])
            return result
        case Unset(), int():
            path = "/api/v2/ProductDimensions"
            params = dict()
            data = None
            params["productId"] = productId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[Dimension])
            return result
