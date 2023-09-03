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
    WarehouseDocument,
    WarehouseDocumentFV,
    WarehouseDocumentListElement,
    WarehouseDocumentStatus,
    WarehouseRegistry,
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


Get_T = TypeVar('Get_T', IHttpActionResult[WarehouseDocument], IHttpActionResult[List[WarehouseDocumentListElement]])


@overload
async def Get(
    api: AsyncAPI, buffer: bool, number: str
) -> IHttpActionResult[WarehouseDocument]: ...


@overload
async def Get(
    api: AsyncAPI, id: int
) -> IHttpActionResult[WarehouseDocument]: ...


@overload
async def Get(
    api: AsyncAPI, 
) -> IHttpActionResult[List[WarehouseDocumentListElement]]: ...


async def Get(
    api: AsyncAPI,
    buffer: bool = Unset(),
    id: int = Unset(),
    number: str = Unset()
) -> Get_T:
    match buffer, id, number:
        case bool(), Unset(), str():
            path = "/api/WarehouseDocuments"
            params = dict()
            data = None
            params["buffer"] = buffer
            params["number"] = number
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, WarehouseDocument)
            return result
        case Unset(), int(), Unset():
            path = "/api/WarehouseDocuments"
            params = dict()
            data = None
            params["id"] = id
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, WarehouseDocument)
            return result
        case Unset(), Unset(), Unset():
            path = "/api/WarehouseDocuments"
            params = dict()
            data = None
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[WarehouseDocumentListElement])
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
    path = "/api/WarehouseDocuments/Catalogs"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[Catalog])
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
    path = "/api/WarehouseDocuments/DocumentSeries"
    params = dict()
    data = None
    params["documentTypeId"] = documentTypeId

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentSeries])
    return result


async def GetFV(
    api: AsyncAPI,
    buffer: bool = Unset(),
    documentId: int = Unset(),
    documentNumber: str = Unset()
) -> IHttpActionResult[List[WarehouseDocumentFV]]:
    match buffer, documentId, documentNumber:
        case bool(), Unset(), str():
            path = "/api/WarehouseDocuments/FV"
            params = dict()
            data = None
            params["buffer"] = buffer
            params["documentNumber"] = documentNumber
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[WarehouseDocumentFV])
            return result
        case Unset(), int(), Unset():
            path = "/api/WarehouseDocuments/FV"
            params = dict()
            data = None
            params["documentId"] = documentId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[WarehouseDocumentFV])
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
    path = "/api/WarehouseDocuments/Kinds"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[Kind])
    return result


async def GetList(
    api: AsyncAPI, dateFrom: Optional[datetime], dateTo: Optional[datetime]
) -> IHttpActionResult[List[WarehouseDocumentListElement]]:
    """
    ['List[WarehouseDocumentListElement]']
    :param api:
    :type api: AsyncAPI
    :param dateFrom:
    :type dateFrom: datetime | None
    :param dateTo:
    :type dateTo: datetime | None
    :returns: List[WarehouseDocumentListElement]
    :rtype: List[WarehouseDocumentListElement]
    """
    path = "/api/WarehouseDocuments/Filter"
    params = dict()
    data = None
    if dateFrom is not None:
        params["dateFrom"] = dateFrom

    if dateTo is not None:
        params["dateTo"] = dateTo

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[WarehouseDocumentListElement])
    return result


async def GetListByContractor(
    api: AsyncAPI,
    contractorCode: str = Unset(),
    contractorId: int = Unset(),
    dateFrom: Optional[datetime] = Unset(),
    dateTo: Optional[datetime] = Unset()
) -> IHttpActionResult[List[WarehouseDocumentListElement]]:
    match contractorCode, contractorId, dateFrom, dateTo:
        case str(), Unset(), datetime() | None | Unset(), datetime() | None | Unset():
            path = "/api/WarehouseDocuments/Filter"
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
            result = await IHttpActionResult.create(response, List[WarehouseDocumentListElement])
            return result
        case Unset(), int(), datetime() | None | Unset(), datetime() | None | Unset():
            path = "/api/WarehouseDocuments/Filter"
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
            result = await IHttpActionResult.create(response, List[WarehouseDocumentListElement])
            return result


async def GetListByDimension(
    api: AsyncAPI, dictionaryValue: str, dimensionCode: str, value: str
) -> IHttpActionResult[List[WarehouseDocumentListElement]]:
    """
    ['List[WarehouseDocumentListElement]']
    :param api:
    :type api: AsyncAPI
    :param dictionaryValue:
    :type dictionaryValue: str
    :param dimensionCode:
    :type dimensionCode: str
    :param value:
    :type value: str
    :returns: List[WarehouseDocumentListElement]
    :rtype: List[WarehouseDocumentListElement]
    """
    path = "/api/WarehouseDocuments/Filter"
    params = dict()
    data = None
    params["dictionaryValue"] = dictionaryValue

    params["dimensionCode"] = dimensionCode

    params["value"] = value

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[WarehouseDocumentListElement])
    return result


