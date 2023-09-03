from .....Client import (
    AsyncAPI,
    ClientResponse,
    IHttpActionResult,
)
from .....Constants import (
    Unset,
)
from ....Common.ViewModels import (
    Catalog,
    Kind,
    Marker,
)
from ....Enums import (
    enumOrderByType,
)
from ....ViewModels import (
    Page,
)
from ...ViewModels import (
    Product,
    ProductBarcodes,
    ProductFilterCriteria,
    ProductListElement,
    ProductListElementWithDimensions,
    ProductListElementWithSalePrices,
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
    api: AsyncAPI, product: Product
) -> IHttpActionResult[Product]:
    """
    ['Product']
    :param api:
    :type api: AsyncAPI
    :param product:
    :type product: Product
    :returns: Product
    :rtype: Product
    """
    path = "/api/Products/Create"
    params = dict()
    data = product.model_dump_json(exclude_unset=True)
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="POST", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, Product)
    return result


async def Filter(
    api: AsyncAPI, criteria: ProductFilterCriteria, salePrices: bool
) -> Union[IHttpActionResult[List[ProductListElement]], IHttpActionResult[List[ProductListElementWithSalePrices]]]:
    """
    ['List[ProductListElement]', 'List[ProductListElementWithSalePrices]']
    :param api:
    :type api: AsyncAPI
    :param criteria:
    :type criteria: ProductFilterCriteria
    :param salePrices:
    :type salePrices: bool
    :returns: List[ProductListElement], List[ProductListElementWithSalePrices]
    :rtype: List[ProductListElement] | List[ProductListElementWithSalePrices]
    """
    path = "/api/Products/Filter"
    params = dict()
    data = criteria.model_dump_json(exclude_unset=True)
    params["salePrices"] = salePrices

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="PATCH", path=path, params=params, headers=headers, data=data)
    # todo: many returns List[ProductListElement]List[ProductListElementWithSalePrices]
    result = await IHttpActionResult.create(response, None)
    return result


async def FilterWithDimensions(
    api: AsyncAPI, criteria: ProductFilterCriteria
) -> IHttpActionResult[List[ProductListElementWithDimensions]]:
    """
    ['List[ProductListElementWithDimensions]']
    :param api:
    :type api: AsyncAPI
    :param criteria:
    :type criteria: ProductFilterCriteria
    :returns: List[ProductListElementWithDimensions]
    :rtype: List[ProductListElementWithDimensions]
    """
    path = "/api/Products/Filter/WithDimensions"
    params = dict()
    data = criteria.model_dump_json(exclude_unset=True)
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="PATCH", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[ProductListElementWithDimensions])
    return result


async def FilterWithSalePrices(
    api: AsyncAPI, criteria: ProductFilterCriteria
) -> IHttpActionResult[List[ProductListElementWithSalePrices]]:
    """
    ['List[ProductListElementWithSalePrices]']
    :param api:
    :type api: AsyncAPI
    :param criteria:
    :type criteria: ProductFilterCriteria
    :returns: List[ProductListElementWithSalePrices]
    :rtype: List[ProductListElementWithSalePrices]
    """
    path = "/api/Products/Filter/WithSalePrices"
    params = dict()
    data = criteria.model_dump_json(exclude_unset=True)
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="PATCH", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[ProductListElementWithSalePrices])
    return result


Get_T = TypeVar('Get_T', IHttpActionResult[Product], IHttpActionResult[List[ProductListElement]])


@overload
async def Get(
    api: AsyncAPI, code: str
) -> IHttpActionResult[Product]: ...


@overload
async def Get(
    api: AsyncAPI, id: int
) -> IHttpActionResult[Product]: ...


@overload
async def Get(
    api: AsyncAPI, 
) -> IHttpActionResult[List[ProductListElement]]: ...


async def Get(
    api: AsyncAPI,
    code: str = Unset(),
    id: int = Unset()
) -> Get_T:
    match code, id:
        case str(), Unset():
            path = "/api/Products"
            params = dict()
            data = None
            params["code"] = code
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, Product)
            return result
        case Unset(), int():
            path = "/api/Products"
            params = dict()
            data = None
            params["id"] = id
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, Product)
            return result
        case Unset(), Unset():
            path = "/api/Products"
            params = dict()
            data = None
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[ProductListElement])
            return result


async def GetBarcodes(
    api: AsyncAPI,
    productCode: str = Unset(),
    productId: int = Unset()
) -> IHttpActionResult[ProductBarcodes]:
    match productCode, productId:
        case Unset(), int():
            path = "/api/Products/Barcodes"
            params = dict()
            data = None
            params["productId"] = productId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, ProductBarcodes)
            return result
        case str(), Unset():
            path = "/api/Products/Barcodes"
            params = dict()
            data = None
            params["productCode"] = productCode
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, ProductBarcodes)
            return result


