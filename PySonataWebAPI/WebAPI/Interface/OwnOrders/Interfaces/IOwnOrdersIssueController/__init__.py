from .....Client import (
    AsyncAPI,
    ClientResponse,
    IHttpActionResult,
)
from .....Constants import (
    Unset,
)
from ...ViewModels import (
    OwnOrder,
    OwnOrderIssue,
    OwnOrderPZ,
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
    api: AsyncAPI, issue: bool, order: OwnOrderIssue
) -> IHttpActionResult[OwnOrder]:
    """
    ['OwnOrder']
    :param api:
    :type api: AsyncAPI
    :param issue:
    :type issue: bool
    :param order:
    :type order: OwnOrderIssue
    :returns: OwnOrder
    :rtype: OwnOrder
    """
    path = "/api/OwnOrdersIssue/New"
    params = dict()
    params["issue"] = issue

    data = order.model_dump_json(exclude_unset=True)
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="POST", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, OwnOrder)
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
    path = "/api/OwnOrdersIssue/DocumentNumber"
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
        case Unset(), int(), Unset():
            path = "/api/OwnOrdersIssue/Delete"
            params = dict()
            data = None
            params["id"] = id
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="DELETE", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result
        case bool(), Unset(), str():
            path = "/api/OwnOrdersIssue/Delete"
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


async def Issue(
    api: AsyncAPI,
    id: int = Unset(),
    number: str = Unset()
) -> IHttpActionResult[OwnOrder]:
    match id, number:
        case Unset(), str():
            path = "/api/OwnOrdersIssue/InBuffer"
            params = dict()
            data = None
            params["number"] = number
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, OwnOrder)
            return result
        case int(), Unset():
            path = "/api/OwnOrdersIssue/InBuffer"
            params = dict()
            data = None
            params["id"] = id
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, OwnOrder)
            return result


async def IssuePZ(
    api: AsyncAPI,
    orderId: int = Unset(),
    orderNumber: str = Unset()
) -> IHttpActionResult[List[OwnOrderPZ]]:
    match orderId, orderNumber:
        case int(), Unset():
            path = "/api/OwnOrdersIssue/PZ"
            params = dict()
            data = None
            params["orderId"] = orderId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[OwnOrderPZ])
            return result
        case Unset(), str():
            path = "/api/OwnOrdersIssue/PZ"
            params = dict()
            data = None
            params["orderNumber"] = orderNumber
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[OwnOrderPZ])
            return result
