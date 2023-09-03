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
    OwnOrder,
    OwnOrderFV,
    OwnOrderListElement,
    OwnOrderPZ,
    OwnOrderPositionRelation,
    OwnOrderStatus,
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


Get_T = TypeVar('Get_T', IHttpActionResult[OwnOrder], IHttpActionResult[List[OwnOrderListElement]])


@overload
async def Get(
    api: AsyncAPI, id: int
) -> IHttpActionResult[OwnOrder]: ...


@overload
async def Get(
    api: AsyncAPI, 
) -> IHttpActionResult[List[OwnOrderListElement]]: ...


@overload
async def Get(
    api: AsyncAPI, buffer: bool, number: str
) -> IHttpActionResult[OwnOrder]: ...


async def Get(
    api: AsyncAPI,
    buffer: bool = Unset(),
    id: int = Unset(),
    number: str = Unset()
) -> Get_T:
    match buffer, id, number:
        case Unset(), int(), Unset():
            path = "/api/OwnOrders"
            params = dict()
            data = None
            params["id"] = id
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, OwnOrder)
            return result
        case Unset(), Unset(), Unset():
            path = "/api/OwnOrders"
            params = dict()
            data = None
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[OwnOrderListElement])
            return result
        case bool(), Unset(), str():
            path = "/api/OwnOrders"
            params = dict()
            data = None
            params["buffer"] = buffer
            params["number"] = number
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, OwnOrder)
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
    path = "/api/OwnOrders/Catalogs"
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
    path = "/api/OwnOrders/DocumentSeries"
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
) -> IHttpActionResult[List[OwnOrderFV]]:
    match buffer, orderId, orderNumber:
        case bool(), Unset(), str():
            path = "/api/OwnOrders/FV"
            params = dict()
            data = None
            params["buffer"] = buffer
            params["orderNumber"] = orderNumber
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[OwnOrderFV])
            return result
        case Unset(), int(), Unset():
            path = "/api/OwnOrders/FV"
            params = dict()
            data = None
            params["orderId"] = orderId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[OwnOrderFV])
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
    path = "/api/OwnOrders/Kinds"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[Kind])
    return result


async def GetList(
    api: AsyncAPI, dateFrom: Optional[datetime], dateTo: Optional[datetime]
) -> IHttpActionResult[List[OwnOrderListElement]]:
    """
    ['List[OwnOrderListElement]']
    :param api:
    :type api: AsyncAPI
    :param dateFrom:
    :type dateFrom: datetime | None
    :param dateTo:
    :type dateTo: datetime | None
    :returns: List[OwnOrderListElement]
    :rtype: List[OwnOrderListElement]
    """
    path = "/api/OwnOrders/Filter"
    params = dict()
    data = None
    if dateFrom is not None:
        params["dateFrom"] = dateFrom

    if dateTo is not None:
        params["dateTo"] = dateTo

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[OwnOrderListElement])
    return result


async def GetListByDeliverer(
    api: AsyncAPI,
    dateFrom: Optional[datetime] = Unset(),
    dateTo: Optional[datetime] = Unset(),
    delivererCode: str = Unset(),
    delivererId: int = Unset()
) -> IHttpActionResult[List[OwnOrderListElement]]:
    match dateFrom, dateTo, delivererCode, delivererId:
        case datetime() | None | Unset(), datetime() | None | Unset(), Unset(), int():
            path = "/api/OwnOrders/Filter"
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
            result = await IHttpActionResult.create(response, List[OwnOrderListElement])
            return result
        case datetime() | None | Unset(), datetime() | None | Unset(), str(), Unset():
            path = "/api/OwnOrders/Filter"
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
            result = await IHttpActionResult.create(response, List[OwnOrderListElement])
            return result


async def GetListByDimension(
    api: AsyncAPI, dictionaryValue: str, dimensionCode: str, value: str
) -> IHttpActionResult[List[OwnOrderListElement]]:
    """
    ['List[OwnOrderListElement]']
    :param api:
    :type api: AsyncAPI
    :param dictionaryValue:
    :type dictionaryValue: str
    :param dimensionCode:
    :type dimensionCode: str
    :param value:
    :type value: str
    :returns: List[OwnOrderListElement]
    :rtype: List[OwnOrderListElement]
    """
    path = "/api/OwnOrders/Filter"
    params = dict()
    data = None
    params["dictionaryValue"] = dictionaryValue

    params["dimensionCode"] = dimensionCode

    params["value"] = value

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[OwnOrderListElement])
    return result


