from .....Client import (
    AsyncAPI,
    ClientResponse,
    IHttpActionResult,
)
from .....Constants import (
    Unset,
)
from ....Common.ViewModels import (
    Catalog,
    DocumentSeries,
    DocumentType,
    Kind,
    Marker,
    PDF,
    PDFSettings,
)
from ....Enums import (
    enumOrderByType,
)
from ....ViewModels import (
    Page,
)
from ...ViewModels import (
    SaleCorrection,
    SaleDocument,
    SaleDocumentCorrection,
    SaleDocumentListElement,
    SaleDocumentStatus,
    SaleDocumentWZ,
    SaleDocumentZMO,
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


Get_T = TypeVar('Get_T', IHttpActionResult[SaleDocument], IHttpActionResult[List[SaleDocumentListElement]])


@overload
async def Get(
    api: AsyncAPI, id: int
) -> IHttpActionResult[SaleDocument]: ...


@overload
async def Get(
    api: AsyncAPI, 
) -> IHttpActionResult[List[SaleDocumentListElement]]: ...


@overload
async def Get(
    api: AsyncAPI, buffer: bool, number: str
) -> IHttpActionResult[SaleDocument]: ...


async def Get(
    api: AsyncAPI,
    buffer: bool = Unset(),
    id: int = Unset(),
    number: str = Unset()
) -> Get_T:
    match buffer, id, number:
        case Unset(), int(), Unset():
            path = "/api/Sales"
            params = dict()
            data = None
            params["id"] = id
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, SaleDocument)
            return result
        case Unset(), Unset(), Unset():
            path = "/api/Sales"
            params = dict()
            data = None
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[SaleDocumentListElement])
            return result
        case bool(), Unset(), str():
            path = "/api/Sales"
            params = dict()
            data = None
            params["buffer"] = buffer
            params["number"] = number
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, SaleDocument)
            return result


async def GetCatalogs(
    api: AsyncAPI, 
) -> IHttpActionResult[List[Catalog]]:
    """
    ['List[Catalog]']
    :param api:
    :type api: AsyncAPI
    :returns: List[Catalog]
    :rtype: List[Catalog]
    """
    path = "/api/Sales/Catalogs"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[Catalog])
    return result


async def GetCorrection(
    api: AsyncAPI,
    buffer: bool = Unset(),
    id: int = Unset(),
    number: str = Unset()
) -> IHttpActionResult[SaleCorrection]:
    match buffer, id, number:
        case bool(), Unset(), str():
            path = "/api/Sales/Correction"
            params = dict()
            data = None
            params["buffer"] = buffer
            params["number"] = number
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, SaleCorrection)
            return result
        case Unset(), int(), Unset():
            path = "/api/Sales/Correction"
            params = dict()
            data = None
            params["id"] = id
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, SaleCorrection)
            return result


async def GetCorrectionSequence(
    api: AsyncAPI,
    buffer: bool = Unset(),
    documentId: int = Unset(),
    documentNumber: str = Unset()
) -> IHttpActionResult[List[SaleDocumentCorrection]]:
    match buffer, documentId, documentNumber:
        case Unset(), int(), Unset():
            path = "/api/Sales/CorrectionSequence"
            params = dict()
            data = None
            params["documentId"] = documentId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[SaleDocumentCorrection])
            return result
        case bool(), Unset(), str():
            path = "/api/Sales/CorrectionSequence"
            params = dict()
            data = None
            params["buffer"] = buffer
            params["documentNumber"] = documentNumber
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[SaleDocumentCorrection])
            return result


async def GetDEXDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Sales/DEXDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetDXKDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Sales/DXKDocumentTypes"
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
    path = "/api/Sales/DocumentSeries"
    params = dict()
    data = None
    params["documentTypeId"] = documentTypeId

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentSeries])
    return result


async def GetFKSDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Sales/FKSDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetFKWDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Sales/FKWDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetFVMKDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Sales/FVMKDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetFVSDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Sales/FVSDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetFVSMDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Sales/FVSMDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetFVWDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Sales/FVWDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetKinds(
    api: AsyncAPI, 
) -> IHttpActionResult[List[Kind]]:
    """
    ['List[Kind]']
    :param api:
    :type api: AsyncAPI
    :returns: List[Kind]
    :rtype: List[Kind]
    """
    path = "/api/Sales/Kinds"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[Kind])
    return result


