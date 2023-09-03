from .....Client import (
    AsyncAPI,
    ClientResponse,
    IHttpActionResult,
)
from .....Constants import (
    Unset,
)
from ...ViewModels import (
    Settlement,
    SettlementListElement,
)
from ...ViewModels.Issue import (
    SettlementIssue,
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


Get_T = TypeVar('Get_T', IHttpActionResult[Settlement], IHttpActionResult[List[SettlementListElement]])


@overload
async def Get(
    api: AsyncAPI, buffer: bool, number: str
) -> IHttpActionResult[Settlement]: ...


@overload
async def Get(
    api: AsyncAPI, id: int
) -> IHttpActionResult[Settlement]: ...


@overload
async def Get(
    api: AsyncAPI, 
) -> IHttpActionResult[List[SettlementListElement]]: ...


async def Get(
    api: AsyncAPI,
    buffer: bool = Unset(),
    id: int = Unset(),
    number: str = Unset()
) -> Get_T:
    match buffer, id, number:
        case bool(), Unset(), str():
            path = "/api/Settlements"
            params = dict()
            data = None
            params["buffer"] = buffer
            params["number"] = number
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, Settlement)
            return result
        case Unset(), int(), Unset():
            path = "/api/Settlements"
            params = dict()
            data = None
            params["id"] = id
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, Settlement)
            return result
        case Unset(), Unset(), Unset():
            path = "/api/Settlements"
            params = dict()
            data = None
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[SettlementListElement])
            return result


async def GetByDocument(
    api: AsyncAPI,
    buffer: bool = Unset(),
    documentId: int = Unset(),
    documentNumber: str = Unset()
) -> IHttpActionResult[Settlement]:
    match buffer, documentId, documentNumber:
        case Unset(), int(), Unset():
            path = "/api/Settlements"
            params = dict()
            data = None
            params["documentId"] = documentId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, Settlement)
            return result
        case bool(), Unset(), str():
            path = "/api/Settlements"
            params = dict()
            data = None
            params["buffer"] = buffer
            params["documentNumber"] = documentNumber
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, Settlement)
            return result


async def GetListByIssueDate(
    api: AsyncAPI,
    contractorCode: str = Unset(),
    contractorId: int = Unset(),
    dateFrom: Optional[datetime] = Unset(),
    dateTo: Optional[datetime] = Unset()
) -> IHttpActionResult[List[SettlementListElement]]:
    match contractorCode, contractorId, dateFrom, dateTo:
        case str(), Unset(), datetime() | None | Unset(), datetime() | None | Unset():
            path = "/api/Settlements/Filter/ByIssueDate"
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
            # no return
            result = await IHttpActionResult.create(response, None)
            return result
        case Unset(), Unset(), datetime() | None | Unset(), datetime() | None | Unset():
            path = "/api/Settlements/Filter/ByIssueDate"
            params = dict()
            data = None
            if dateFrom is not None and not isinstance(dateFrom, Unset):
                params["dateFrom"] = dateFrom
            if dateTo is not None and not isinstance(dateTo, Unset):
                params["dateTo"] = dateTo
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[SettlementListElement])
            return result
        case Unset(), int(), datetime() | None | Unset(), datetime() | None | Unset():
            path = "/api/Settlements/Filter/ByIssueDate"
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
            # no return
            result = await IHttpActionResult.create(response, None)
            return result


async def GetListByMaturityDate(
    api: AsyncAPI,
    contractorCode: str = Unset(),
    contractorId: int = Unset(),
    dateFrom: Optional[datetime] = Unset(),
    dateTo: Optional[datetime] = Unset()
) -> IHttpActionResult[List[SettlementListElement]]:
    match contractorCode, contractorId, dateFrom, dateTo:
        case str(), Unset(), datetime() | None | Unset(), datetime() | None | Unset():
            path = "/api/Settlements/Filter/ByMaturityDate"
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
            result = await IHttpActionResult.create(response, List[SettlementListElement])
            return result
        case Unset(), Unset(), datetime() | None | Unset(), datetime() | None | Unset():
            path = "/api/Settlements/Filter/ByMaturityDate"
            params = dict()
            data = None
            if dateFrom is not None and not isinstance(dateFrom, Unset):
                params["dateFrom"] = dateFrom
            if dateTo is not None and not isinstance(dateTo, Unset):
                params["dateTo"] = dateTo
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[SettlementListElement])
            return result
        case Unset(), int(), datetime() | None | Unset(), datetime() | None | Unset():
            path = "/api/Settlements/Filter/ByMaturityDate"
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
            result = await IHttpActionResult.create(response, List[SettlementListElement])
            return result


