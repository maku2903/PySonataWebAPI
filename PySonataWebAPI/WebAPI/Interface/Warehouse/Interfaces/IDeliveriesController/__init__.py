from .....Client import (
    AsyncAPI,
    ClientResponse,
    IHttpActionResult,
)
from .....Constants import (
    Unset,
)
from ...ViewModels import (
    DeliveryListElement,
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


async def GetInWarehouse(
    api: AsyncAPI,
    productCode: str = Unset(),
    productId: int = Unset(),
    warehouseCode: str = Unset(),
    warehouseId: int = Unset()
) -> IHttpActionResult[List[DeliveryListElement]]:
    match productCode, productId, warehouseCode, warehouseId:
        case str(), Unset(), str(), Unset():
            path = "/api/Deliveries/InWarehouse"
            params = dict()
            data = None
            params["productCode"] = productCode
            params["warehouseCode"] = warehouseCode
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[DeliveryListElement])
            return result
        case Unset(), int(), Unset(), int():
            path = "/api/Deliveries/InWarehouse"
            params = dict()
            data = None
            params["productId"] = productId
            params["warehouseId"] = warehouseId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[DeliveryListElement])
            return result
