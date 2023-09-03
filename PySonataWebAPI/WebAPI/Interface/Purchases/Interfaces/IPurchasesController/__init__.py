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
    PurchaseCorrection,
    PurchaseDocument,
    PurchaseDocumentCorrection,
    PurchaseDocumentListElement,
    PurchaseDocumentStatus,
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


Get_T = TypeVar('Get_T', IHttpActionResult[PurchaseDocument], IHttpActionResult[List[PurchaseDocumentListElement]])


@overload
async def Get(
    api: AsyncAPI, buffer: bool, number: str
) -> IHttpActionResult[PurchaseDocument]: ...


@overload
async def Get(
    api: AsyncAPI, id: int
) -> IHttpActionResult[PurchaseDocument]: ...


@overload
async def Get(
    api: AsyncAPI, 
) -> IHttpActionResult[List[PurchaseDocumentListElement]]: ...


async def Get(
    api: AsyncAPI,
    buffer: bool = Unset(),
    id: int = Unset(),
    number: str = Unset()
) -> Get_T:
    match buffer, id, number:
        case bool(), Unset(), str():
            path = "/api/Purchases"
            params = dict()
            data = None
            params["buffer"] = buffer
            params["number"] = number
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, PurchaseDocument)
            return result
        case Unset(), int(), Unset():
            path = "/api/Purchases"
            params = dict()
            data = None
            params["id"] = id
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, PurchaseDocument)
            return result
        case Unset(), Unset(), Unset():
            path = "/api/Purchases"
            params = dict()
            data = None
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[PurchaseDocumentListElement])
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
    path = "/api/Purchases/Catalogs"
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
) -> IHttpActionResult[PurchaseCorrection]:
    match buffer, id, number:
        case Unset(), int(), Unset():
            path = "/api/Purchases/Correction"
            params = dict()
            data = None
            params["id"] = id
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, PurchaseCorrection)
            return result
        case bool(), Unset(), str():
            path = "/api/Purchases/Correction"
            params = dict()
            data = None
            params["buffer"] = buffer
            params["number"] = number
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, PurchaseCorrection)
            return result


async def GetCorrectionSequence(
    api: AsyncAPI,
    buffer: bool = Unset(),
    documentId: int = Unset(),
    documentNumber: str = Unset()
) -> IHttpActionResult[List[PurchaseDocumentCorrection]]:
    match buffer, documentId, documentNumber:
        case bool(), Unset(), str():
            path = "/api/Purchases/CorrectionSequence"
            params = dict()
            data = None
            params["buffer"] = buffer
            params["documentNumber"] = documentNumber
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[PurchaseDocumentCorrection])
            return result
        case Unset(), int(), Unset():
            path = "/api/Purchases/CorrectionSequence"
            params = dict()
            data = None
            params["documentId"] = documentId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[PurchaseDocumentCorrection])
            return result


async def GetDIMDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Purchases/DIMDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetDMKDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Purchases/DMKDocumentTypes"
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
    path = "/api/Purchases/DocumentSeries"
    params = dict()
    data = None
    params["documentTypeId"] = documentTypeId

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentSeries])
    return result


async def GetFMKDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Purchases/FMKDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetFRKDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Purchases/FRKDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetFVMDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Purchases/FVMDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetFVRDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Purchases/FVRDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetFVZDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Purchases/FVZDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetFWZDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Purchases/FWZDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetFWZKDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Purchases/FWZKDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetFZKDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Purchases/FZKDocumentTypes"
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
    path = "/api/Purchases/Kinds"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[Kind])
    return result


async def GetList(
    api: AsyncAPI, dateFrom: Optional[datetime], dateTo: Optional[datetime]
) -> IHttpActionResult[List[PurchaseDocumentListElement]]:
    """
    ['List[PurchaseDocumentListElement]']
    :param api:
    :type api: AsyncAPI
    :param dateFrom:
    :type dateFrom: datetime | None
    :param dateTo:
    :type dateTo: datetime | None
    :returns: List[PurchaseDocumentListElement]
    :rtype: List[PurchaseDocumentListElement]
    """
    path = "/api/Purchases/Filter"
    params = dict()
    data = None
    if dateFrom is not None:
        params["dateFrom"] = dateFrom

    if dateTo is not None:
        params["dateTo"] = dateTo

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[PurchaseDocumentListElement])
    return result


async def GetListByDeliverer(
    api: AsyncAPI,
    dateFrom: Optional[datetime] = Unset(),
    dateTo: Optional[datetime] = Unset(),
    delivererCode: str = Unset(),
    delivererId: int = Unset()
) -> IHttpActionResult[List[PurchaseDocumentListElement]]:
    match dateFrom, dateTo, delivererCode, delivererId:
        case datetime() | None | Unset(), datetime() | None | Unset(), str(), Unset():
            path = "/api/Purchases/Filter"
            params = dict()
            data = None
            if dateFrom is not None and not isinstance(dateFrom, Unset):
                params["dateFrom"] = dateFrom
            if dateTo is not None and not isinstance(dateTo, Unset):
                params["dateTo"] = dateTo
            params["delivererCode"] = delivererCode
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[PurchaseDocumentListElement])
            return result
        case datetime() | None | Unset(), datetime() | None | Unset(), Unset(), int():
            path = "/api/Purchases/Filter"
            params = dict()
            data = None
            if dateFrom is not None and not isinstance(dateFrom, Unset):
                params["dateFrom"] = dateFrom
            if dateTo is not None and not isinstance(dateTo, Unset):
                params["dateTo"] = dateTo
            params["delivererId"] = delivererId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[PurchaseDocumentListElement])
            return result