async def GetNotSettled(
    api: AsyncAPI, 
) -> IHttpActionResult[List[SettlementListElement]]:
    """
    ['List[SettlementListElement]']
    :param api:
    :type api: AsyncAPI
    :returns: List[SettlementListElement]
    :rtype: List[SettlementListElement]
    """
    path = "/api/Settlements/Filter/NotSettled"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[SettlementListElement])
    return result


async def GetNotSettledByIssueDate(
    api: AsyncAPI,
    contractorCode: str = Unset(),
    contractorId: int = Unset(),
    dateFrom: Optional[datetime] = Unset(),
    dateTo: Optional[datetime] = Unset()
) -> IHttpActionResult[List[SettlementListElement]]:
    match contractorCode, contractorId, dateFrom, dateTo:
        case Unset(), int(), datetime() | None | Unset(), datetime() | None | Unset():
            path = "/api/Settlements/Filter/NotSettled/ByIssueDate"
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
            # no return
            result = await IHttpActionResult.create(response, None)
            return result
        case str(), Unset(), datetime() | None | Unset(), datetime() | None | Unset():
            path = "/api/Settlements/Filter/NotSettled/ByIssueDate"
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
            # no return
            result = await IHttpActionResult.create(response, None)
            return result
        case Unset(), Unset(), datetime() | None | Unset(), datetime() | None | Unset():
            path = "/api/Settlements/Filter/NotSettled/ByIssueDate"
            params = dict()
            data = None
            if dateFrom is not None and not isinstance(dateFrom, Unset):
                params["dateFrom"] = dateFrom
            if dateTo is not None and not isinstance(dateTo, Unset):
                params["dateTo"] = dateTo
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[SettlementListElement])
            return result


async def GetNotSettledByMaturityDate(
    api: AsyncAPI,
    contractorCode: str = Unset(),
    contractorId: int = Unset(),
    dateFrom: Optional[datetime] = Unset(),
    dateTo: Optional[datetime] = Unset()
) -> IHttpActionResult[List[SettlementListElement]]:
    match contractorCode, contractorId, dateFrom, dateTo:
        case str(), Unset(), datetime() | None | Unset(), datetime() | None | Unset():
            path = "/api/Settlements/Filter/NotSettled/ByMaturityDate"
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
            result = await IHttpActionResult.create(response, List[SettlementListElement])
            return result
        case Unset(), int(), datetime() | None | Unset(), datetime() | None | Unset():
            path = "/api/Settlements/Filter/NotSettled/ByMaturityDate"
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
            result = await IHttpActionResult.create(response, List[SettlementListElement])
            return result
        case Unset(), Unset(), datetime() | None | Unset(), datetime() | None | Unset():
            path = "/api/Settlements/Filter/NotSettled/ByMaturityDate"
            params = dict()
            data = None
            if dateFrom is not None and not isinstance(dateFrom, Unset):
                params["dateFrom"] = dateFrom
            if dateTo is not None and not isinstance(dateTo, Unset):
                params["dateTo"] = dateTo
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[SettlementListElement])
            return result


async def Issue(
    api: AsyncAPI, settlement: SettlementIssue
) -> IHttpActionResult[Settlement]:
    """
    ['Settlement']
    :param api:
    :type api: AsyncAPI
    :param settlement:
    :type settlement: SettlementIssue
    :returns: Settlement
    :rtype: Settlement
    """
    path = "/api/Settlements/Issue"
    params = dict()
    data = settlement.model_dump_json(exclude_unset=True)
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="POST", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, Settlement)
    return result