async def GetListByWarehouse(
    api: AsyncAPI,
    dateFrom: Optional[datetime] = Unset(),
    dateTo: Optional[datetime] = Unset(),
    warehouseCode: str = Unset(),
    warehouseId: int = Unset()
) -> IHttpActionResult[List[WarehouseDocumentListElement]]:
    match dateFrom, dateTo, warehouseCode, warehouseId:
        case datetime() | None | Unset(), datetime() | None | Unset(), str(), Unset():
            path = "/api/WarehouseDocuments/Filter"
            params = dict()
            data = None
            if dateFrom is not None and not isinstance(dateFrom, Unset):
                params["dateFrom"] = dateFrom
            if dateTo is not None and not isinstance(dateTo, Unset):
                params["dateTo"] = dateTo
            params["warehouseCode"] = warehouseCode
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[WarehouseDocumentListElement])
            return result
        case datetime() | None | Unset(), datetime() | None | Unset(), Unset(), int():
            path = "/api/WarehouseDocuments/Filter"
            params = dict()
            data = None
            if dateFrom is not None and not isinstance(dateFrom, Unset):
                params["dateFrom"] = dateFrom
            if dateTo is not None and not isinstance(dateTo, Unset):
                params["dateTo"] = dateTo
            params["warehouseId"] = warehouseId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[WarehouseDocumentListElement])
            return result


async def GetMMMinusDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/WarehouseDocuments/MMMinusDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
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
    path = "/api/WarehouseDocuments/Markers"
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
        case Unset(), int(), Unset(), Unset(), PDFSettings():
            path = "/api/WarehouseDocuments/PDF"
            params = dict()
            params["documentId"] = documentId
            data = settings.model_dump_json(exclude_unset=True)
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PATCH", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, PDF)
            return result
        case bool(), Unset(), str(), Unset(), PDFSettings():
            path = "/api/WarehouseDocuments/PDF"
            params = dict()
            params["buffer"] = buffer
            params["documentNumber"] = documentNumber
            data = settings.model_dump_json(exclude_unset=True)
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PATCH", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, PDF)
            return result
        case bool(), Unset(), str(), bool(), Unset():
            path = "/api/WarehouseDocuments/PDF"
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
        case Unset(), int(), Unset(), bool(), Unset():
            path = "/api/WarehouseDocuments/PDF"
            params = dict()
            data = None
            params["documentId"] = documentId
            params["printNote"] = printNote
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, PDF)
            return result


async def GetPWDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/WarehouseDocuments/PWDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetPZODocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/WarehouseDocuments/PZDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetPagedDocument(
    api: AsyncAPI, orderBy: enumOrderByType, page: int, size: int
) -> IHttpActionResult[Page[WarehouseDocumentListElement]]:
    """
    ['Page[WarehouseDocumentListElement]']
    :param api:
    :type api: AsyncAPI
    :param orderBy:
    :type orderBy: enumOrderByType
    :param page:
    :type page: int
    :param size:
    :type size: int
    :returns: Page[WarehouseDocumentListElement]
    :rtype: Page[WarehouseDocumentListElement]
    """
    path = "/api/WarehouseDocuments/Page"
    params = dict()
    data = None
    params["orderBy"] = orderBy

    params["page"] = page

    params["size"] = size

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, Page[WarehouseDocumentListElement])
    return result


async def GetRWDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/WarehouseDocuments/RWDocumentTypes"
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
) -> IHttpActionResult[WarehouseDocumentStatus]:
    match buffer, documentId, documentNumber:
        case bool(), Unset(), str():
            path = "/api/WarehouseDocuments/Status"
            params = dict()
            data = None
            params["buffer"] = buffer
            params["documentNumber"] = documentNumber
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, WarehouseDocumentStatus)
            return result
        case Unset(), int(), Unset():
            path = "/api/WarehouseDocuments/Status"
            params = dict()
            data = None
            params["documentId"] = documentId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, WarehouseDocumentStatus)
            return result


async def GetWZODocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/WarehouseDocuments/WZDocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetWarehouseRegistries(
    api: AsyncAPI, 
) -> IHttpActionResult[List[WarehouseRegistry]]:
    """
    ['List[WarehouseRegistry]']
    :param api:
    :type api: AsyncAPI
    :returns: List[WarehouseRegistry]
    :rtype: List[WarehouseRegistry]
    """
    path = "/api/WarehouseDocuments/WarehouseRegistries"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[WarehouseRegistry])
    return result