async def GetList(
    api: AsyncAPI, dateFrom: Optional[datetime], dateTo: Optional[datetime]
) -> IHttpActionResult[List[SaleDocumentListElement]]:
    """
    ['List[SaleDocumentListElement]']
    :param api:
    :type api: AsyncAPI
    :param dateFrom:
    :type dateFrom: datetime | None
    :param dateTo:
    :type dateTo: datetime | None
    :returns: List[SaleDocumentListElement]
    :rtype: List[SaleDocumentListElement]
    """
    path = "/api/Sales/Filter"
    params = dict()
    data = None
    if dateFrom is not None:
        params["dateFrom"] = dateFrom

    if dateTo is not None:
        params["dateTo"] = dateTo

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[SaleDocumentListElement])
    return result


async def GetListByBuyer(
    api: AsyncAPI,
    buyerCode: str = Unset(),
    buyerId: int = Unset(),
    dateFrom: Optional[datetime] = Unset(),
    dateTo: Optional[datetime] = Unset()
) -> IHttpActionResult[List[SaleDocumentListElement]]:
    match buyerCode, buyerId, dateFrom, dateTo:
        case str(), Unset(), datetime() | None | Unset(), datetime() | None | Unset():
            path = "/api/Sales/Filter"
            params = dict()
            data = None
            params["buyerCode"] = buyerCode
            if dateFrom is not None and not isinstance(dateFrom, Unset):
                params["dateFrom"] = dateFrom
            if dateTo is not None and not isinstance(dateTo, Unset):
                params["dateTo"] = dateTo
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[SaleDocumentListElement])
            return result
        case Unset(), int(), datetime() | None | Unset(), datetime() | None | Unset():
            path = "/api/Sales/Filter"
            params = dict()
            data = None
            params["buyerId"] = buyerId
            if dateFrom is not None and not isinstance(dateFrom, Unset):
                params["dateFrom"] = dateFrom
            if dateTo is not None and not isinstance(dateTo, Unset):
                params["dateTo"] = dateTo
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[SaleDocumentListElement])
            return result


async def GetListByDimension(
    api: AsyncAPI, dictionaryValue: str, dimensionCode: str, value: str
) -> IHttpActionResult[List[SaleDocumentListElement]]:
    """
    ['List[SaleDocumentListElement]']
    :param api:
    :type api: AsyncAPI
    :param dictionaryValue:
    :type dictionaryValue: str
    :param dimensionCode:
    :type dimensionCode: str
    :param value:
    :type value: str
    :returns: List[SaleDocumentListElement]
    :rtype: List[SaleDocumentListElement]
    """
    path = "/api/Sales/Filter"
    params = dict()
    data = None
    params["dictionaryValue"] = dictionaryValue

    params["dimensionCode"] = dimensionCode

    params["value"] = value

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[SaleDocumentListElement])
    return result


async def GetListByRecipient(
    api: AsyncAPI,
    dateFrom: Optional[datetime] = Unset(),
    dateTo: Optional[datetime] = Unset(),
    recipientCode: str = Unset(),
    recipientId: int = Unset()
) -> IHttpActionResult[List[SaleDocumentListElement]]:
    match dateFrom, dateTo, recipientCode, recipientId:
        case datetime() | None | Unset(), datetime() | None | Unset(), str(), Unset():
            path = "/api/Sales/Filter"
            params = dict()
            data = None
            if dateFrom is not None and not isinstance(dateFrom, Unset):
                params["dateFrom"] = dateFrom
            if dateTo is not None and not isinstance(dateTo, Unset):
                params["dateTo"] = dateTo
            params["recipientCode"] = recipientCode
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[SaleDocumentListElement])
            return result
        case datetime() | None | Unset(), datetime() | None | Unset(), Unset(), int():
            path = "/api/Sales/Filter"
            params = dict()
            data = None
            if dateFrom is not None and not isinstance(dateFrom, Unset):
                params["dateFrom"] = dateFrom
            if dateTo is not None and not isinstance(dateTo, Unset):
                params["dateTo"] = dateTo
            params["recipientId"] = recipientId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[SaleDocumentListElement])
            return result


async def GetMarkers(
    api: AsyncAPI, 
) -> IHttpActionResult[List[Marker]]:
    """
    ['List[Marker]']
    :param api:
    :type api: AsyncAPI
    :returns: List[Marker]
    :rtype: List[Marker]
    """
    path = "/api/Sales/Markers"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[Marker])
    return result