async def GetCatalogs(
    api: AsyncAPI, 
) -> IHttpActionResult[List[Catalog]]:
    """
    ['List[Catalog]']
    :param api:
    :type api: AsyncAPI
    :returns: List[Catalog]
    :rtype: List[Catalog]
    """
    path = "/api/Products/Catalogs"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[Catalog])
    return result


async def GetKinds(
    api: AsyncAPI, 
) -> IHttpActionResult[List[Kind]]:
    """
    ['List[Kind]']
    :param api:
    :type api: AsyncAPI
    :returns: List[Kind]
    :rtype: List[Kind]
    """
    path = "/api/Products/Kinds"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[Kind])
    return result


async def GetMarkers(
    api: AsyncAPI, 
) -> IHttpActionResult[List[Marker]]:
    """
    ['List[Marker]']
    :param api:
    :type api: AsyncAPI
    :returns: List[Marker]
    :rtype: List[Marker]
    """
    path = "/api/Products/Markers"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[Marker])
    return result


async def GetPageWithDimensions(
    api: AsyncAPI, orderBy: enumOrderByType, page: int, size: int
) -> IHttpActionResult[Page[ProductListElementWithDimensions]]:
    """
    ['Page[ProductListElementWithDimensions]']
    :param api:
    :type api: AsyncAPI
    :param orderBy:
    :type orderBy: enumOrderByType
    :param page:
    :type page: int
    :param size:
    :type size: int
    :returns: Page[ProductListElementWithDimensions]
    :rtype: Page[ProductListElementWithDimensions]
    """
    path = "/api/Products/PageWithDimensions"
    params = dict()
    data = None
    params["orderBy"] = orderBy

    params["page"] = page

    params["size"] = size

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, Page[ProductListElementWithDimensions])
    return result


async def GetPageWithSalePrices(
    api: AsyncAPI, orderBy: enumOrderByType, page: int, size: int
) -> IHttpActionResult[Page[ProductListElementWithSalePrices]]:
    """
    ['Page[ProductListElementWithSalePrices]']
    :param api:
    :type api: AsyncAPI
    :param orderBy:
    :type orderBy: enumOrderByType
    :param page:
    :type page: int
    :param size:
    :type size: int
    :returns: Page[ProductListElementWithSalePrices]
    :rtype: Page[ProductListElementWithSalePrices]
    """
    path = "/api/Products/PageWithSalePrices"
    params = dict()
    data = None
    params["orderBy"] = orderBy

    params["page"] = page

    params["size"] = size

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, Page[ProductListElementWithSalePrices])
    return result


async def GetPagedDocument(
    api: AsyncAPI, orderBy: enumOrderByType, page: int, size: int
) -> IHttpActionResult[Page[ProductListElement]]:
    """
    ['Page[ProductListElement]']
    :param api:
    :type api: AsyncAPI
    :param orderBy:
    :type orderBy: enumOrderByType
    :param page:
    :type page: int
    :param size:
    :type size: int
    :returns: Page[ProductListElement]
    :rtype: Page[ProductListElement]
    """
    path = "/api/Products/Page"
    params = dict()
    data = None
    params["orderBy"] = orderBy

    params["page"] = page

    params["size"] = size

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, Page[ProductListElement])
    return result


async def GetWithDimensions(
    api: AsyncAPI, 
) -> IHttpActionResult[List[ProductListElementWithDimensions]]:
    """
    ['List[ProductListElementWithDimensions]']
    :param api:
    :type api: AsyncAPI
    :returns: List[ProductListElementWithDimensions]
    :rtype: List[ProductListElementWithDimensions]
    """
    path = "/api/Products/WithDimensions"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[ProductListElementWithDimensions])
    return result


async def GetWithSalePrices(
    api: AsyncAPI, 
) -> IHttpActionResult[List[ProductListElementWithSalePrices]]:
    """
    ['List[ProductListElementWithSalePrices]']
    :param api:
    :type api: AsyncAPI
    :returns: List[ProductListElementWithSalePrices]
    :rtype: List[ProductListElementWithSalePrices]
    """
    path = "/api/Products/WithSalePrices"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[ProductListElementWithSalePrices])
    return result


async def IncrementalSync(
    api: AsyncAPI, dateFrom: datetime
) -> IHttpActionResult[None]:
    """
    []
    :param api:
    :type api: AsyncAPI
    :param dateFrom:
    :type dateFrom: datetime
    :returns: 
    :rtype: 
    """
    path = "/api/Products/IncrementalSync"
    params = dict()
    data = None
    params["dateFrom"] = dateFrom

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    # no return
    result = await IHttpActionResult.create(response, None)
    return result


async def Update(
    api: AsyncAPI, product: Product
) -> IHttpActionResult[None]:
    """
    []
    :param api:
    :type api: AsyncAPI
    :param product:
    :type product: Product
    :returns: 
    :rtype: 
    """
    path = "/api/Products/Update"
    params = dict()
    data = product.model_dump_json(exclude_unset=True)
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
    # no return
    result = await IHttpActionResult.create(response, None)
    return result
