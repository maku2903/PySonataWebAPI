from ......Client import (
    AsyncAPI,
    ClientResponse,
    IHttpActionResult,
)
from ......Constants import (
    Unset,
)
from ...ViewModels import (
    CalculationFilterOptions,
    CalculationListElement,
    CalculationListElementGrouped,
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


async def Custom(
    api: AsyncAPI, options: CalculationFilterOptions
) -> IHttpActionResult[List[CalculationListElement]]:
    """
    ['List[CalculationListElement]']
    :param api:
    :type api: AsyncAPI
    :param options:
    :type options: CalculationFilterOptions
    :returns: List[CalculationListElement]
    :rtype: List[CalculationListElement]
    """
    path = "/api/FKCalculations/CustomFilter"
    params = dict()
    data = options.model_dump_json(exclude_unset=True)
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[CalculationListElement])
    return result


async def Get(
    api: AsyncAPI, 
) -> IHttpActionResult[List[CalculationListElement]]:
    """
    ['List[CalculationListElement]']
    :param api:
    :type api: AsyncAPI
    :returns: List[CalculationListElement]
    :rtype: List[CalculationListElement]
    """
    path = "/api/FKCalculations"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[CalculationListElement])
    return result


async def GetAfterMaturityTermByContractor(
    api: AsyncAPI, contractorPosition: int, dateFrom: Optional[datetime], dateTo: Optional[datetime]
) -> IHttpActionResult[List[CalculationListElement]]:
    """
    ['List[CalculationListElement]']
    :param api:
    :type api: AsyncAPI
    :param contractorPosition:
    :type contractorPosition: int
    :param dateFrom:
    :type dateFrom: datetime | None
    :param dateTo:
    :type dateTo: datetime | None
    :returns: List[CalculationListElement]
    :rtype: List[CalculationListElement]
    """
    path = "/api/FKCalculations/Filter/AfterMaturityTerm"
    params = dict()
    data = None
    params["contractorPosition"] = contractorPosition

    if dateFrom is not None:
        params["dateFrom"] = dateFrom

    if dateTo is not None:
        params["dateTo"] = dateTo

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[CalculationListElement])
    return result


async def GetAfterMaturityTermByEmployee(
    api: AsyncAPI, dateFrom: Optional[datetime], dateTo: Optional[datetime], employeePosition: int
) -> IHttpActionResult[List[CalculationListElement]]:
    """
    ['List[CalculationListElement]']
    :param api:
    :type api: AsyncAPI
    :param dateFrom:
    :type dateFrom: datetime | None
    :param dateTo:
    :type dateTo: datetime | None
    :param employeePosition:
    :type employeePosition: int
    :returns: List[CalculationListElement]
    :rtype: List[CalculationListElement]
    """
    path = "/api/FKCalculations/Filter/AfterMaturityTerm"
    params = dict()
    data = None
    if dateFrom is not None:
        params["dateFrom"] = dateFrom

    if dateTo is not None:
        params["dateTo"] = dateTo

    params["employeePosition"] = employeePosition

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[CalculationListElement])
    return result


async def GetBeforeMaturityTermByContractor(
    api: AsyncAPI, contractorPosition: int, dateFrom: Optional[datetime], dateTo: Optional[datetime]
) -> IHttpActionResult[List[CalculationListElement]]:
    """
    ['List[CalculationListElement]']
    :param api:
    :type api: AsyncAPI
    :param contractorPosition:
    :type contractorPosition: int
    :param dateFrom:
    :type dateFrom: datetime | None
    :param dateTo:
    :type dateTo: datetime | None
    :returns: List[CalculationListElement]
    :rtype: List[CalculationListElement]
    """
    path = "/api/FKCalculations/Filter/BeforeMaturityTerm"
    params = dict()
    data = None
    params["contractorPosition"] = contractorPosition

    if dateFrom is not None:
        params["dateFrom"] = dateFrom

    if dateTo is not None:
        params["dateTo"] = dateTo

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[CalculationListElement])
    return result


