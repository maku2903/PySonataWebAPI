from .....Client import (
    AsyncAPI,
    ClientResponse,
    IHttpActionResult,
)
from .....Constants import (
    Unset,
)
from ...ViewModels import (
    BankAccount,
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


async def Get(
    api: AsyncAPI, id: int
) -> IHttpActionResult[BankAccount]:
    """
    ['BankAccount']
    :param api:
    :type api: AsyncAPI
    :param id:
    :type id: int
    :returns: BankAccount
    :rtype: BankAccount
    """
    path = "/api/BankAccounts"
    params = dict()
    data = None
    params["id"] = id

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, BankAccount)
    return result


async def GetListByContractor(
    api: AsyncAPI,
    contractorCode: str = Unset(),
    contractorId: int = Unset()
) -> IHttpActionResult[List[BankAccount]]:
    match contractorCode, contractorId:
        case Unset(), int():
            path = "/api/BankAccounts"
            params = dict()
            data = None
            params["contractorId"] = contractorId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[BankAccount])
            return result
        case str(), Unset():
            path = "/api/BankAccounts"
            params = dict()
            data = None
            params["contractorCode"] = contractorCode
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[BankAccount])
            return result


async def Insert(
    api: AsyncAPI,
    bankAccount: BankAccount = Unset(),
    contractorCode: str = Unset(),
    contractorId: int = Unset()
) -> IHttpActionResult[BankAccount]:
    match bankAccount, contractorCode, contractorId:
        case BankAccount(), Unset(), int():
            path = "/api/BankAccounts/Create"
            params = dict()
            data = bankAccount.model_dump_json(exclude_unset=True)
            params["contractorId"] = contractorId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="POST", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, BankAccount)
            return result
        case BankAccount(), str(), Unset():
            path = "/api/BankAccounts/Create"
            params = dict()
            data = bankAccount.model_dump_json(exclude_unset=True)
            params["contractorCode"] = contractorCode
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="POST", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, BankAccount)
            return result


async def SetAsMain(
    api: AsyncAPI, id: int
) -> IHttpActionResult[None]:
    """
    []
    :param api:
    :type api: AsyncAPI
    :param id:
    :type id: int
    :returns: 
    :rtype: 
    """
    path = "/api/BankAccounts/SetAsMain"
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
    api: AsyncAPI, bankAccount: BankAccount
) -> IHttpActionResult[None]:
    """
    []
    :param api:
    :type api: AsyncAPI
    :param bankAccount:
    :type bankAccount: BankAccount
    :returns: 
    :rtype: 
    """
    path = "/api/BankAccounts/Update"
    params = dict()
    data = bankAccount.model_dump_json(exclude_unset=True)
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
    # no return
    result = await IHttpActionResult.create(response, None)
    return result
