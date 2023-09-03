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
    FilterCriteria,
    FilterOption,
)
from ...ViewModels import (
    Contractor,
    ContractorListElement,
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
    api: AsyncAPI, contractor: Contractor
) -> IHttpActionResult[Contractor]:
    """
    ['Contractor']
    :param api:
    :type api: AsyncAPI
    :param contractor:
    :type contractor: Contractor
    :returns: Contractor
    :rtype: Contractor
    """
    path = "/api/FKContractors/Create"
    params = dict()
    data = contractor.model_dump_json(exclude_unset=True)
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="POST", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, Contractor)
    return result


async def Filter(
    api: AsyncAPI, criteria: List[FilterCriteria]
) -> IHttpActionResult[List[ContractorListElement]]:
    """
    ['List[ContractorListElement]']
    :param api:
    :type api: AsyncAPI
    :param criteria:
    :type criteria: FilterCriteria
    :returns: List[ContractorListElement]
    :rtype: List[ContractorListElement]
    """
    path = "/api/FKContractors/Filter"
    params = dict()
    data = f"[{','.join([elem.model_dump_json(exclude_unset=True) for elem in criteria])}]"
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="PATCH", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[ContractorListElement])
    return result


async def FilterOptions(
    api: AsyncAPI, 
) -> IHttpActionResult[List[FilterOption]]:
    """
    ['List[FilterOption]']
    :param api:
    :type api: AsyncAPI
    :returns: List[FilterOption]
    :rtype: List[FilterOption]
    """
    path = "/api/FKContractors/Filter"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="OPTIONS", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[FilterOption])
    return result


async def Get(
    api: AsyncAPI, 
) -> IHttpActionResult[List[ContractorListElement]]:
    """
    ['List[ContractorListElement]']
    :param api:
    :type api: AsyncAPI
    :returns: List[ContractorListElement]
    :rtype: List[ContractorListElement]
    """
    path = "/api/FKContractors"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[ContractorListElement])
    return result


async def GetByCode(
    api: AsyncAPI, code: str
) -> IHttpActionResult[Contractor]:
    """
    ['Contractor']
    :param api:
    :type api: AsyncAPI
    :param code:
    :type code: str
    :returns: Contractor
    :rtype: Contractor
    """
    path = "/api/FKContractors"
    params = dict()
    data = None
    params["code"] = code

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, Contractor)
    return result


async def GetById(
    api: AsyncAPI, id: int
) -> IHttpActionResult[Contractor]:
    """
    ['Contractor']
    :param api:
    :type api: AsyncAPI
    :param id:
    :type id: int
    :returns: Contractor
    :rtype: Contractor
    """
    path = "/api/FKContractors"
    params = dict()
    data = None
    params["id"] = id

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, Contractor)
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
    path = "/api/FKContractors"
    params = dict()
    data = None
    params["nip"] = nip

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
    path = "/api/FKContractors"
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
) -> IHttpActionResult[Contractor]:
    """
    ['Contractor']
    :param api:
    :type api: AsyncAPI
    :param position:
    :type position: int
    :returns: Contractor
    :rtype: Contractor
    """
    path = "/api/FKContractors"
    params = dict()
    data = None
    params["position"] = position

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, Contractor)
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
    path = "/api/FKContractors/Page"
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


async def Update(
    api: AsyncAPI, contractor: Contractor
) -> IHttpActionResult[None]:
    """
    []
    :param api:
    :type api: AsyncAPI
    :param contractor:
    :type contractor: Contractor
    :returns: 
    :rtype: 
    """
    path = "/api/FKContractors/Update"
    params = dict()
    data = contractor.model_dump_json(exclude_unset=True)
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
    # no return
    result = await IHttpActionResult.create(response, None)
    return result