async def GetListByDimension(
    api: AsyncAPI, dictionaryValue: str, dimensionCode: str, value: str
) -> IHttpActionResult[List[PurchaseDocumentListElement]]:
    """
    ['List[PurchaseDocumentListElement]']
    :param api:
    :type api: AsyncAPI
    :param dictionaryValue:
    :type dictionaryValue: str
    :param dimensionCode:
    :type dimensionCode: str
    :param value:
    :type value: str
    :returns: List[PurchaseDocumentListElement]
    :rtype: List[PurchaseDocumentListElement]
    """
    path = "/api/Purchases/Filter"
    params = dict()
    data = None
    params["dictionaryValue"] = dictionaryValue

    params["dimensionCode"] = dimensionCode

    params["value"] = value

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[PurchaseDocumentListElement])
    return result


async def GetListBySeller(
    api: AsyncAPI,
    dateFrom: Optional[datetime] = Unset(),
    dateTo: Optional[datetime] = Unset(),
    sellerCode: str = Unset(),
    sellerId: int = Unset()
) -> IHttpActionResult[List[PurchaseDocumentListElement]]:
    match dateFrom, dateTo, sellerCode, sellerId:
        case datetime() | None | Unset(), datetime() | None | Unset(), str(), Unset():
            path = "/api/Purchases/Filter"
            params = dict()
            data = None
            if dateFrom is not None and not isinstance(dateFrom, Unset):
                params["dateFrom"] = dateFrom
            if dateTo is not None and not isinstance(dateTo, Unset):
                params["dateTo"] = dateTo
            params["sellerCode"] = sellerCode
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[PurchaseDocumentListElement])
            return result
        case datetime() | None | Unset(), datetime() | None | Unset(), Unset(), int():
            path = "/api/Purchases/Filter"
            params = dict()
            data = None
            if dateFrom is not None and not isinstance(dateFrom, Unset):
                params["dateFrom"] = dateFrom
            if dateTo is not None and not isinstance(dateTo, Unset):
                params["dateTo"] = dateTo
            params["sellerId"] = sellerId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[PurchaseDocumentListElement])
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
    path = "/api/Purchases/Markers"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[Marker])
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
        case Unset(), int(), Unset(), bool(), Unset():
            path = "/api/Purchases/PDF"
            params = dict()
            data = None
            params["documentId"] = documentId
            params["printNote"] = printNote
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, PDF)
            return result
        case bool(), Unset(), str(), bool(), Unset():
            path = "/api/Purchases/PDF"
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
            path = "/api/Purchases/PDF"
            params = dict()
            params["documentId"] = documentId
            data = settings.model_dump_json(exclude_unset=True)
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PATCH", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, PDF)
            return result
        case bool(), Unset(), str(), Unset(), PDFSettings():
            path = "/api/Purchases/PDF"
            params = dict()
            params["buffer"] = buffer
            params["documentNumber"] = documentNumber
            data = settings.model_dump_json(exclude_unset=True)
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PATCH", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, PDF)
            return result


async def GetPZ(
    api: AsyncAPI,
    buffer: bool = Unset(),
    documentId: int = Unset(),
    documentNumber: str = Unset()
) -> IHttpActionResult[None]:
    match buffer, documentId, documentNumber:
        case bool(), Unset(), str():
            path = "/api/Purchases/PZ"
            params = dict()
            data = None
            params["buffer"] = buffer
            params["documentNumber"] = documentNumber
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result
        case Unset(), int(), Unset():
            path = "/api/Purchases/PZ"
            params = dict()
            data = None
            params["documentId"] = documentId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result


async def GetPagedDocument(
    api: AsyncAPI, orderBy: enumOrderByType, page: int, size: int
) -> IHttpActionResult[Page[PurchaseDocumentListElement]]:
    """
    ['Page[PurchaseDocumentListElement]']
    :param api:
    :type api: AsyncAPI
    :param orderBy:
    :type orderBy: enumOrderByType
    :param page:
    :type page: int
    :param size:
    :type size: int
    :returns: Page[PurchaseDocumentListElement]
    :rtype: Page[PurchaseDocumentListElement]
    """
    path = "/api/Purchases/Page"
    params = dict()
    data = None
    params["orderBy"] = orderBy

    params["page"] = page

    params["size"] = size

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, Page[PurchaseDocumentListElement])
    return result


async def GetRKZDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Purchases/RKZDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetRUZDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Purchases/RUZDocumentTypes"
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
) -> IHttpActionResult[PurchaseDocumentStatus]:
    match buffer, documentId, documentNumber:
        case Unset(), int(), Unset():
            path = "/api/Purchases/Status"
            params = dict()
            data = None
            params["documentId"] = documentId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, PurchaseDocumentStatus)
            return result
        case bool(), Unset(), str():
            path = "/api/Purchases/Status"
            params = dict()
            data = None
            params["buffer"] = buffer
            params["documentNumber"] = documentNumber
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, PurchaseDocumentStatus)
            return result


async def GetWNKDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Purchases/WNKDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetWNTDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Purchases/WNTDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetZMW(
    api: AsyncAPI,
    buffer: bool = Unset(),
    documentId: int = Unset(),
    documentNumber: str = Unset()
) -> IHttpActionResult[None]:
    match buffer, documentId, documentNumber:
        case Unset(), int(), Unset():
            path = "/api/Purchases/ZMW"
            params = dict()
            data = None
            params["documentId"] = documentId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result
        case bool(), Unset(), str():
            path = "/api/Purchases/ZMW"
            params = dict()
            data = None
            params["buffer"] = buffer
            params["documentNumber"] = documentNumber
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result


async def GetZRKDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Purchases/ZRKDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetZRZDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Purchases/ZRZDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result
