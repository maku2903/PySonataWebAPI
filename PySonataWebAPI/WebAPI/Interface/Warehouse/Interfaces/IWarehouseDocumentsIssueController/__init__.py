from .....Client import (
    AsyncAPI,
    ClientResponse,
    IHttpActionResult,
)
from .....Constants import (
    Unset,
)
from ...ViewModels import (
    WarehouseDocument,
    WarehouseDocumentEdit,
    WarehouseDocumentIssue,
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
    api: AsyncAPI, document: WarehouseDocumentIssue, issue: bool
) -> IHttpActionResult[WarehouseDocument]:
    """
    ['WarehouseDocument']
    :param api:
    :type api: AsyncAPI
    :param document:
    :type document: WarehouseDocumentIssue
    :param issue:
    :type issue: bool
    :returns: WarehouseDocument
    :rtype: WarehouseDocument
    """
    path = "/api/WarehouseDocumentsIssue/New"
    params = dict()
    data = document.model_dump_json(exclude_unset=True)
    params["issue"] = issue

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="POST", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, WarehouseDocument)
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
    path = "/api/WarehouseDocumentsIssue/DocumentNumber"
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


async def Edit(
    api: AsyncAPI, document: WarehouseDocumentEdit
) -> IHttpActionResult[WarehouseDocument]:
    """
    ['WarehouseDocument']
    :param api:
    :type api: AsyncAPI
    :param document:
    :type document: WarehouseDocumentEdit
    :returns: WarehouseDocument
    :rtype: WarehouseDocument
    """
    path = "/api/WarehouseDocumentsIssue/Edit"
    params = dict()
    data = document.model_dump_json(exclude_unset=True)
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, WarehouseDocument)
    return result


async def Issue(
    api: AsyncAPI,
    id: int = Unset(),
    number: str = Unset()
) -> IHttpActionResult[WarehouseDocument]:
    match id, number:
        case Unset(), str():
            path = "/api/WarehouseDocumentsIssue/InBuffer"
            params = dict()
            data = None
            params["number"] = number
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, WarehouseDocument)
            return result
        case int(), Unset():
            path = "/api/WarehouseDocumentsIssue/InBuffer"
            params = dict()
            data = None
            params["id"] = id
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, WarehouseDocument)
            return result


async def IssueMMPlus(
    api: AsyncAPI,
    documentId: int = Unset(),
    documentNumber: str = Unset()
) -> IHttpActionResult[None]:
    match documentId, documentNumber:
        case int(), Unset():
            path = "/api/WarehouseDocumentsIssue/MMPlus"
            params = dict()
            data = None
            params["documentId"] = documentId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result
        case Unset(), str():
            path = "/api/WarehouseDocumentsIssue/MMPlus"
            params = dict()
            data = None
            params["documentNumber"] = documentNumber
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result
