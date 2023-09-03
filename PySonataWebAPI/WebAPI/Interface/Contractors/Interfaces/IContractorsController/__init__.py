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
    Kind,
    Marker,
)
from ....Enums import (
    enumOrderByType,
)
from ....ViewModels import (
    Page,
)
from ...ViewModels import (
    Contractor,
    ContractorFilterCriteria,
    ContractorListElement,
    ContractorListElementWithDimensions,
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
    api: AsyncAPI, contractor: Contractor, syncFk: bool
) -> IHttpActionResult[Contractor]:
    """
    ['Contractor']
    :param api:
    :type api: AsyncAPI
    :param contractor:
    :type contractor: Contractor
    :param syncFk:
    :type syncFk: bool
    :returns: Contractor
    :rtype: Contractor
    """
    path = "/api/Contractors/Create"
    params = dict()
    data = contractor.model_dump_json(exclude_unset=True)
    params["syncFk"] = syncFk

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="POST", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, Contractor)
    return result


async def Filter(
    api: AsyncAPI, criteria: ContractorFilterCriteria
) -> IHttpActionResult[List[ContractorListElement]]:
    """
    ['List[ContractorListElement]']
    :param api:
    :type api: AsyncAPI
    :param criteria:
    :type criteria: ContractorFilterCriteria
    :returns: List[ContractorListElement]
    :rtype: List[ContractorListElement]
    """
    path = "/api/Contractors/Filter"
    params = dict()
    data = criteria.model_dump_json(exclude_unset=True)
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="PATCH", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[ContractorListElement])
    return result


async def FilterWithDimensions(
    api: AsyncAPI, criteria: ContractorFilterCriteria
) -> IHttpActionResult[List[ContractorListElementWithDimensions]]:
    """
    ['List[ContractorListElementWithDimensions]']
    :param api:
    :type api: AsyncAPI
    :param criteria:
    :type criteria: ContractorFilterCriteria
    :returns: List[ContractorListElementWithDimensions]
    :rtype: List[ContractorListElementWithDimensions]
    """
    path = "/api/Contractors/Filter"
    params = dict()
    data = criteria.model_dump_json(exclude_unset=True)
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="PATCH", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[ContractorListElementWithDimensions])
    return result


Get_T = TypeVar('Get_T', IHttpActionResult[Contractor], IHttpActionResult[List[ContractorListElement]])


@overload
async def Get(
    api: AsyncAPI, code: str
) -> IHttpActionResult[Contractor]: ...


@overload
async def Get(
    api: AsyncAPI, id: int
) -> IHttpActionResult[Contractor]: ...


@overload
async def Get(
    api: AsyncAPI, 
) -> IHttpActionResult[List[ContractorListElement]]: ...


async def Get(
    api: AsyncAPI,
    code: str = Unset(),
    id: int = Unset()
) -> Get_T:
    match code, id:
        case str(), Unset():
            path = "/api/Contractors"
            params = dict()
            data = None
            params["code"] = code
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, Contractor)
            return result
        case Unset(), int():
            path = "/api/Contractors"
            params = dict()
            data = None
            params["id"] = id
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, Contractor)
            return result
        case Unset(), Unset():
            path = "/api/Contractors"
            params = dict()
            data = None
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[ContractorListElement])
            return result


async def GetByNIP(
    api: AsyncAPI, nip: str
) -> IHttpActionResult[List[Contractor]]:
    """
    ['List[Contractor]']
    :param api:
    :type api: AsyncAPI
    :param nip:
    :type nip: str
    :returns: List[Contractor]
    :rtype: List[Contractor]
    """
    path = "/api/Contractors"
    params = dict()
    data = None
    params["nip"] = nip

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[Contractor])
    return result


async def GetByNIPAndPosition(
    api: AsyncAPI, nip: str, position: int
) -> IHttpActionResult[List[Contractor]]:
    """
    ['List[Contractor]']
    :param api:
    :type api: AsyncAPI
    :param nip:
    :type nip: str
    :param position:
    :type position: int
    :returns: List[Contractor]
    :rtype: List[Contractor]
    """
    path = "/api/Contractors"
    params = dict()
    data = None
    params["nip"] = nip

    params["position"] = position

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[Contractor])
    return result


