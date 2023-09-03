from .....Client import (
    AsyncAPI,
    ClientResponse,
    IHttpActionResult,
)
from .....Constants import (
    Unset,
)
from ...ViewModels import (
    Order,
    OrderEdit,
    OrderFV,
    OrderIssue,
    OrderWZ,
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


async def AddNew(
    api: AsyncAPI, issue: bool, order: OrderIssue
) -> IHttpActionResult[Order]:
    """
    ['Order']
    :param api:
    :type api: AsyncAPI
    :param issue:
    :type issue: bool
    :param order:
    :type order: OrderIssue
    :returns: Order
    :rtype: Order
    """
    path = "/api/OrdersIssue/New"
    params = dict()
    params["issue"] = issue

    data = order.model_dump_json(exclude_unset=True)
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="POST", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, Order)
    return result


async def ChangeDocumentNumber(
    api: AsyncAPI, id: int, number: str
) -> IHttpActionResult[None]:
    """
    []
    :param api:
    :type api: AsyncAPI
    :param id:
    :type id: int
    :param number:
    :type number: str
    :returns: 
    :rtype: 
    """
    path = "/api/OrdersIssue/DocumentNumber"
    params = dict()
    data = None
    params["id"] = id

    params["number"] = number

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="PATCH", path=path, params=params, headers=headers, data=data)
    # no return
    result = await IHttpActionResult.create(response, None)
    return result


async def Delete(
    api: AsyncAPI,
    buffer: bool = Unset(),
    id: int = Unset(),
    number: str = Unset()
) -> IHttpActionResult[None]:
    match buffer, id, number:
        case bool(), Unset(), str():
            path = "/api/OrdersIssue/Delete"
            params = dict()
            data = None
            params["buffer"] = buffer
            params["number"] = number
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="DELETE", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result
        case Unset(), int(), Unset():
            path = "/api/OrdersIssue/Delete"
            params = dict()
            data = None
            params["id"] = id
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="DELETE", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result


async def Edit(
    api: AsyncAPI, order: OrderEdit
) -> IHttpActionResult[Order]:
    """
    ['Order']
    :param api:
    :type api: AsyncAPI
    :param order:
    :type order: OrderEdit
    :returns: Order
    :rtype: Order
    """
    path = "/api/OrdersIssue/Edit"
    params = dict()
    data = order.model_dump_json(exclude_unset=True)
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, Order)
    return result


async def Issue(
    api: AsyncAPI,
    id: int = Unset(),
    number: str = Unset()
) -> IHttpActionResult[Order]:
    match id, number:
        case int(), Unset():
            path = "/api/OrdersIssue/InBuffer"
            params = dict()
            data = None
            params["id"] = id
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, Order)
            return result
        case Unset(), str():
            path = "/api/OrdersIssue/InBuffer"
            params = dict()
            data = None
            params["number"] = number
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, Order)
            return result


async def IssueFV(
    api: AsyncAPI,
    orderId: int = Unset(),
    orderNumber: str = Unset()
) -> IHttpActionResult[List[OrderFV]]:
    match orderId, orderNumber:
        case Unset(), str():
            path = "/api/OrdersIssue/FV"
            params = dict()
            data = None
            params["orderNumber"] = orderNumber
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[OrderFV])
            return result
        case int(), Unset():
            path = "/api/OrdersIssue/FV"
            params = dict()
            data = None
            params["orderId"] = orderId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[OrderFV])
            return result


async def IssueWZ(
    api: AsyncAPI,
    orderId: int = Unset(),
    orderNumber: str = Unset()
) -> IHttpActionResult[List[OrderWZ]]:
    match orderId, orderNumber:
        case int(), Unset():
            path = "/api/OrdersIssue/WZ"
            params = dict()
            data = None
            params["orderId"] = orderId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[OrderWZ])
            return result
        case Unset(), str():
            path = "/api/OrdersIssue/WZ"
            params = dict()
            data = None
            params["orderNumber"] = orderNumber
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[OrderWZ])
            return result
