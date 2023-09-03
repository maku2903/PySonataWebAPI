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
    Order,
    OrderFV,
    OrderListElement,
    OrderPositionRelation,
    OrderStatus,
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


Get_T = TypeVar('Get_T', IHttpActionResult[Order], IHttpActionResult[List[OrderListElement]])


@overload
async def Get(
    api: AsyncAPI, 
) -> IHttpActionResult[List[OrderListElement]]: ...


@overload
async def Get(
    api: AsyncAPI, id: int
) -> IHttpActionResult[Order]: ...


@overload
async def Get(
    api: AsyncAPI, buffer: bool, number: str
) -> IHttpActionResult[Order]: ...


async def Get(
    api: AsyncAPI,
    buffer: bool = Unset(),
    id: int = Unset(),
    number: str = Unset()
) -> Get_T:
    match buffer, id, number:
        case Unset(), Unset(), Unset():
            path = "/api/Orders"
            params = dict()
            data = None
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[OrderListElement])
            return result
        case Unset(), int(), Unset():
            path = "/api/Orders"
            params = dict()
            data = None
            params["id"] = id
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, Order)
            return result
        case bool(), Unset(), str():
            path = "/api/Orders"
            params = dict()
            data = None
            params["buffer"] = buffer
            params["number"] = number
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, Order)
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
    path = "/api/Orders/Catalogs"
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
    path = "/api/Orders/DocumentSeries"
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
    orderId: int = Unset(),
    orderNumber: str = Unset()
) -> IHttpActionResult[List[OrderFV]]:
    match buffer, orderId, orderNumber:
        case bool(), Unset(), str():
            path = "/api/Orders/FV"
            params = dict()
            data = None
            params["buffer"] = buffer
            params["orderNumber"] = orderNumber
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[OrderFV])
            return result
        case Unset(), int(), Unset():
            path = "/api/Orders/FV"
            params = dict()
            data = None
            params["orderId"] = orderId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[OrderFV])
            return result


async def GetInvoicesPDF(
    api: AsyncAPI,
    buffer: bool = Unset(),
    orderId: int = Unset(),
    orderNumber: str = Unset(),
    printNote: bool = Unset()
) -> IHttpActionResult[List[PDF]]:
    match buffer, orderId, orderNumber, printNote:
        case bool(), Unset(), str(), bool():
            path = "/api/Orders/InvoicesPDF"
            params = dict()
            data = None
            params["buffer"] = buffer
            params["orderNumber"] = orderNumber
            params["printNote"] = printNote
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[PDF])
            return result
        case Unset(), int(), Unset(), bool():
            path = "/api/Orders/InvoicesPDF"
            params = dict()
            data = None
            params["orderId"] = orderId
            params["printNote"] = printNote
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[PDF])
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
    path = "/api/Orders/Kinds"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[Kind])
    return result


async def GetList(
    api: AsyncAPI, dateFrom: Optional[datetime], dateTo: Optional[datetime]
) -> IHttpActionResult[List[OrderListElement]]:
    """
    ['List[OrderListElement]']
    :param api:
    :type api: AsyncAPI
    :param dateFrom:
    :type dateFrom: datetime | None
    :param dateTo:
    :type dateTo: datetime | None
    :returns: List[OrderListElement]
    :rtype: List[OrderListElement]
    """
    path = "/api/Orders/Filter"
    params = dict()
    data = None
    if dateFrom is not None:
        params["dateFrom"] = dateFrom

    if dateTo is not None:
        params["dateTo"] = dateTo

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[OrderListElement])
    return result


async def GetListByBuyer(
    api: AsyncAPI,
    buyerCode: str = Unset(),
    buyerId: int = Unset(),
    dateFrom: Optional[datetime] = Unset(),
    dateTo: Optional[datetime] = Unset()
) -> IHttpActionResult[List[OrderListElement]]:
    match buyerCode, buyerId, dateFrom, dateTo:
        case Unset(), int(), datetime() | None | Unset(), datetime() | None | Unset():
            path = "/api/Orders/Filter"
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
            result = await IHttpActionResult.create(response, List[OrderListElement])
            return result
        case str(), Unset(), datetime() | None | Unset(), datetime() | None | Unset():
            path = "/api/Orders/Filter"
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
            result = await IHttpActionResult.create(response, List[OrderListElement])
            return result


async def GetListByDimension(
    api: AsyncAPI, dictionaryValue: str, dimensionCode: str, value: str
) -> IHttpActionResult[List[OrderListElement]]:
    """
    ['List[OrderListElement]']
    :param api:
    :type api: AsyncAPI
    :param dictionaryValue:
    :type dictionaryValue: str
    :param dimensionCode:
    :type dimensionCode: str
    :param value:
    :type value: str
    :returns: List[OrderListElement]
    :rtype: List[OrderListElement]
    """
    path = "/api/Orders/Filter"
    params = dict()
    data = None
    params["dictionaryValue"] = dictionaryValue

    params["dimensionCode"] = dimensionCode

    params["value"] = value

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[OrderListElement])
    return result


