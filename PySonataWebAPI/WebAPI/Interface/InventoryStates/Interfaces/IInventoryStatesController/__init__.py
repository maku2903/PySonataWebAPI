from .....Client import (
    AsyncAPI,
    ClientResponse,
    IHttpActionResult,
)
from .....Constants import (
    Unset,
)
from ...ViewModels import (
    InventoryState,
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
) -> IHttpActionResult[List[InventoryState]]:
    """
    ['List[InventoryState]']
    :param api:
    :type api: AsyncAPI
    :returns: List[InventoryState]
    :rtype: List[InventoryState]
    """
    path = "/api/InventoryStates"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[InventoryState])
    return result


async def GetByProductCode(
    api: AsyncAPI, code: str
) -> IHttpActionResult[List[InventoryState]]:
    """
    ['List[InventoryState]']
    :param api:
    :type api: AsyncAPI
    :param code:
    :type code: str
    :returns: List[InventoryState]
    :rtype: List[InventoryState]
    """
    path = "/api/InventoryStates/ByProduct"
    params = dict()
    data = None
    params["code"] = code

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[InventoryState])
    return result


async def GetByProductId(
    api: AsyncAPI, id: int
) -> IHttpActionResult[List[InventoryState]]:
    """
    ['List[InventoryState]']
    :param api:
    :type api: AsyncAPI
    :param id:
    :type id: int
    :returns: List[InventoryState]
    :rtype: List[InventoryState]
    """
    path = "/api/InventoryStates/ByProduct"
    params = dict()
    data = None
    params["id"] = id

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[InventoryState])
    return result


async def GetByProductIdAndWarehouseId(
    api: AsyncAPI, productId: int, warehouseId: int
) -> IHttpActionResult[InventoryState]:
    """
    ['InventoryState']
    :param api:
    :type api: AsyncAPI
    :param productId:
    :type productId: int
    :param warehouseId:
    :type warehouseId: int
    :returns: InventoryState
    :rtype: InventoryState
    """
    path = "/api/InventoryStates/ByProductAndWarehouse"
    params = dict()
    data = None
    params["productId"] = productId

    params["warehouseId"] = warehouseId

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, InventoryState)
    return result


async def GetByWarehouseCode(
    api: AsyncAPI, code: str
) -> IHttpActionResult[List[InventoryState]]:
    """
    ['List[InventoryState]']
    :param api:
    :type api: AsyncAPI
    :param code:
    :type code: str
    :returns: List[InventoryState]
    :rtype: List[InventoryState]
    """
    path = "/api/InventoryStates/ByWarehouse"
    params = dict()
    data = None
    params["code"] = code

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[InventoryState])
    return result


async def GetByWarehouseId(
    api: AsyncAPI, id: int
) -> IHttpActionResult[List[InventoryState]]:
    """
    ['List[InventoryState]']
    :param api:
    :type api: AsyncAPI
    :param id:
    :type id: int
    :returns: List[InventoryState]
    :rtype: List[InventoryState]
    """
    path = "/api/InventoryStates/ByWarehouse"
    params = dict()
    data = None
    params["id"] = id

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[InventoryState])
    return result


async def GetChanges(
    api: AsyncAPI, date: datetime
) -> IHttpActionResult[List[InventoryState]]:
    """
    ['List[InventoryState]']
    :param api:
    :type api: AsyncAPI
    :param date:
    :type date: datetime
    :returns: List[InventoryState]
    :rtype: List[InventoryState]
    """
    path = "/api/InventoryStates/Changes"
    params = dict()
    data = None
    params["date"] = date

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[InventoryState])
    return result
