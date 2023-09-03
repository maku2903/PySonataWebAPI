from ......Client import (
    AsyncAPI,
    ClientResponse,
    IHttpActionResult,
)
from ......Constants import (
    Unset,
)
from .....Enums import (
    enumOrderByType,
)
from .....ViewModels import (
    Page,
)
from ....Common.ViewModels import (
    Marker,
)
from ...ViewModels import (
    Document,
    DocumentListElement,
    DocumentType,
    Feature,
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


Get_T = TypeVar('Get_T', IHttpActionResult[Document], IHttpActionResult[List[DocumentListElement]])


@overload
async def Get(
    api: AsyncAPI, id: int, yearId: int
) -> IHttpActionResult[Document]: ...


@overload
async def Get(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DocumentListElement]]: ...


async def Get(
    api: AsyncAPI,
    id: int = Unset(),
    yearId: int = Unset()
) -> Get_T:
    match id, yearId:
        case int(), int():
            path = "/api/FKDocuments"
            params = dict()
            data = None
            params["id"] = id
            params["yearId"] = yearId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, Document)
            return result
        case Unset(), Unset():
            path = "/api/FKDocuments"
            params = dict()
            data = None
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[DocumentListElement])
            return result


async def GetDocumentFeatures(
    api: AsyncAPI,
    yearId: int = Unset()
) -> IHttpActionResult[List[Feature]]:
    match yearId:
        case Unset():
            path = "/api/FKDocuments/DocumentFeatures"
            params = dict()
            data = None
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[Feature])
            return result
        case int():
            path = "/api/FKDocuments/DocumentFeatures"
            params = dict()
            data = None
            params["yearId"] = yearId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[Feature])
            return result


async def GetDocumentRecordFeatures(
    api: AsyncAPI,
    yearId: int = Unset()
) -> IHttpActionResult[List[Feature]]:
    match yearId:
        case int():
            path = "/api/FKDocuments/DocumentRecordFeatures"
            params = dict()
            data = None
            params["yearId"] = yearId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[Feature])
            return result
        case Unset():
            path = "/api/FKDocuments/DocumentRecordFeatures"
            params = dict()
            data = None
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[Feature])
            return result


async def GetDocumentTypes(
    api: AsyncAPI,
    yearId: int = Unset()
) -> IHttpActionResult[List[DocumentType]]:
    match yearId:
        case Unset():
            path = "/api/FKDocuments/DocumentTypes"
            params = dict()
            data = None
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[DocumentType])
            return result
        case int():
            path = "/api/FKDocuments/DocumentTypes"
            params = dict()
            data = None
            params["yearId"] = yearId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[DocumentType])
            return result


async def GetFromAccountingBooks(
    api: AsyncAPI,
    contractorPosition: int = Unset(),
    dateFrom: Optional[datetime] = Unset(),
    dateTo: Optional[datetime] = Unset(),
    yearId: int = Unset()
) -> IHttpActionResult[List[DocumentListElement]]:
    match contractorPosition, dateFrom, dateTo, yearId:
        case int(), datetime() | None | Unset(), datetime() | None | Unset(), int():
            path = "/api/FKDocuments/Buffer"
            params = dict()
            data = None
            params["contractorPosition"] = contractorPosition
            if dateFrom is not None and not isinstance(dateFrom, Unset):
                params["dateFrom"] = dateFrom
            if dateTo is not None and not isinstance(dateTo, Unset):
                params["dateTo"] = dateTo
            params["yearId"] = yearId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[DocumentListElement])
            return result
        case Unset(), datetime() | None | Unset(), datetime() | None | Unset(), int():
            path = "/api/FKDocuments/AccountingBooks"
            params = dict()
            data = None
            if dateFrom is not None and not isinstance(dateFrom, Unset):
                params["dateFrom"] = dateFrom
            if dateTo is not None and not isinstance(dateTo, Unset):
                params["dateTo"] = dateTo
            params["yearId"] = yearId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[DocumentListElement])
            return result


async def GetFromBuffer(
    api: AsyncAPI,
    contractorPosition: int = Unset(),
    dateFrom: Optional[datetime] = Unset(),
    dateTo: Optional[datetime] = Unset(),
    yearId: int = Unset()
) -> IHttpActionResult[List[DocumentListElement]]:
    match contractorPosition, dateFrom, dateTo, yearId:
        case int(), datetime() | None | Unset(), datetime() | None | Unset(), int():
            path = "/api/FKDocuments/Buffer"
            params = dict()
            data = None
            params["contractorPosition"] = contractorPosition
            if dateFrom is not None and not isinstance(dateFrom, Unset):
                params["dateFrom"] = dateFrom
            if dateTo is not None and not isinstance(dateTo, Unset):
                params["dateTo"] = dateTo
            params["yearId"] = yearId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[DocumentListElement])
            return result
        case Unset(), datetime() | None | Unset(), datetime() | None | Unset(), int():
            path = "/api/FKDocuments/Buffer"
            params = dict()
            data = None
            if dateFrom is not None and not isinstance(dateFrom, Unset):
                params["dateFrom"] = dateFrom
            if dateTo is not None and not isinstance(dateTo, Unset):
                params["dateTo"] = dateTo
            params["yearId"] = yearId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[DocumentListElement])
            return result


async def GetFromSchemes(
    api: AsyncAPI,
    contractorPosition: int = Unset(),
    dateFrom: Optional[datetime] = Unset(),
    dateTo: Optional[datetime] = Unset(),
    yearId: int = Unset()
) -> IHttpActionResult[List[DocumentListElement]]:
    match contractorPosition, dateFrom, dateTo, yearId:
        case Unset(), datetime() | None | Unset(), datetime() | None | Unset(), int():
            path = "/api/FKDocuments/Schemes"
            params = dict()
            data = None
            if dateFrom is not None and not isinstance(dateFrom, Unset):
                params["dateFrom"] = dateFrom
            if dateTo is not None and not isinstance(dateTo, Unset):
                params["dateTo"] = dateTo
            params["yearId"] = yearId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[DocumentListElement])
            return result
        case int(), datetime() | None | Unset(), datetime() | None | Unset(), int():
            path = "/api/FKDocuments/Buffer"
            params = dict()
            data = None
            params["contractorPosition"] = contractorPosition
            if dateFrom is not None and not isinstance(dateFrom, Unset):
                params["dateFrom"] = dateFrom
            if dateTo is not None and not isinstance(dateTo, Unset):
                params["dateTo"] = dateTo
            params["yearId"] = yearId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[DocumentListElement])
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
    path = "/api/FKDocuments/Markers"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[Marker])
    return result


async def GetPagedDocument(
    api: AsyncAPI, orderBy: enumOrderByType, page: int, size: int
) -> IHttpActionResult[Page[DocumentListElement]]:
    """
    ['Page[DocumentListElement]']
    :param api:
    :type api: AsyncAPI
    :param orderBy:
    :type orderBy: enumOrderByType
    :param page:
    :type page: int
    :param size:
    :type size: int
    :returns: Page[DocumentListElement]
    :rtype: Page[DocumentListElement]
    """
    path = "/api/FKDocuments/Page"
    params = dict()
    data = None
    params["orderBy"] = orderBy

    params["page"] = page

    params["size"] = size

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, Page[DocumentListElement])
    return result
