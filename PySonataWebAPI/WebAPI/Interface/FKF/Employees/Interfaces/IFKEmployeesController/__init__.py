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
from ...ViewModels import (
    Employee,
    EmployeeListElement,
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
    api: AsyncAPI, employee: Employee
) -> IHttpActionResult[Employee]:
    """
    ['Employee']
    :param api:
    :type api: AsyncAPI
    :param employee:
    :type employee: Employee
    :returns: Employee
    :rtype: Employee
    """
    path = "/api/FKEmployees/Create"
    params = dict()
    data = employee.model_dump_json(exclude_unset=True)
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="POST", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, Employee)
    return result


async def Get(
    api: AsyncAPI, 
) -> IHttpActionResult[List[EmployeeListElement]]:
    """
    ['List[EmployeeListElement]']
    :param api:
    :type api: AsyncAPI
    :returns: List[EmployeeListElement]
    :rtype: List[EmployeeListElement]
    """
    path = "/api/FKEmployees"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[EmployeeListElement])
    return result


async def GetByCode(
    api: AsyncAPI, code: str
) -> IHttpActionResult[Employee]:
    """
    ['Employee']
    :param api:
    :type api: AsyncAPI
    :param code:
    :type code: str
    :returns: Employee
    :rtype: Employee
    """
    path = "/api/FKEmployees"
    params = dict()
    data = None
    params["code"] = code

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, Employee)
    return result


async def GetById(
    api: AsyncAPI, id: int
) -> IHttpActionResult[Employee]:
    """
    ['Employee']
    :param api:
    :type api: AsyncAPI
    :param id:
    :type id: int
    :returns: Employee
    :rtype: Employee
    """
    path = "/api/FKEmployees"
    params = dict()
    data = None
    params["id"] = id

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, Employee)
    return result


async def GetByPosition(
    api: AsyncAPI, position: int
) -> IHttpActionResult[Employee]:
    """
    ['Employee']
    :param api:
    :type api: AsyncAPI
    :param position:
    :type position: int
    :returns: Employee
    :rtype: Employee
    """
    path = "/api/FKEmployees"
    params = dict()
    data = None
    params["position"] = position

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, Employee)
    return result


async def GetPagedDocument(
    api: AsyncAPI, orderBy: enumOrderByType, page: int, size: int
) -> IHttpActionResult[Page[EmployeeListElement]]:
    """
    ['Page[EmployeeListElement]']
    :param api:
    :type api: AsyncAPI
    :param orderBy:
    :type orderBy: enumOrderByType
    :param page:
    :type page: int
    :param size:
    :type size: int
    :returns: Page[EmployeeListElement]
    :rtype: Page[EmployeeListElement]
    """
    path = "/api/FKEmployees/Page"
    params = dict()
    data = None
    params["orderBy"] = orderBy

    params["page"] = page

    params["size"] = size

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, Page[EmployeeListElement])
    return result


async def Update(
    api: AsyncAPI, employee: Employee
) -> IHttpActionResult[None]:
    """
    []
    :param api:
    :type api: AsyncAPI
    :param employee:
    :type employee: Employee
    :returns: 
    :rtype: 
    """
    path = "/api/FKEmployees/Update"
    params = dict()
    data = employee.model_dump_json(exclude_unset=True)
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
    # no return
    result = await IHttpActionResult.create(response, None)
    return result