async def GetBeforeMaturityTermByEmployee(
    api: AsyncAPI, dateFrom: Optional[datetime], dateTo: Optional[datetime], employeePosition: int
) -> IHttpActionResult[List[CalculationListElement]]:
    """
    ['List[CalculationListElement]']
    :param api:
    :type api: AsyncAPI
    :param dateFrom:
    :type dateFrom: datetime | None
    :param dateTo:
    :type dateTo: datetime | None
    :param employeePosition:
    :type employeePosition: int
    :returns: List[CalculationListElement]
    :rtype: List[CalculationListElement]
    """
    path = "/api/FKCalculations/Filter/BeforeMaturityTerm"
    params = dict()
    data = None
    if dateFrom is not None:
        params["dateFrom"] = dateFrom

    if dateTo is not None:
        params["dateTo"] = dateTo

    params["employeePosition"] = employeePosition

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[CalculationListElement])
    return result


async def GetByContractor(
    api: AsyncAPI, contractorPosition: int, dateFrom: Optional[datetime], dateTo: Optional[datetime]
) -> IHttpActionResult[List[CalculationListElement]]:
    """
    ['List[CalculationListElement]']
    :param api:
    :type api: AsyncAPI
    :param contractorPosition:
    :type contractorPosition: int
    :param dateFrom:
    :type dateFrom: datetime | None
    :param dateTo:
    :type dateTo: datetime | None
    :returns: List[CalculationListElement]
    :rtype: List[CalculationListElement]
    """
    path = "/api/FKCalculations/Filter"
    params = dict()
    data = None
    params["contractorPosition"] = contractorPosition

    if dateFrom is not None:
        params["dateFrom"] = dateFrom

    if dateTo is not None:
        params["dateTo"] = dateTo

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[CalculationListElement])
    return result


async def GetByEmployee(
    api: AsyncAPI, dateFrom: Optional[datetime], dateTo: Optional[datetime], employeePosition: int
) -> IHttpActionResult[List[CalculationListElement]]:
    """
    ['List[CalculationListElement]']
    :param api:
    :type api: AsyncAPI
    :param dateFrom:
    :type dateFrom: datetime | None
    :param dateTo:
    :type dateTo: datetime | None
    :param employeePosition:
    :type employeePosition: int
    :returns: List[CalculationListElement]
    :rtype: List[CalculationListElement]
    """
    path = "/api/FKCalculations/Filter"
    params = dict()
    data = None
    if dateFrom is not None:
        params["dateFrom"] = dateFrom

    if dateTo is not None:
        params["dateTo"] = dateTo

    params["employeePosition"] = employeePosition

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[CalculationListElement])
    return result


async def GetDueAfterMaturityTermByContractor(
    api: AsyncAPI, contractorPosition: int, dateFrom: Optional[datetime], dateTo: Optional[datetime]
) -> IHttpActionResult[List[CalculationListElement]]:
    """
    ['List[CalculationListElement]']
    :param api:
    :type api: AsyncAPI
    :param contractorPosition:
    :type contractorPosition: int
    :param dateFrom:
    :type dateFrom: datetime | None
    :param dateTo:
    :type dateTo: datetime | None
    :returns: List[CalculationListElement]
    :rtype: List[CalculationListElement]
    """
    path = "/api/FKCalculations/Filter/Due/AfterMaturityTerm"
    params = dict()
    data = None
    params["contractorPosition"] = contractorPosition

    if dateFrom is not None:
        params["dateFrom"] = dateFrom

    if dateTo is not None:
        params["dateTo"] = dateTo

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[CalculationListElement])
    return result


async def GetDueAfterMaturityTermByEmployee(
    api: AsyncAPI, dateFrom: Optional[datetime], dateTo: Optional[datetime], employeePosition: int
) -> IHttpActionResult[List[CalculationListElement]]:
    """
    ['List[CalculationListElement]']
    :param api:
    :type api: AsyncAPI
    :param dateFrom:
    :type dateFrom: datetime | None
    :param dateTo:
    :type dateTo: datetime | None
    :param employeePosition:
    :type employeePosition: int
    :returns: List[CalculationListElement]
    :rtype: List[CalculationListElement]
    """
    path = "/api/FKCalculations/Filter/Due/AfterMaturityTerm"
    params = dict()
    data = None
    if dateFrom is not None:
        params["dateFrom"] = dateFrom

    if dateTo is not None:
        params["dateTo"] = dateTo

    params["employeePosition"] = employeePosition

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[CalculationListElement])
    return result


