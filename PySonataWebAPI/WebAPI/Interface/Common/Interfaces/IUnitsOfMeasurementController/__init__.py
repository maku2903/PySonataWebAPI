from .....Client import (
    AsyncAPI,
    ClientResponse,
    IHttpActionResult,
)
from .....Constants import (
    Unset,
)
from ...ViewModels import (
    UnitOfMeasurement,
    UnitOfMeasurementDefinition,
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
) -> IHttpActionResult[List[UnitOfMeasurement]]:
    """
    ['List[UnitOfMeasurement]']
    :param api:
    :type api: AsyncAPI
    :returns: List[UnitOfMeasurement]
    :rtype: List[UnitOfMeasurement]
    """
    path = "/api/UnitsOfMeasurement"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[UnitOfMeasurement])
    return result


async def GetDefinition(
    api: AsyncAPI, 
) -> IHttpActionResult[List[UnitOfMeasurementDefinition]]:
    """
    ['List[UnitOfMeasurementDefinition]']
    :param api:
    :type api: AsyncAPI
    :returns: List[UnitOfMeasurementDefinition]
    :rtype: List[UnitOfMeasurementDefinition]
    """
    path = "/api/UnitsOfMeasurement/Definition"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[UnitOfMeasurementDefinition])
    return result
