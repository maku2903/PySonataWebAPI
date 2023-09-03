from ......Client import (
    AsyncAPI,
    ClientResponse,
    IHttpActionResult,
)
from ......Constants import (
    Unset,
)
from ...ViewModels import (
    CurrencyTable,
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
    api: AsyncAPI,
    currencyId: int = Unset(),
    date: Optional[datetime] = Unset()
) -> IHttpActionResult[List[CurrencyTable]]:
    match currencyId, date:
        case Unset(), Unset():
            path = "/api/FKCurrenciesTables"
            params = dict()
            data = None
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[CurrencyTable])
            return result
        case int(), datetime() | None | Unset():
            path = "/api/FKCurrenciesTables"
            params = dict()
            data = None
            params["currencyId"] = currencyId
            if date is not None and not isinstance(date, Unset):
                params["date"] = date
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[CurrencyTable])
            return result


async def GetList(
    api: AsyncAPI, dateFrom: Optional[datetime], dateTo: Optional[datetime]
) -> IHttpActionResult[List[CurrencyTable]]:
    """
    ['List[CurrencyTable]']
    :param api:
    :type api: AsyncAPI
    :param dateFrom:
    :type dateFrom: datetime | None
    :param dateTo:
    :type dateTo: datetime | None
    :returns: List[CurrencyTable]
    :rtype: List[CurrencyTable]
    """
    path = "/api/FKCurrenciesTables/Filter"
    params = dict()
    data = None
    if dateFrom is not None:
        params["dateFrom"] = dateFrom

    if dateTo is not None:
        params["dateTo"] = dateTo

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[CurrencyTable])
    return result


async def GetListByCurrency(
    api: AsyncAPI, currencyId: int, dateFrom: Optional[datetime], dateTo: Optional[datetime]
) -> IHttpActionResult[List[CurrencyTable]]:
    """
    ['List[CurrencyTable]']
    :param api:
    :type api: AsyncAPI
    :param currencyId:
    :type currencyId: int
    :param dateFrom:
    :type dateFrom: datetime | None
    :param dateTo:
    :type dateTo: datetime | None
    :returns: List[CurrencyTable]
    :rtype: List[CurrencyTable]
    """
    path = "/api/FKCurrenciesTables/Filter"
    params = dict()
    data = None
    params["currencyId"] = currencyId

    if dateFrom is not None:
        params["dateFrom"] = dateFrom

    if dateTo is not None:
        params["dateTo"] = dateTo

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[CurrencyTable])
    return result