async def GetDueAfterMaturityTermGroupedBySubject(
    api: AsyncAPI, dateFrom: Optional[datetime], dateTo: Optional[datetime]
) -> IHttpActionResult[List[CalculationListElementGrouped]]:
    """
    ['List[CalculationListElementGrouped]']
    :param api:
    :type api: AsyncAPI
    :param dateFrom:
    :type dateFrom: datetime | None
    :param dateTo:
    :type dateTo: datetime | None
    :returns: List[CalculationListElementGrouped]
    :rtype: List[CalculationListElementGrouped]
    """
    path = "/api/FKCalculations/Grouped/Due/AfterMaturityTerm"
    params = dict()
    data = None
    if dateFrom is not None:
        params["dateFrom"] = dateFrom

    if dateTo is not None:
        params["dateTo"] = dateTo

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[CalculationListElementGrouped])
    return result


async def GetDueBeforeMaturityTermByContractor(
    api: AsyncAPI, contractorPosition: int, dateFrom: Optional[datetime], dateTo: Optional[datetime]
) -> IHttpActionResult[List[CalculationListElement]]:
    """
    ['List[CalculationListElement]']
    :param api:
    :type api: AsyncAPI
    :param contractorPosition:
    :type contractorPosition: int
    :param dateFrom:
    :type dateFrom: datetime | None
    :param dateTo:
    :type dateTo: datetime | None
    :returns: List[CalculationListElement]
    :rtype: List[CalculationListElement]
    """
    path = "/api/FKCalculations/Filter/Due/BeforeMaturityTerm"
    params = dict()
    data = None
    params["contractorPosition"] = contractorPosition

    if dateFrom is not None:
        params["dateFrom"] = dateFrom

    if dateTo is not None:
        params["dateTo"] = dateTo

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[CalculationListElement])
    return result


async def GetDueBeforeMaturityTermByEmployee(
    api: AsyncAPI, dateFrom: Optional[datetime], dateTo: Optional[datetime], employeePosition: int
) -> IHttpActionResult[List[CalculationListElement]]:
    """
    ['List[CalculationListElement]']
    :param api:
    :type api: AsyncAPI
    :param dateFrom:
    :type dateFrom: datetime | None
    :param dateTo:
    :type dateTo: datetime | None
    :param employeePosition:
    :type employeePosition: int
    :returns: List[CalculationListElement]
    :rtype: List[CalculationListElement]
    """
    path = "/api/FKCalculations/Filter/Due/BeforeMaturityTerm"
    params = dict()
    data = None
    if dateFrom is not None:
        params["dateFrom"] = dateFrom

    if dateTo is not None:
        params["dateTo"] = dateTo

    params["employeePosition"] = employeePosition

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[CalculationListElement])
    return result


async def GetDueBeforeMaturityTermGroupedBySubject(
    api: AsyncAPI, dateFrom: Optional[datetime], dateTo: Optional[datetime]
) -> IHttpActionResult[List[CalculationListElementGrouped]]:
    """
    ['List[CalculationListElementGrouped]']
    :param api:
    :type api: AsyncAPI
    :param dateFrom:
    :type dateFrom: datetime | None
    :param dateTo:
    :type dateTo: datetime | None
    :returns: List[CalculationListElementGrouped]
    :rtype: List[CalculationListElementGrouped]
    """
    path = "/api/FKCalculations/Grouped/Due/BeforeMaturityTerm"
    params = dict()
    data = None
    if dateFrom is not None:
        params["dateFrom"] = dateFrom

    if dateTo is not None:
        params["dateTo"] = dateTo

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[CalculationListElementGrouped])
    return result


async def GetDueByContractor(
    api: AsyncAPI, contractorPosition: int, dateFrom: Optional[datetime], dateTo: Optional[datetime]
) -> IHttpActionResult[List[CalculationListElement]]:
    """
    ['List[CalculationListElement]']
    :param api:
    :type api: AsyncAPI
    :param contractorPosition:
    :type contractorPosition: int
    :param dateFrom:
    :type dateFrom: datetime | None
    :param dateTo:
    :type dateTo: datetime | None
    :returns: List[CalculationListElement]
    :rtype: List[CalculationListElement]
    """
    path = "/api/FKCalculations/Filter/Due"
    params = dict()
    data = None
    params["contractorPosition"] = contractorPosition

    if dateFrom is not None:
        params["dateFrom"] = dateFrom

    if dateTo is not None:
        params["dateTo"] = dateTo

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[CalculationListElement])
    return result


