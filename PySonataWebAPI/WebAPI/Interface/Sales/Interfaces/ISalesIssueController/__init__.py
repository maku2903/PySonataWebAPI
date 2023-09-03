from .....Client import (
    AsyncAPI,
    ClientResponse,
    IHttpActionResult,
)
from .....Constants import (
    Unset,
)
from ...ViewModels import (
    AdvancePaymentOptions,
    SaleCorrection,
    SaleCorrectionIssue,
    SaleDocument,
    SaleDocumentIssue,
    SaleDocumentWZ,
)
from ...ViewModels.DocumentIssue import (
    DocumentIssueSettlement,
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


AddNew_T = TypeVar('AddNew_T', IHttpActionResult[SaleCorrection], IHttpActionResult[SaleDocument])


@overload
async def AddNew(
    api: AsyncAPI, document: SaleDocumentIssue, issue: bool
) -> IHttpActionResult[SaleDocument]: ...


@overload
async def AddNew(
    api: AsyncAPI, correction: SaleCorrectionIssue, issue: bool
) -> IHttpActionResult[SaleCorrection]: ...


async def AddNew(
    api: AsyncAPI,
    correction: SaleCorrectionIssue = Unset(),
    document: SaleDocumentIssue = Unset(),
    issue: bool = Unset()
) -> AddNew_T:
    match correction, document, issue:
        case Unset(), SaleDocumentIssue(), bool():
            path = "/api/SalesIssue/New"
            params = dict()
            data = document.model_dump_json(exclude_unset=True)
            params["issue"] = issue
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="POST", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, SaleDocument)
            return result
        case SaleCorrectionIssue(), Unset(), bool():
            path = "/api/SalesIssue/NewCorrection"
            params = dict()
            data = correction.model_dump_json(exclude_unset=True)
            params["issue"] = issue
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="POST", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, SaleCorrection)
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
    path = "/api/SalesIssue/DocumentNumber"
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


Issue_T = TypeVar('Issue_T', IHttpActionResult[SaleCorrection], IHttpActionResult[SaleDocument])


@overload
async def Issue(
    api: AsyncAPI, number: str
) -> Union[IHttpActionResult[SaleCorrection], IHttpActionResult[SaleDocument], IHttpActionResult[SaleDocument]]: ...


@overload
async def Issue(
    api: AsyncAPI, id: int
) -> Union[IHttpActionResult[SaleCorrection], IHttpActionResult[SaleDocument], IHttpActionResult[SaleDocument]]: ...


async def Issue(
    api: AsyncAPI,
    id: int = Unset(),
    number: str = Unset()
) -> Issue_T:
    match id, number:
        case Unset(), str():
            path = "/api/SalesIssue/InBuffer"
            params = dict()
            data = None
            params["number"] = number
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            # todo: many returns SaleCorrectionSaleDocumentSaleDocument
            result = await IHttpActionResult.create(response, None)
            return result
        case int(), Unset():
            path = "/api/SalesIssue/InBuffer"
            params = dict()
            data = None
            params["id"] = id
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            # todo: many returns SaleCorrectionSaleDocumentSaleDocument
            result = await IHttpActionResult.create(response, None)
            return result


async def IssueAdvancePayment(
    api: AsyncAPI,
    documentId: int = Unset(),
    documentNumber: str = Unset(),
    options: AdvancePaymentOptions = Unset()
) -> IHttpActionResult[SaleDocument]:
    match documentId, documentNumber, options:
        case Unset(), str(), AdvancePaymentOptions():
            path = "/api/SalesIssue/AdvancePayment"
            params = dict()
            params["documentNumber"] = documentNumber
            data = options.model_dump_json(exclude_unset=True)
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, SaleDocument)
            return result
        case int(), Unset(), AdvancePaymentOptions():
            path = "/api/SalesIssue/AdvancePayment"
            params = dict()
            params["documentId"] = documentId
            data = options.model_dump_json(exclude_unset=True)
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, SaleDocument)
            return result


async def IssuePN(
    api: AsyncAPI,
    documentId: int = Unset(),
    documentNumber: str = Unset(),
    settlement: DocumentIssueSettlement = Unset()
) -> IHttpActionResult[None]:
    match documentId, documentNumber, settlement:
        case Unset(), str(), DocumentIssueSettlement():
            path = "/api/SalesIssue/IssuePayment"
            params = dict()
            params["documentNumber"] = documentNumber
            data = settlement.model_dump_json(exclude_unset=True)
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result
        case int(), Unset(), DocumentIssueSettlement():
            path = "/api/SalesIssue/IssuePayment"
            params = dict()
            params["documentId"] = documentId
            data = settlement.model_dump_json(exclude_unset=True)
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result


async def IssueWZ(
    api: AsyncAPI,
    documentId: int = Unset(),
    documentNumber: str = Unset(),
    inBuffer: bool = Unset()
) -> IHttpActionResult[List[SaleDocumentWZ]]:
    match documentId, documentNumber, inBuffer:
        case int(), Unset(), bool():
            path = "/api/SalesIssue/WZ"
            params = dict()
            data = None
            params["documentId"] = documentId
            params["inBuffer"] = inBuffer
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[SaleDocumentWZ])
            return result
        case Unset(), str(), bool():
            path = "/api/SalesIssue/WZ"
            params = dict()
            data = None
            params["documentNumber"] = documentNumber
            params["inBuffer"] = inBuffer
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[SaleDocumentWZ])
            return result


async def IssueWZCorrection(
    api: AsyncAPI,
    documentId: int = Unset(),
    documentNumber: str = Unset(),
    issue: bool = Unset()
) -> IHttpActionResult[List[SaleDocumentWZ]]:
    match documentId, documentNumber, issue:
        case int(), Unset(), bool():
            path = "/api/SalesIssue/IssueWZCorrection"
            params = dict()
            data = None
            params["documentId"] = documentId
            params["issue"] = issue
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[SaleDocumentWZ])
            return result
        case Unset(), str(), bool():
            path = "/api/SalesIssue/IssueWZCorrection"
            params = dict()
            data = None
            params["documentNumber"] = documentNumber
            params["issue"] = issue
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[SaleDocumentWZ])
            return result