async def GetListBySeller(
    api: AsyncAPI,
    dateFrom: Optional[datetime] = Unset(),
    dateTo: Optional[datetime] = Unset(),
    sellerCode: str = Unset(),
    sellerId: int = Unset()
) -> IHttpActionResult[List[OwnOrderListElement]]:
    match dateFrom, dateTo, sellerCode, sellerId:
        case datetime() | None | Unset(), datetime() | None | Unset(), str(), Unset():
            path = "/api/OwnOrders/Filter"
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
            result = await IHttpActionResult.create(response, List[OwnOrderListElement])
            return result
        case datetime() | None | Unset(), datetime() | None | Unset(), Unset(), int():
            path = "/api/OwnOrders/Filter"
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
            result = await IHttpActionResult.create(response, List[OwnOrderListElement])
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
    path = "/api/OwnOrders/Markers"
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
        case bool(), Unset(), str(), bool(), Unset():
            path = "/api/OwnOrders/PDF"
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
        case Unset(), int(), Unset(), Unset(), PDFSettings():
            path = "/api/OwnOrders/PDF"
            params = dict()
            params["orderId"] = orderId
            data = settings.model_dump_json(exclude_unset=True)
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PATCH", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, PDF)
            return result
        case Unset(), int(), Unset(), bool(), Unset():
            path = "/api/OwnOrders/PDF"
            params = dict()
            data = None
            params["orderId"] = orderId
            params["printNote"] = printNote
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, PDF)
            return result
        case bool(), Unset(), str(), Unset(), PDFSettings():
            path = "/api/OwnOrders/PDF"
            params = dict()
            params["buffer"] = buffer
            params["orderNumber"] = orderNumber
            data = settings.model_dump_json(exclude_unset=True)
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PATCH", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, PDF)
            return result


async def GetPZ(
    api: AsyncAPI,
    buffer: bool = Unset(),
    orderId: int = Unset(),
    orderNumber: str = Unset()
) -> IHttpActionResult[List[OwnOrderPZ]]:
    match buffer, orderId, orderNumber:
        case Unset(), int(), Unset():
            path = "/api/OwnOrders/PZ"
            params = dict()
            data = None
            params["orderId"] = orderId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[OwnOrderPZ])
            return result
        case bool(), Unset(), str():
            path = "/api/OwnOrders/PZ"
            params = dict()
            data = None
            params["buffer"] = buffer
            params["orderNumber"] = orderNumber
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[OwnOrderPZ])
            return result


async def GetPagedDocument(
    api: AsyncAPI, orderBy: enumOrderByType, page: int, size: int
) -> IHttpActionResult[Page[OwnOrderListElement]]:
    """
    ['Page[OwnOrderListElement]']
    :param api:
    :type api: AsyncAPI
    :param orderBy:
    :type orderBy: enumOrderByType
    :param page:
    :type page: int
    :param size:
    :type size: int
    :returns: Page[OwnOrderListElement]
    :rtype: Page[OwnOrderListElement]
    """
    path = "/api/OwnOrders/Page"
    params = dict()
    data = None
    params["orderBy"] = orderBy

    params["page"] = page

    params["size"] = size

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, Page[OwnOrderListElement])
    return result


async def GetPositionRelations(
    api: AsyncAPI, positionId: int
) -> IHttpActionResult[OwnOrderPositionRelation]:
    """
    ['OwnOrderPositionRelation']
    :param api:
    :type api: AsyncAPI
    :param positionId:
    :type positionId: int
    :returns: OwnOrderPositionRelation
    :rtype: OwnOrderPositionRelation
    """
    path = "/api/OwnOrders/PositionRelations"
    params = dict()
    data = None
    params["positionId"] = positionId

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, OwnOrderPositionRelation)
    return result


async def GetStatus(
    api: AsyncAPI,
    buffer: bool = Unset(),
    orderId: int = Unset(),
    orderNumber: str = Unset()
) -> IHttpActionResult[OwnOrderStatus]:
    match buffer, orderId, orderNumber:
        case bool(), Unset(), str():
            path = "/api/OwnOrders/Status"
            params = dict()
            data = None
            params["buffer"] = buffer
            params["orderNumber"] = orderNumber
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, OwnOrderStatus)
            return result
        case Unset(), int(), Unset():
            path = "/api/OwnOrders/Status"
            params = dict()
            data = None
            params["orderId"] = orderId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, OwnOrderStatus)
            return result


async def GetZMWDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/OwnOrders/ZMODocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result


async def GetZWWDocumentTypes(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentType]]:
    """
    ['List[DocumentType]']
    :param api:
    :type api: AsyncAPI
    :returns: List[DocumentType]
    :rtype: List[DocumentType]
    """
    path = "/api/OwnOrders/ZWODocumentTypes"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[DocumentType])
    return result
