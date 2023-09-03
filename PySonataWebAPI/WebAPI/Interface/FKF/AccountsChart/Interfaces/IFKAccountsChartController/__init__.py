from ......Client import (
    AsyncAPI,
    ClientResponse,
    IHttpActionResult,
)
from ......Constants import (
    Unset,
)
from ...ViewModels import (
    AccountChartElement,
    AccountChartElementSimple,
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


async def GetFlatList(
    api: AsyncAPI, yearId: int
) -> IHttpActionResult[List[AccountChartElementSimple]]:
    """
    ['List[AccountChartElementSimple]']
    :param api:
    :type api: AsyncAPI
    :param yearId:
    :type yearId: int
    :returns: List[AccountChartElementSimple]
    :rtype: List[AccountChartElementSimple]
    """
    path = "/api/FKAccountsChart/FlatList"
    params = dict()
    data = None
    params["yearId"] = yearId

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[AccountChartElementSimple])
    return result


async def GetTreeList(
    api: AsyncAPI, yearId: int
) -> IHttpActionResult[List[AccountChartElement]]:
    """
    ['List[AccountChartElement]']
    :param api:
    :type api: AsyncAPI
    :param yearId:
    :type yearId: int
    :returns: List[AccountChartElement]
    :rtype: List[AccountChartElement]
    """
    path = "/api/FKAccountsChart/FlatList"
    params = dict()
    data = None
    params["yearId"] = yearId

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[AccountChartElement])
    return result
