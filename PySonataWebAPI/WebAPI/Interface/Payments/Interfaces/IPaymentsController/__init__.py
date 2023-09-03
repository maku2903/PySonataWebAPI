from .....Client import (
    AsyncAPI,
    ClientResponse,
    IHttpActionResult,
)
from .....Constants import (
    Unset,
)
from ....Common.ViewModels import (
    DocumentSeries,
    DocumentType,
    PDF,
)
from ....Enums import (
    enumOrderByType,
)
from ....ViewModels import (
    Page,
)
from ...ViewModels import (
    Payment,
    PaymentListElement,
)
from ...ViewModels.Issue import (
    PaymentIssue,
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


Get_T = TypeVar('Get_T', IHttpActionResult[Payment], IHttpActionResult[List[PaymentListElement]])


@overload
async def Get(
    api: AsyncAPI, 
) -> IHttpActionResult[List[PaymentListElement]]: ...


@overload
async def Get(
    api: AsyncAPI, buffer: bool, number: str
) -> IHttpActionResult[Payment]: ...


@overload
async def Get(
    api: AsyncAPI, id: int
) -> IHttpActionResult[Payment]: ...


async def Get(
    api: AsyncAPI,
    buffer: bool = Unset(),
    id: int = Unset(),
    number: str = Unset()
) -> Get_T:
    match buffer, id, number:
        case Unset(), Unset(), Unset():
            path = "/api/Payments"
            params = dict()
            data = None
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[PaymentListElement])
            return result
        case bool(), Unset(), str():
            path = "/api/Payments"
            params = dict()
            data = None
            params["buffer"] = buffer
            params["number"] = number
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, Payment)
            return result
        case Unset(), int(), Unset():
            path = "/api/Payments"
            params = dict()
            data = None
            params["id"] = id
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, Payment)
            return result


async def GetBPDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Payments/BPDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetBWDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Payments/BWDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetDocumentSeries(
    api: AsyncAPI, documentTypeId: int
) -> IHttpActionResult[List[DocumentSeries]]:
    """
    ['List[DocumentSeries]']
    :param api:
    :type api: AsyncAPI
    :param documentTypeId:
    :type documentTypeId: int
    :returns: List[DocumentSeries]
    :rtype: List[DocumentSeries]
    """
    path = "/api/Payments/DocumentSeries"
    params = dict()
    data = None
    params["documentTypeId"] = documentTypeId

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentSeries])
    return result


async def GetIPDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Payments/IPDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetIWDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Payments/IWDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetKPDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Payments/KPDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetKWDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Payments/KWDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetList(
    api: AsyncAPI, dateFrom: Optional[datetime], dateTo: Optional[datetime]
) -> IHttpActionResult[List[PaymentListElement]]:
    """
    ['List[PaymentListElement]']
    :param api:
    :type api: AsyncAPI
    :param dateFrom:
    :type dateFrom: datetime | None
    :param dateTo:
    :type dateTo: datetime | None
    :returns: List[PaymentListElement]
    :rtype: List[PaymentListElement]
    """
    path = "/api/Payments/Filter"
    params = dict()
    data = None
    if dateFrom is not None:
        params["dateFrom"] = dateFrom

    if dateTo is not None:
        params["dateTo"] = dateTo

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[PaymentListElement])
    return result


async def GetListByContractor(
    api: AsyncAPI,
    contractorCode: str = Unset(),
    contractorId: int = Unset(),
    dateFrom: Optional[datetime] = Unset(),
    dateTo: Optional[datetime] = Unset()
) -> IHttpActionResult[List[PaymentListElement]]:
    match contractorCode, contractorId, dateFrom, dateTo:
        case str(), Unset(), datetime() | None | Unset(), datetime() | None | Unset():
            path = "/api/Payments/Filter"
            params = dict()
            data = None
            params["contractorCode"] = contractorCode
            if dateFrom is not None and not isinstance(dateFrom, Unset):
                params["dateFrom"] = dateFrom
            if dateTo is not None and not isinstance(dateTo, Unset):
                params["dateTo"] = dateTo
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[PaymentListElement])
            return result
        case Unset(), int(), datetime() | None | Unset(), datetime() | None | Unset():
            path = "/api/Payments/Filter"
            params = dict()
            data = None
            params["contractorId"] = contractorId
            if dateFrom is not None and not isinstance(dateFrom, Unset):
                params["dateFrom"] = dateFrom
            if dateTo is not None and not isinstance(dateTo, Unset):
                params["dateTo"] = dateTo
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[PaymentListElement])
            return result


async def GetListByPaymentRegistry(
    api: AsyncAPI,
    dateFrom: Optional[datetime] = Unset(),
    dateTo: Optional[datetime] = Unset(),
    paymentRegistryCode: str = Unset(),
    paymentRegistryId: int = Unset()
) -> IHttpActionResult[List[PaymentListElement]]:
    match dateFrom, dateTo, paymentRegistryCode, paymentRegistryId:
        case datetime() | None | Unset(), datetime() | None | Unset(), str(), Unset():
            path = "/api/Payments/Filter"
            params = dict()
            data = None
            if dateFrom is not None and not isinstance(dateFrom, Unset):
                params["dateFrom"] = dateFrom
            if dateTo is not None and not isinstance(dateTo, Unset):
                params["dateTo"] = dateTo
            params["paymentRegistryCode"] = paymentRegistryCode
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[PaymentListElement])
            return result
        case datetime() | None | Unset(), datetime() | None | Unset(), Unset(), int():
            path = "/api/Payments/Filter"
            params = dict()
            data = None
            if dateFrom is not None and not isinstance(dateFrom, Unset):
                params["dateFrom"] = dateFrom
            if dateTo is not None and not isinstance(dateTo, Unset):
                params["dateTo"] = dateTo
            params["paymentRegistryId"] = paymentRegistryId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[PaymentListElement])
            return result