async def GetDueByEmployee(
    api: AsyncAPI, dateFrom: Optional[datetime], dateTo: Optional[datetime], employeePosition: int
) -> IHttpActionResult[List[CalculationListElement]]:
    """
    ['List[CalculationListElement]']
    :param api:
    :type api: AsyncAPI
    :param dateFrom:
    :type dateFrom: datetime | None
    :param dateTo:
    :type dateTo: datetime | None
    :param employeePosition:
    :type employeePosition: int
    :returns: List[CalculationListElement]
    :rtype: List[CalculationListElement]
    """
    path = "/api/FKCalculations/Filter/Due"
    params = dict()
    data = None
    if dateFrom is not None:
        params["dateFrom"] = dateFrom

    if dateTo is not None:
        params["dateTo"] = dateTo

    params["employeePosition"] = employeePosition

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[CalculationListElement])
    return result


async def GetDueGroupedBySubject(
    api: AsyncAPI, dateFrom: Optional[datetime], dateTo: Optional[datetime]
) -> IHttpActionResult[List[CalculationListElementGrouped]]:
    """
    ['List[CalculationListElementGrouped]']
    :param api:
    :type api: AsyncAPI
    :param dateFrom:
    :type dateFrom: datetime | None
    :param dateTo:
    :type dateTo: datetime | None
    :returns: List[CalculationListElementGrouped]
    :rtype: List[CalculationListElementGrouped]
    """
    path = "/api/FKCalculations/Grouped/Due"
    params = dict()
    data = None
    if dateFrom is not None:
        params["dateFrom"] = dateFrom

    if dateTo is not None:
        params["dateTo"] = dateTo

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[CalculationListElementGrouped])
    return result


async def GetDueNotSettledByContractor(
    api: AsyncAPI, contractorPosition: int, dateFrom: Optional[datetime], dateTo: Optional[datetime]
) -> IHttpActionResult[List[CalculationListElement]]:
    """
    ['List[CalculationListElement]']
    :param api:
    :type api: AsyncAPI
    :param contractorPosition:
    :type contractorPosition: int
    :param dateFrom:
    :type dateFrom: datetime | None
    :param dateTo:
    :type dateTo: datetime | None
    :returns: List[CalculationListElement]
    :rtype: List[CalculationListElement]
    """
    path = "/api/FKCalculations/Filter/Due/NotSettled"
    params = dict()
    data = None
    params["contractorPosition"] = contractorPosition

    if dateFrom is not None:
        params["dateFrom"] = dateFrom

    if dateTo is not None:
        params["dateTo"] = dateTo

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[CalculationListElement])
    return result


async def GetDueNotSettledByEmployee(
    api: AsyncAPI, dateFrom: Optional[datetime], dateTo: Optional[datetime], employeePosition: int
) -> IHttpActionResult[List[CalculationListElement]]:
    """
    ['List[CalculationListElement]']
    :param api:
    :type api: AsyncAPI
    :param dateFrom:
    :type dateFrom: datetime | None
    :param dateTo:
    :type dateTo: datetime | None
    :param employeePosition:
    :type employeePosition: int
    :returns: List[CalculationListElement]
    :rtype: List[CalculationListElement]
    """
    path = "/api/FKCalculations/Filter/Due/NotSettled"
    params = dict()
    data = None
    if dateFrom is not None:
        params["dateFrom"] = dateFrom

    if dateTo is not None:
        params["dateTo"] = dateTo

    params["employeePosition"] = employeePosition

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[CalculationListElement])
    return result


async def GetDueNotSettledGroupedBySubject(
    api: AsyncAPI, dateFrom: Optional[datetime], dateTo: Optional[datetime]
) -> IHttpActionResult[List[CalculationListElementGrouped]]:
    """
    ['List[CalculationListElementGrouped]']
    :param api:
    :type api: AsyncAPI
    :param dateFrom:
    :type dateFrom: datetime | None
    :param dateTo:
    :type dateTo: datetime | None
    :returns: List[CalculationListElementGrouped]
    :rtype: List[CalculationListElementGrouped]
    """
    path = "/api/FKCalculations/Grouped/Due/NotSettled"
    params = dict()
    data = None
    if dateFrom is not None:
        params["dateFrom"] = dateFrom

    if dateTo is not None:
        params["dateTo"] = dateTo

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[CalculationListElementGrouped])
    return result


