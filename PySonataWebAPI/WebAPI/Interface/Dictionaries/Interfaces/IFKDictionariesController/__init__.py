from .....Client import (
    AsyncAPI,
    ClientResponse,
    IHttpActionResult,
)
from .....Constants import (
    Unset,
)
from ...ViewModels import (
    BusinessDictionary,
    BusinessDictionaryElement,
    ContractorPosition,
    Dictionary,
    DictionaryElement,
    DictionaryListElement,
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
    api: AsyncAPI, dictionaryId: int, element: DictionaryElement
) -> IHttpActionResult[None]:
    """
    []
    :param api:
    :type api: AsyncAPI
    :param dictionaryId:
    :type dictionaryId: int
    :param element:
    :type element: DictionaryElement
    :returns: 
    :rtype: 
    """
    path = "/api/Dictionaries/Create"
    params = dict()
    params["dictionaryId"] = dictionaryId

    data = element.model_dump_json(exclude_unset=True)
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="POST", path=path, params=params, headers=headers, data=data)
    # no return
    result = await IHttpActionResult.create(response, None)
    return result


async def AddNewBusiness(
    api: AsyncAPI, dictionaryId: int, element: BusinessDictionaryElement
) -> IHttpActionResult[None]:
    """
    []
    :param api:
    :type api: AsyncAPI
    :param dictionaryId:
    :type dictionaryId: int
    :param element:
    :type element: BusinessDictionaryElement
    :returns: 
    :rtype: 
    """
    path = "/api/FKDictionaries/CreateBusiness"
    params = dict()
    params["dictionaryId"] = dictionaryId

    data = element.model_dump_json(exclude_unset=True)
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="POST", path=path, params=params, headers=headers, data=data)
    # no return
    result = await IHttpActionResult.create(response, None)
    return result


Get_T = TypeVar('Get_T', IHttpActionResult[Dictionary], IHttpActionResult[List[DictionaryListElement]])


@overload
async def Get(
    api: AsyncAPI, id: int
) -> IHttpActionResult[Dictionary]: ...


@overload
async def Get(
    api: AsyncAPI, 
) -> IHttpActionResult[List[DictionaryListElement]]: ...


async def Get(
    api: AsyncAPI,
    id: int = Unset()
) -> Get_T:
    match id:
        case int():
            path = "/api/Dictionaries"
            params = dict()
            data = None
            params["id"] = id
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, Dictionary)
            return result
        case Unset():
            path = "/api/Dictionaries"
            params = dict()
            data = None
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[DictionaryListElement])
            return result


async def GetBusiness(
    api: AsyncAPI, id: int
) -> IHttpActionResult[BusinessDictionary]:
    """
    ['BusinessDictionary']
    :param api:
    :type api: AsyncAPI
    :param id:
    :type id: int
    :returns: BusinessDictionary
    :rtype: BusinessDictionary
    """
    path = "/api/FKDictionaries/Business"
    params = dict()
    data = None
    params["id"] = id

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, BusinessDictionary)
    return result


async def SetContractorPosition(
    api: AsyncAPI,
    id: int = Unset(),
    position: int = Unset()
) -> IHttpActionResult[ContractorPosition]:
    match id, position:
        case int(), Unset():
            path = "/api/FKDictionaries/SetContractorPosition"
            params = dict()
            data = None
            params["id"] = id
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PATCH", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, ContractorPosition)
            return result
        case int(), int():
            path = "/api/FKDictionaries/SetContractorPosition"
            params = dict()
            data = None
            params["id"] = id
            params["position"] = position
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PATCH", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, ContractorPosition)
            return result


async def SetElementPosition(
    api: AsyncAPI,
    id: int = Unset(),
    position: int = Unset()
) -> IHttpActionResult[None]:
    match id, position:
        case int(), int():
            path = "/api/FKDictionaries/SetElementPosition"
            params = dict()
            data = None
            params["id"] = id
            params["position"] = position
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PATCH", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result
        case int(), Unset():
            path = "/api/FKDictionaries/SetElementPosition"
            params = dict()
            data = None
            params["id"] = id
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PATCH", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result


async def Update(
    api: AsyncAPI, dictionaryId: int, element: DictionaryElement
) -> IHttpActionResult[None]:
    """
    []
    :param api:
    :type api: AsyncAPI
    :param dictionaryId:
    :type dictionaryId: int
    :param element:
    :type element: DictionaryElement
    :returns: 
    :rtype: 
    """
    path = "/api/Dictionaries/Update"
    params = dict()
    params["dictionaryId"] = dictionaryId

    data = element.model_dump_json(exclude_unset=True)
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
    # no return
    result = await IHttpActionResult.create(response, None)
    return result


async def UpdateBusiness(
    api: AsyncAPI, dictionaryId: int, element: BusinessDictionaryElement
) -> IHttpActionResult[None]:
    """
    []
    :param api:
    :type api: AsyncAPI
    :param dictionaryId:
    :type dictionaryId: int
    :param element:
    :type element: BusinessDictionaryElement
    :returns: 
    :rtype: 
    """
    path = "/api/FKDictionaries/UpdateBusiness"
    params = dict()
    params["dictionaryId"] = dictionaryId

    data = element.model_dump_json(exclude_unset=True)
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
    # no return
    result = await IHttpActionResult.create(response, None)
    return result
