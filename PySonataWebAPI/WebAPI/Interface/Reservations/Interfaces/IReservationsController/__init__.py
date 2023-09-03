from .....Client import (
    AsyncAPI,
    ClientResponse,
    IHttpActionResult,
)
from .....Constants import (
    Unset,
)
from ...ViewModels import (
    AdvancedReservationNew,
    Reservation,
    ReservationListElement,
    ReservationNew,
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
    api: AsyncAPI, reservation: ReservationNew
) -> IHttpActionResult[Reservation]:
    """
    ['Reservation']
    :param api:
    :type api: AsyncAPI
    :param reservation:
    :type reservation: ReservationNew
    :returns: Reservation
    :rtype: Reservation
    """
    path = "/api/Reservations/Create"
    params = dict()
    data = reservation.model_dump_json(exclude_unset=True)
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="POST", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, Reservation)
    return result


async def AdvancedAddNew(
    api: AsyncAPI, reservation: AdvancedReservationNew
) -> IHttpActionResult[Reservation]:
    """
    ['Reservation']
    :param api:
    :type api: AsyncAPI
    :param reservation:
    :type reservation: AdvancedReservationNew
    :returns: Reservation
    :rtype: Reservation
    """
    path = "/api/Reservations/AdvancedCreate"
    params = dict()
    data = reservation.model_dump_json(exclude_unset=True)
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="POST", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, Reservation)
    return result


async def AdvancedDelete(
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
    path = "/api/Reservations/AdvancedDelete"
    params = dict()
    data = None
    params["id"] = id

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="DELETE", path=path, params=params, headers=headers, data=data)
    # no return
    result = await IHttpActionResult.create(response, None)
    return result


async def Delete(
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
    path = "/api/Reservations/Delete"
    params = dict()
    data = None
    params["id"] = id

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="DELETE", path=path, params=params, headers=headers, data=data)
    # no return
    result = await IHttpActionResult.create(response, None)
    return result


Get_T = TypeVar('Get_T', IHttpActionResult[Reservation], IHttpActionResult[List[ReservationListElement]])


@overload
async def Get(
    api: AsyncAPI, 
) -> IHttpActionResult[List[ReservationListElement]]: ...


@overload
async def Get(
    api: AsyncAPI, id: int
) -> IHttpActionResult[Reservation]: ...


async def Get(
    api: AsyncAPI,
    id: int = Unset()
) -> Get_T:
    match id:
        case Unset():
            path = "/api/Reservations"
            params = dict()
            data = None
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[ReservationListElement])
            return result
        case int():
            path = "/api/Reservations"
            params = dict()
            data = None
            params["id"] = id
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, Reservation)
            return result


async def GetListByContractor(
    api: AsyncAPI,
    contractorCode: str = Unset(),
    contractorId: int = Unset()
) -> IHttpActionResult[List[ReservationListElement]]:
    match contractorCode, contractorId:
        case str(), Unset():
            path = "/api/Reservations/Filter"
            params = dict()
            data = None
            params["contractorCode"] = contractorCode
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[ReservationListElement])
            return result
        case Unset(), int():
            path = "/api/Reservations/Filter"
            params = dict()
            data = None
            params["contractorId"] = contractorId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[ReservationListElement])
            return result


async def GetListByProduct(
    api: AsyncAPI,
    productCode: str = Unset(),
    productId: int = Unset()
) -> IHttpActionResult[List[ReservationListElement]]:
    match productCode, productId:
        case str(), Unset():
            path = "/api/Reservations/Filter"
            params = dict()
            data = None
            params["productCode"] = productCode
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[ReservationListElement])
            return result
        case Unset(), int():
            path = "/api/Reservations/Filter"
            params = dict()
            data = None
            params["productId"] = productId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[ReservationListElement])
            return result