async def GetNotSettledByContractor(
    api: AsyncAPI, contractorPosition: int, dateFrom: Optional[datetime], dateTo: Optional[datetime]
) -> IHttpActionResult[List[CalculationListElement]]:
    """
    ['List[CalculationListElement]']
    :param api:
    :type api: AsyncAPI
    :param contractorPosition:
    :type contractorPosition: int
    :param dateFrom:
    :type dateFrom: datetime | None
    :param dateTo:
    :type dateTo: datetime | None
    :returns: List[CalculationListElement]
    :rtype: List[CalculationListElement]
    """
    path = "/api/FKCalculations/Filter/NotSettled"
    params = dict()
    data = None
    params["contractorPosition"] = contractorPosition

    if dateFrom is not None:
        params["dateFrom"] = dateFrom

    if dateTo is not None:
        params["dateTo"] = dateTo

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[CalculationListElement])
    return result


async def GetNotSettledByEmployee(
    api: AsyncAPI, dateFrom: Optional[datetime], dateTo: Optional[datetime], employeePosition: int
) -> IHttpActionResult[List[CalculationListElement]]:
    """
    ['List[CalculationListElement]']
    :param api:
    :type api: AsyncAPI
    :param dateFrom:
    :type dateFrom: datetime | None
    :param dateTo:
    :type dateTo: datetime | None
    :param employeePosition:
    :type employeePosition: int
    :returns: List[CalculationListElement]
    :rtype: List[CalculationListElement]
    """
    path = "/api/FKCalculations/Filter/NotSettled"
    params = dict()
    data = None
    if dateFrom is not None:
        params["dateFrom"] = dateFrom

    if dateTo is not None:
        params["dateTo"] = dateTo

    params["employeePosition"] = employeePosition

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[CalculationListElement])
    return result


async def GetObligationAfterMaturityTermByContractor(
    api: AsyncAPI, contractorPosition: int, dateFrom: Optional[datetime], dateTo: Optional[datetime]
) -> IHttpActionResult[List[CalculationListElement]]:
    """
    ['List[CalculationListElement]']
    :param api:
    :type api: AsyncAPI
    :param contractorPosition:
    :type contractorPosition: int
    :param dateFrom:
    :type dateFrom: datetime | None
    :param dateTo:
    :type dateTo: datetime | None
    :returns: List[CalculationListElement]
    :rtype: List[CalculationListElement]
    """
    path = "/api/FKCalculations/Filter/Obligation/AfterMaturityTerm"
    params = dict()
    data = None
    params["contractorPosition"] = contractorPosition

    if dateFrom is not None:
        params["dateFrom"] = dateFrom

    if dateTo is not None:
        params["dateTo"] = dateTo

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[CalculationListElement])
    return result


async def GetObligationAfterMaturityTermByEmployee(
    api: AsyncAPI, dateFrom: Optional[datetime], dateTo: Optional[datetime], employeePosition: int
) -> IHttpActionResult[List[CalculationListElement]]:
    """
    ['List[CalculationListElement]']
    :param api:
    :type api: AsyncAPI
    :param dateFrom:
    :type dateFrom: datetime | None
    :param dateTo:
    :type dateTo: datetime | None
    :param employeePosition:
    :type employeePosition: int
    :returns: List[CalculationListElement]
    :rtype: List[CalculationListElement]
    """
    path = "/api/FKCalculations/Filter/Obligation/AfterMaturityTerm"
    params = dict()
    data = None
    if dateFrom is not None:
        params["dateFrom"] = dateFrom

    if dateTo is not None:
        params["dateTo"] = dateTo

    params["employeePosition"] = employeePosition

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[CalculationListElement])
    return result