async def GetListByRecipient(
    api: AsyncAPI,
    dateFrom: Optional[datetime] = Unset(),
    dateTo: Optional[datetime] = Unset(),
    recipientCode: str = Unset(),
    recipientId: int = Unset()
) -> IHttpActionResult[List[OrderListElement]]:
    match dateFrom, dateTo, recipientCode, recipientId:
        case datetime() | None | Unset(), datetime() | None | Unset(), str(), Unset():
            path = "/api/Orders/Filter"
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
            result = await IHttpActionResult.create(response, List[OrderListElement])
            return result
        case datetime() | None | Unset(), datetime() | None | Unset(), Unset(), int():
            path = "/api/Orders/Filter"
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
            result = await IHttpActionResult.create(response, List[OrderListElement])
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
    path = "/api/Orders/Markers"
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
    orderId: int = Unset(),
    orderNumber: str = Unset(),
    printNote: bool = Unset(),
    settings: PDFSettings = Unset()
) -> IHttpActionResult[PDF]:
    match buffer, orderId, orderNumber, printNote, settings:
        case Unset(), int(), Unset(), Unset(), PDFSettings():
            path = "/api/Orders/PDF"
            params = dict()
            params["orderId"] = orderId
            data = settings.model_dump_json(exclude_unset=True)
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PATCH", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, PDF)
            return result
        case bool(), Unset(), str(), bool(), Unset():
            path = "/api/Orders/PDF"
            params = dict()
            data = None
            params["buffer"] = buffer
            params["orderNumber"] = orderNumber
            params["printNote"] = printNote
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, PDF)
            return result
        case bool(), Unset(), str(), Unset(), PDFSettings():
            path = "/api/Orders/PDF"
            params = dict()
            params["buffer"] = buffer
            params["orderNumber"] = orderNumber
            data = settings.model_dump_json(exclude_unset=True)
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PATCH", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, PDF)
            return result
        case Unset(), int(), Unset(), bool(), Unset():
            path = "/api/Orders/PDF"
            params = dict()
            data = None
            params["orderId"] = orderId
            params["printNote"] = printNote
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, PDF)
            return result


async def GetPagedDocument(
    api: AsyncAPI, orderBy: enumOrderByType, page: int, size: int
) -> IHttpActionResult[Page[OrderListElement]]:
    """
    ['Page[OrderListElement]']
    :param api:
    :type api: AsyncAPI
    :param orderBy:
    :type orderBy: enumOrderByType
    :param page:
    :type page: int
    :param size:
    :type size: int
    :returns: Page[OrderListElement]
    :rtype: Page[OrderListElement]
    """
    path = "/api/Orders/Page"
    params = dict()
    data = None
    params["orderBy"] = orderBy

    params["page"] = page

    params["size"] = size

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, Page[OrderListElement])
    return result


async def GetPositionRelations(
    api: AsyncAPI, positionId: int
) -> IHttpActionResult[OrderPositionRelation]:
    """
    ['OrderPositionRelation']
    :param api:
    :type api: AsyncAPI
    :param positionId:
    :type positionId: int
    :returns: OrderPositionRelation
    :rtype: OrderPositionRelation
    """
    path = "/api/Orders/PositionRelations"
    params = dict()
    data = None
    params["positionId"] = positionId

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, OrderPositionRelation)
    return result


async def GetStatus(
    api: AsyncAPI,
    buffer: bool = Unset(),
    orderId: int = Unset(),
    orderNumber: str = Unset()
) -> IHttpActionResult[OrderStatus]:
    match buffer, orderId, orderNumber:
        case Unset(), int(), Unset():
            path = "/api/Orders/Status"
            params = dict()
            data = None
            params["orderId"] = orderId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, OrderStatus)
            return result
        case bool(), Unset(), str():
            path = "/api/Orders/Status"
            params = dict()
            data = None
            params["buffer"] = buffer
            params["orderNumber"] = orderNumber
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, OrderStatus)
            return result


async def GetWZ(
    api: AsyncAPI,
    buffer: bool = Unset(),
    orderId: int = Unset(),
    orderNumber: str = Unset()
) -> IHttpActionResult[List[OrderWZ]]:
    match buffer, orderId, orderNumber:
        case bool(), Unset(), str():
            path = "/api/Orders/WZ"
            params = dict()
            data = None
            params["buffer"] = buffer
            params["orderNumber"] = orderNumber
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[OrderWZ])
            return result
        case Unset(), int(), Unset():
            path = "/api/Orders/WZ"
            params = dict()
            data = None
            params["orderId"] = orderId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[OrderWZ])
            return result


async def GetZMODocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Orders/ZMODocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetZWODocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/Orders/ZWODocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
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
    path = "/api/Orders/IncrementalSync"
    params = dict()
    data = None
    params["dateFrom"] = dateFrom

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    # no return
    result = await IHttpActionResult.create(response, None)
    return result