async def GetPARDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Sales/PARDocumentTypes"
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
    printNote: bool = Unset(),
    settings: PDFSettings = Unset()
) -> IHttpActionResult[PDF]:
    match buffer, documentId, documentNumber, printNote, settings:
        case bool(), Unset(), str(), bool(), Unset():
            path = "/api/Sales/PDF"
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
        case Unset(), int(), Unset(), Unset(), PDFSettings():
            path = "/api/Sales/PDF"
            params = dict()
            params["documentId"] = documentId
            data = settings.model_dump_json(exclude_unset=True)
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PATCH", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, PDF)
            return result
        case Unset(), int(), Unset(), bool(), Unset():
            path = "/api/Sales/PDF"
            params = dict()
            data = None
            params["documentId"] = documentId
            params["printNote"] = printNote
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, PDF)
            return result
        case bool(), Unset(), str(), Unset(), PDFSettings():
            path = "/api/Sales/PDF"
            params = dict()
            params["buffer"] = buffer
            params["documentNumber"] = documentNumber
            data = settings.model_dump_json(exclude_unset=True)
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PATCH", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, PDF)
            return result


async def GetPRKDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Sales/PRKDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetPagedDocument(
    api: AsyncAPI, orderBy: enumOrderByType, page: int, size: int
) -> IHttpActionResult[Page[SaleDocumentListElement]]:
    """
    ['Page[SaleDocumentListElement]']
    :param api:
    :type api: AsyncAPI
    :param orderBy:
    :type orderBy: enumOrderByType
    :param page:
    :type page: int
    :param size:
    :type size: int
    :returns: Page[SaleDocumentListElement]
    :rtype: Page[SaleDocumentListElement]
    """
    path = "/api/Sales/Page"
    params = dict()
    data = None
    params["orderBy"] = orderBy

    params["page"] = page

    params["size"] = size

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, Page[SaleDocumentListElement])
    return result


async def GetREXDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Sales/REXDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetRKSDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Sales/RKSDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetRUSDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Sales/RUSDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetRXKDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Sales/RXKDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetSKKDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Sales/SKKDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetSKODocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Sales/SKODocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetSKWDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Sales/SKWDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetSKWKDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Sales/SKWKDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetSRKDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Sales/SRKDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetSRSDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Sales/SRSDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetStatus(
    api: AsyncAPI,
    buffer: bool = Unset(),
    documentId: int = Unset(),
    documentNumber: str = Unset()
) -> IHttpActionResult[SaleDocumentStatus]:
    match buffer, documentId, documentNumber:
        case bool(), Unset(), str():
            path = "/api/Sales/Status"
            params = dict()
            data = None
            params["buffer"] = buffer
            params["documentNumber"] = documentNumber
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, SaleDocumentStatus)
            return result
        case Unset(), int(), Unset():
            path = "/api/Sales/Status"
            params = dict()
            data = None
            params["documentId"] = documentId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, SaleDocumentStatus)
            return result


async def GetWDTDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Sales/WDTDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetWDTKDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Sales/WDTKDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetWKSDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Sales/WKSDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetWZ(
    api: AsyncAPI,
    buffer: bool = Unset(),
    documentId: int = Unset(),
    documentNumber: str = Unset()
) -> IHttpActionResult[List[SaleDocumentWZ]]:
    match buffer, documentId, documentNumber:
        case bool(), Unset(), str():
            path = "/api/Sales/WZ"
            params = dict()
            data = None
            params["buffer"] = buffer
            params["documentNumber"] = documentNumber
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[SaleDocumentWZ])
            return result
        case Unset(), int(), Unset():
            path = "/api/Sales/WZ"
            params = dict()
            data = None
            params["documentId"] = documentId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[SaleDocumentWZ])
            return result


async def GetZMO(
    api: AsyncAPI,
    buffer: bool = Unset(),
    documentId: int = Unset(),
    documentNumber: str = Unset()
) -> IHttpActionResult[List[SaleDocumentZMO]]:
    match buffer, documentId, documentNumber:
        case Unset(), int(), Unset():
            path = "/api/Sales/ZMO"
            params = dict()
            data = None
            params["documentId"] = documentId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[SaleDocumentZMO])
            return result
        case bool(), Unset(), str():
            path = "/api/Sales/ZMO"
            params = dict()
            data = None
            params["buffer"] = buffer
            params["documentNumber"] = documentNumber
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[SaleDocumentZMO])
            return result


async def IncrementalSync(
    api: AsyncAPI, dateFrom: datetime
) -> IHttpActionResult[None]:
    """
    []
    :param api:
    :type api: AsyncAPI
    :param dateFrom:
    :type dateFrom: datetime
    :returns: 
    :rtype: 
    """
    path = "/api/Sales/IncrementalSync"
    params = dict()
    data = None
    params["dateFrom"] = dateFrom

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    # no return
    result = await IHttpActionResult.create(response, None)
    return result