async def GetObligationAfterMaturityTermGroupedBySubject(
    api: AsyncAPI, dateFrom: Optional[datetime], dateTo: Optional[datetime]
) -> IHttpActionResult[List[CalculationListElementGrouped]]:
    """
    ['List[CalculationListElementGrouped]']
    :param api:
    :type api: AsyncAPI
    :param dateFrom:
    :type dateFrom: datetime | None
    :param dateTo:
    :type dateTo: datetime | None
    :returns: List[CalculationListElementGrouped]
    :rtype: List[CalculationListElementGrouped]
    """
    path = "/api/FKCalculations/Grouped/Obligation/AfterMaturityTerm"
    params = dict()
    data = None
    if dateFrom is not None:
        params["dateFrom"] = dateFrom

    if dateTo is not None:
        params["dateTo"] = dateTo

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[CalculationListElementGrouped])
    return result


async def GetObligationBeforeMaturityTermByContractor(
    api: AsyncAPI, contractorPosition: int, dateFrom: Optional[datetime], dateTo: Optional[datetime]
) -> IHttpActionResult[List[CalculationListElement]]:
    """
    ['List[CalculationListElement]']
    :param api:
    :type api: AsyncAPI
    :param contractorPosition:
    :type contractorPosition: int
    :param dateFrom:
    :type dateFrom: datetime | None
    :param dateTo:
    :type dateTo: datetime | None
    :returns: List[CalculationListElement]
    :rtype: List[CalculationListElement]
    """
    path = "/api/FKCalculations/Filter/Obligation/BeforeMaturityTerm"
    params = dict()
    data = None
    params["contractorPosition"] = contractorPosition

    if dateFrom is not None:
        params["dateFrom"] = dateFrom

    if dateTo is not None:
        params["dateTo"] = dateTo

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[CalculationListElement])
    return result


async def GetObligationBeforeMaturityTermByEmployee(
    api: AsyncAPI, dateFrom: Optional[datetime], dateTo: Optional[datetime], employeePosition: int
) -> IHttpActionResult[List[CalculationListElement]]:
    """
    ['List[CalculationListElement]']
    :param api:
    :type api: AsyncAPI
    :param dateFrom:
    :type dateFrom: datetime | None
    :param dateTo:
    :type dateTo: datetime | None
    :param employeePosition:
    :type employeePosition: int
    :returns: List[CalculationListElement]
    :rtype: List[CalculationListElement]
    """
    path = "/api/FKCalculations/Filter/Obligation/BeforeMaturityTerm"
    params = dict()
    data = None
    if dateFrom is not None:
        params["dateFrom"] = dateFrom

    if dateTo is not None:
        params["dateTo"] = dateTo

    params["employeePosition"] = employeePosition

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[CalculationListElement])
    return result


async def GetObligationBeforeMaturityTermGroupedBySubject(
    api: AsyncAPI, dateFrom: Optional[datetime], dateTo: Optional[datetime]
) -> IHttpActionResult[List[CalculationListElementGrouped]]:
    """
    ['List[CalculationListElementGrouped]']
    :param api:
    :type api: AsyncAPI
    :param dateFrom:
    :type dateFrom: datetime | None
    :param dateTo:
    :type dateTo: datetime | None
    :returns: List[CalculationListElementGrouped]
    :rtype: List[CalculationListElementGrouped]
    """
    path = "/api/FKCalculations/Grouped/Obligation/BeforeMaturityTerm"
    params = dict()
    data = None
    if dateFrom is not None:
        params["dateFrom"] = dateFrom

    if dateTo is not None:
        params["dateTo"] = dateTo

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[CalculationListElementGrouped])
    return result


async def GetObligationByContractor(
    api: AsyncAPI, contractorPosition: int, dateFrom: Optional[datetime], dateTo: Optional[datetime]
) -> IHttpActionResult[List[CalculationListElement]]:
    """
    ['List[CalculationListElement]']
    :param api:
    :type api: AsyncAPI
    :param contractorPosition:
    :type contractorPosition: int
    :param dateFrom:
    :type dateFrom: datetime | None
    :param dateTo:
    :type dateTo: datetime | None
    :returns: List[CalculationListElement]
    :rtype: List[CalculationListElement]
    """
    path = "/api/FKCalculations/Filter/Obligation"
    params = dict()
    data = None
    params["contractorPosition"] = contractorPosition

    if dateFrom is not None:
        params["dateFrom"] = dateFrom

    if dateTo is not None:
        params["dateTo"] = dateTo

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[CalculationListElement])
    return result


