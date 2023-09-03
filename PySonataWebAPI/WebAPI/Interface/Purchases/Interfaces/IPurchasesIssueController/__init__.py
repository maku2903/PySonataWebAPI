from .....Client import (
    AsyncAPI,
    ClientResponse,
    IHttpActionResult,
)
from .....Constants import (
    Unset,
)
from ...ViewModels import (
    PurchaseCorrection,
    PurchaseCorrectionIssue,
    PurchaseDocument,
    PurchaseDocumentIssue,
    PurchaseDocumentPZ,
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


AddNew_T = TypeVar('AddNew_T', IHttpActionResult[PurchaseCorrection], IHttpActionResult[PurchaseDocument])


@overload
async def AddNew(
    api: AsyncAPI, document: PurchaseDocumentIssue, issue: bool
) -> IHttpActionResult[PurchaseDocument]: ...


@overload
async def AddNew(
    api: AsyncAPI, correction: PurchaseCorrectionIssue, issue: bool
) -> IHttpActionResult[PurchaseCorrection]: ...


async def AddNew(
    api: AsyncAPI,
    correction: PurchaseCorrectionIssue = Unset(),
    document: PurchaseDocumentIssue = Unset(),
    issue: bool = Unset()
) -> AddNew_T:
    match correction, document, issue:
        case Unset(), PurchaseDocumentIssue(), bool():
            path = "/api/PurchasesIssue/New"
            params = dict()
            data = document.model_dump_json(exclude_unset=True)
            params["issue"] = issue
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="POST", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, PurchaseDocument)
            return result
        case PurchaseCorrectionIssue(), Unset(), bool():
            path = "/api/PurchasesIssue/NewCorrection"
            params = dict()
            data = correction.model_dump_json(exclude_unset=True)
            params["issue"] = issue
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="POST", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, PurchaseCorrection)
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
    path = "/api/PurchasesIssue/DocumentNumber"
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


Issue_T = TypeVar('Issue_T', IHttpActionResult[PurchaseCorrection], IHttpActionResult[PurchaseDocument])


@overload
async def Issue(
    api: AsyncAPI, number: str
) -> Union[IHttpActionResult[PurchaseCorrection], IHttpActionResult[PurchaseDocument], IHttpActionResult[PurchaseDocument]]: ...


@overload
async def Issue(
    api: AsyncAPI, id: int
) -> Union[IHttpActionResult[PurchaseCorrection], IHttpActionResult[PurchaseDocument], IHttpActionResult[PurchaseDocument]]: ...


async def Issue(
    api: AsyncAPI,
    id: int = Unset(),
    number: str = Unset()
) -> Issue_T:
    match id, number:
        case Unset(), str():
            path = "/api/PurchasesIssue/InBuffer"
            params = dict()
            data = None
            params["number"] = number
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            # todo: many returns PurchaseCorrectionPurchaseDocumentPurchaseDocument
            result = await IHttpActionResult.create(response, None)
            return result
        case int(), Unset():
            path = "/api/PurchasesIssue/InBuffer"
            params = dict()
            data = None
            params["id"] = id
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            # todo: many returns PurchaseCorrectionPurchaseDocumentPurchaseDocument
            result = await IHttpActionResult.create(response, None)
            return result


async def IssuePZ(
    api: AsyncAPI,
    documentId: int = Unset(),
    documentNumber: str = Unset()
) -> IHttpActionResult[List[PurchaseDocumentPZ]]:
    match documentId, documentNumber:
        case int(), Unset():
            path = "/api/PurchasesIssue/PZ"
            params = dict()
            data = None
            params["documentId"] = documentId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[PurchaseDocumentPZ])
            return result
        case Unset(), str():
            path = "/api/PurchasesIssue/PZ"
            params = dict()
            data = None
            params["documentNumber"] = documentNumber
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[PurchaseDocumentPZ])
            return result


async def IssuePZCorrection(
    api: AsyncAPI,
    documentId: int = Unset(),
    documentNumber: str = Unset(),
    issue: bool = Unset()
) -> IHttpActionResult[List[PurchaseDocumentPZ]]:
    match documentId, documentNumber, issue:
        case Unset(), str(), bool():
            path = "/api/PurchasesIssue/PZCorrection"
            params = dict()
            data = None
            params["documentNumber"] = documentNumber
            params["issue"] = issue
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[PurchaseDocumentPZ])
            return result
        case int(), Unset(), bool():
            path = "/api/PurchasesIssue/PZCorrection"
            params = dict()
            data = None
            params["documentId"] = documentId
            params["issue"] = issue
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[PurchaseDocumentPZ])
            return result