async def GetListByReceivingPaymentRegistry(
    api: AsyncAPI,
    dateFrom: Optional[datetime] = Unset(),
    dateTo: Optional[datetime] = Unset(),
    receivingPaymentRegistryCode: str = Unset(),
    receivingPaymentRegistryId: int = Unset()
) -> IHttpActionResult[List[PaymentListElement]]:
    match dateFrom, dateTo, receivingPaymentRegistryCode, receivingPaymentRegistryId:
        case datetime() | None | Unset(), datetime() | None | Unset(), Unset(), int():
            path = "/api/Payments/Filter"
            params = dict()
            data = None
            if dateFrom is not None and not isinstance(dateFrom, Unset):
                params["dateFrom"] = dateFrom
            if dateTo is not None and not isinstance(dateTo, Unset):
                params["dateTo"] = dateTo
            params["receivingPaymentRegistryId"] = receivingPaymentRegistryId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[PaymentListElement])
            return result
        case datetime() | None | Unset(), datetime() | None | Unset(), str(), Unset():
            path = "/api/Payments/Filter"
            params = dict()
            data = None
            if dateFrom is not None and not isinstance(dateFrom, Unset):
                params["dateFrom"] = dateFrom
            if dateTo is not None and not isinstance(dateTo, Unset):
                params["dateTo"] = dateTo
            params["receivingPaymentRegistryCode"] = receivingPaymentRegistryCode
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[PaymentListElement])
            return result


async def GetNALDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Payments/NALDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetPDF(
    api: AsyncAPI,
    buffer: bool = Unset(),
    documentId: int = Unset(),
    documentNumber: str = Unset(),
    printNote: bool = Unset()
) -> IHttpActionResult[PDF]:
    match buffer, documentId, documentNumber, printNote:
        case Unset(), int(), Unset(), bool():
            path = "/api/Payments/PDF"
            params = dict()
            data = None
            params["documentId"] = documentId
            params["printNote"] = printNote
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, PDF)
            return result
        case bool(), Unset(), str(), bool():
            path = "/api/Payments/PDF"
            params = dict()
            data = None
            params["buffer"] = buffer
            params["documentNumber"] = documentNumber
            params["printNote"] = printNote
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, PDF)
            return result


async def GetPagedDocument(
    api: AsyncAPI, orderBy: enumOrderByType, page: int, size: int
) -> IHttpActionResult[Page[PaymentListElement]]:
    """
    ['Page[PaymentListElement]']
    :param api:
    :type api: AsyncAPI
    :param orderBy:
    :type orderBy: enumOrderByType
    :param page:
    :type page: int
    :param size:
    :type size: int
    :returns: Page[PaymentListElement]
    :rtype: Page[PaymentListElement]
    """
    path = "/api/Payments/Page"
    params = dict()
    data = None
    params["orderBy"] = orderBy

    params["page"] = page

    params["size"] = size

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, Page[PaymentListElement])
    return result


async def GetTRMinusDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Payments/TRMinusDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetTRPlusDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Payments/TRPlusDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetZOBDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Payments/ZOBDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def IssuePayment(
    api: AsyncAPI, payment: PaymentIssue
) -> IHttpActionResult[Payment]:
    """
    ['Payment']
    :param api:
    :type api: AsyncAPI
    :param payment:
    :type payment: PaymentIssue
    :returns: Payment
    :rtype: Payment
    """
    path = "/api/Payments/Payment"
    params = dict()
    data = payment.model_dump_json(exclude_unset=True)
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="POST", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, Payment)
    return result


async def IssueTransferMinus(
    api: AsyncAPI, payment: PaymentIssue
) -> IHttpActionResult[Payment]:
    """
    ['Payment']
    :param api:
    :type api: AsyncAPI
    :param payment:
    :type payment: PaymentIssue
    :returns: Payment
    :rtype: Payment
    """
    path = "/api/Payments/TransferMinus"
    params = dict()
    data = payment.model_dump_json(exclude_unset=True)
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="POST", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, Payment)
    return result


async def IssueTransferPlus(
    api: AsyncAPI,
    paymentId: int = Unset(),
    paymentNumber: str = Unset()
) -> IHttpActionResult[Payment]:
    match paymentId, paymentNumber:
        case int(), Unset():
            path = "/api/Payments/TransferPlus"
            params = dict()
            data = None
            params["paymentId"] = paymentId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, Payment)
            return result
        case Unset(), str():
            path = "/api/Payments/TransferPlus"
            params = dict()
            data = None
            params["paymentNumber"] = paymentNumber
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, Payment)
            return result