async def GetByPesel(
    api: AsyncAPI, pesel: str
) -> IHttpActionResult[List[Contractor]]:
    """
    ['List[Contractor]']
    :param api:
    :type api: AsyncAPI
    :param pesel:
    :type pesel: str
    :returns: List[Contractor]
    :rtype: List[Contractor]
    """
    path = "/api/Contractors"
    params = dict()
    data = None
    params["pesel"] = pesel

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[Contractor])
    return result


async def GetByPosition(
    api: AsyncAPI, position: int
) -> IHttpActionResult[List[Contractor]]:
    """
    ['List[Contractor]']
    :param api:
    :type api: AsyncAPI
    :param position:
    :type position: int
    :returns: List[Contractor]
    :rtype: List[Contractor]
    """
    path = "/api/Contractors"
    params = dict()
    data = None
    params["position"] = position

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[Contractor])
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
    path = "/api/Contractors/Catalogs"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[Catalog])
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
    path = "/api/Contractors/Kinds"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[Kind])
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
    path = "/api/Contractors/Markers"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[Marker])
    return result


async def GetPagedDocument(
    api: AsyncAPI, orderBy: enumOrderByType, page: int, size: int
) -> IHttpActionResult[Page[ContractorListElement]]:
    """
    ['Page[ContractorListElement]']
    :param api:
    :type api: AsyncAPI
    :param orderBy:
    :type orderBy: enumOrderByType
    :param page:
    :type page: int
    :param size:
    :type size: int
    :returns: Page[ContractorListElement]
    :rtype: Page[ContractorListElement]
    """
    path = "/api/Contractors/Page"
    params = dict()
    data = None
    params["orderBy"] = orderBy

    params["page"] = page

    params["size"] = size

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, Page[ContractorListElement])
    return result


async def GetPagedDocumentWithDimensions(
    api: AsyncAPI, orderBy: enumOrderByType, page: int, size: int
) -> IHttpActionResult[Page[ContractorListElementWithDimensions]]:
    """
    ['Page[ContractorListElementWithDimensions]']
    :param api:
    :type api: AsyncAPI
    :param orderBy:
    :type orderBy: enumOrderByType
    :param page:
    :type page: int
    :param size:
    :type size: int
    :returns: Page[ContractorListElementWithDimensions]
    :rtype: Page[ContractorListElementWithDimensions]
    """
    path = "/api/Contractors/PageWithDimensions"
    params = dict()
    data = None
    params["orderBy"] = orderBy

    params["page"] = page

    params["size"] = size

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, Page[ContractorListElementWithDimensions])
    return result


async def GetWithDimensions(
    api: AsyncAPI, 
) -> IHttpActionResult[List[ContractorListElementWithDimensions]]:
    """
    ['List[ContractorListElementWithDimensions]']
    :param api:
    :type api: AsyncAPI
    :returns: List[ContractorListElementWithDimensions]
    :rtype: List[ContractorListElementWithDimensions]
    """
    path = "/api/Contractors"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[ContractorListElementWithDimensions])
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
    path = "/api/Contractors/IncrementalSync"
    params = dict()
    data = None
    params["dateFrom"] = dateFrom

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    # no return
    result = await IHttpActionResult.create(response, None)
    return result


async def SyncFK(
    api: AsyncAPI,
    contractorCode: str = Unset(),
    contractorId: int = Unset(),
    isNew: bool = Unset()
) -> IHttpActionResult[None]:
    match contractorCode, contractorId, isNew:
        case Unset(), int(), bool():
            path = "/api/Contractors/SyncFK"
            params = dict()
            data = None
            params["contractorId"] = contractorId
            params["isNew"] = isNew
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PATCH", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result
        case str(), Unset(), bool():
            path = "/api/Contractors/SyncFK"
            params = dict()
            data = None
            params["contractorCode"] = contractorCode
            params["isNew"] = isNew
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PATCH", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result


async def Update(
    api: AsyncAPI, contractor: Contractor, syncFk: bool
) -> IHttpActionResult[None]:
    """
    []
    :param api:
    :type api: AsyncAPI
    :param contractor:
    :type contractor: Contractor
    :param syncFk:
    :type syncFk: bool
    :returns: 
    :rtype: 
    """
    path = "/api/Contractors/Update"
    params = dict()
    data = contractor.model_dump_json(exclude_unset=True)
    params["syncFk"] = syncFk

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
    # no return
    result = await IHttpActionResult.create(response, None)
    return result