async def GetObligationByEmployee(
    api: AsyncAPI, dateFrom: Optional[datetime], dateTo: Optional[datetime], employeePosition: int
) -> IHttpActionResult[List[CalculationListElement]]:
    """
    ['List[CalculationListElement]']
    :param api:
    :type api: AsyncAPI
    :param dateFrom:
    :type dateFrom: datetime | None
    :param dateTo:
    :type dateTo: datetime | None
    :param employeePosition:
    :type employeePosition: int
    :returns: List[CalculationListElement]
    :rtype: List[CalculationListElement]
    """
    path = "/api/FKCalculations/Filter/Obligation"
    params = dict()
    data = None
    if dateFrom is not None:
        params["dateFrom"] = dateFrom

    if dateTo is not None:
        params["dateTo"] = dateTo

    params["employeePosition"] = employeePosition

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[CalculationListElement])
    return result


async def GetObligationGroupedBySubject(
    api: AsyncAPI, dateFrom: Optional[datetime], dateTo: Optional[datetime]
) -> IHttpActionResult[List[CalculationListElementGrouped]]:
    """
    ['List[CalculationListElementGrouped]']
    :param api:
    :type api: AsyncAPI
    :param dateFrom:
    :type dateFrom: datetime | None
    :param dateTo:
    :type dateTo: datetime | None
    :returns: List[CalculationListElementGrouped]
    :rtype: List[CalculationListElementGrouped]
    """
    path = "/api/FKCalculations/Grouped/Obligation"
    params = dict()
    data = None
    if dateFrom is not None:
        params["dateFrom"] = dateFrom

    if dateTo is not None:
        params["dateTo"] = dateTo

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[CalculationListElementGrouped])
    return result


async def GetObligationNotSettledByContractor(
    api: AsyncAPI, contractorPosition: int, dateFrom: Optional[datetime], dateTo: Optional[datetime]
) -> IHttpActionResult[List[CalculationListElement]]:
    """
    ['List[CalculationListElement]']
    :param api:
    :type api: AsyncAPI
    :param contractorPosition:
    :type contractorPosition: int
    :param dateFrom:
    :type dateFrom: datetime | None
    :param dateTo:
    :type dateTo: datetime | None
    :returns: List[CalculationListElement]
    :rtype: List[CalculationListElement]
    """
    path = "/api/FKCalculations/Filter/Obligation/NotSettled"
    params = dict()
    data = None
    params["contractorPosition"] = contractorPosition

    if dateFrom is not None:
        params["dateFrom"] = dateFrom

    if dateTo is not None:
        params["dateTo"] = dateTo

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[CalculationListElement])
    return result


async def GetObligationNotSettledByEmployee(
    api: AsyncAPI, dateFrom: Optional[datetime], dateTo: Optional[datetime], employeePosition: int
) -> IHttpActionResult[List[CalculationListElement]]:
    """
    ['List[CalculationListElement]']
    :param api:
    :type api: AsyncAPI
    :param dateFrom:
    :type dateFrom: datetime | None
    :param dateTo:
    :type dateTo: datetime | None
    :param employeePosition:
    :type employeePosition: int
    :returns: List[CalculationListElement]
    :rtype: List[CalculationListElement]
    """
    path = "/api/FKCalculations/Filter/Obligation/NotSettled"
    params = dict()
    data = None
    if dateFrom is not None:
        params["dateFrom"] = dateFrom

    if dateTo is not None:
        params["dateTo"] = dateTo

    params["employeePosition"] = employeePosition

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[CalculationListElement])
    return result


async def GetObligationNotSettledGroupedBySubject(
    api: AsyncAPI, dateFrom: Optional[datetime], dateTo: Optional[datetime]
) -> IHttpActionResult[List[CalculationListElementGrouped]]:
    """
    ['List[CalculationListElementGrouped]']
    :param api:
    :type api: AsyncAPI
    :param dateFrom:
    :type dateFrom: datetime | None
    :param dateTo:
    :type dateTo: datetime | None
    :returns: List[CalculationListElementGrouped]
    :rtype: List[CalculationListElementGrouped]
    """
    path = "/api/FKCalculations/Grouped/Obligation/NotSettled"
    params = dict()
    data = None
    if dateFrom is not None:
        params["dateFrom"] = dateFrom

    if dateTo is not None:
        params["dateTo"] = dateTo

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[CalculationListElementGrouped])
    return result
