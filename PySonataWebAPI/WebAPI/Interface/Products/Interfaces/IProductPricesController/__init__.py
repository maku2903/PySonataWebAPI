from .....Client import (
    AsyncAPI,
    ClientResponse,
    IHttpActionResult,
)
from .....Constants import (
    Unset,
)
from ...ViewModels.PriceCalculations import (
    PriceCalculationCriteria,
    PriceCalculationResult,
    PriceOrderCriteria,
    PriceOrderResult,
)
from ...ViewModels.Prices import (
    IndividualDiscount,
    IndividualDiscountListElement,
    PriceFactor,
    PriceFactorCriteria,
    ProductPriceListElement,
    ProductPricesEdit,
    ProductSalePriceBase,
    QuantitativeDiscount,
    QuantitativeDiscountListElement,
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


async def CalculatePrices(
    api: AsyncAPI, criteria: PriceCalculationCriteria
) -> IHttpActionResult[PriceCalculationResult]:
    """
    ['PriceCalculationResult']
    :param api:
    :type api: AsyncAPI
    :param criteria:
    :type criteria: PriceCalculationCriteria
    :returns: PriceCalculationResult
    :rtype: PriceCalculationResult
    """
    path = "/api/ProductPrices/CalculatePrices"
    params = dict()
    data = criteria.model_dump_json(exclude_unset=True)
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="PATCH", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, PriceCalculationResult)
    return result


async def GetIndividualDiscounts(
    api: AsyncAPI, 
) -> IHttpActionResult[List[IndividualDiscountListElement]]:
    """
    ['List[IndividualDiscountListElement]']
    :param api:
    :type api: AsyncAPI
    :returns: List[IndividualDiscountListElement]
    :rtype: List[IndividualDiscountListElement]
    """
    path = "/api/ProductPrices/IndividualDiscounts"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[IndividualDiscountListElement])
    return result


async def GetIndividualDiscountsByContractor(
    api: AsyncAPI,
    contractorCode: str = Unset(),
    contractorId: int = Unset()
) -> IHttpActionResult[List[IndividualDiscount]]:
    match contractorCode, contractorId:
        case Unset(), int():
            path = "/api/ProductPrices/IndividualDiscounts"
            params = dict()
            data = None
            params["contractorId"] = contractorId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[IndividualDiscount])
            return result
        case str(), Unset():
            path = "/api/ProductPrices/IndividualDiscounts"
            params = dict()
            data = None
            params["contractorCode"] = contractorCode
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[IndividualDiscount])
            return result


async def GetIndividualDiscountsByContractorKind(
    api: AsyncAPI, contractorKindId: int
) -> IHttpActionResult[List[IndividualDiscount]]:
    """
    ['List[IndividualDiscount]']
    :param api:
    :type api: AsyncAPI
    :param contractorKindId:
    :type contractorKindId: int
    :returns: List[IndividualDiscount]
    :rtype: List[IndividualDiscount]
    """
    path = "/api/ProductPrices/IndividualDiscounts"
    params = dict()
    data = None
    params["contractorKindId"] = contractorKindId

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[IndividualDiscount])
    return result


async def GetPriceFactors(
    api: AsyncAPI, criteria: PriceFactorCriteria
) -> IHttpActionResult[List[PriceFactor]]:
    """
    ['List[PriceFactor]']
    :param api:
    :type api: AsyncAPI
    :param criteria:
    :type criteria: PriceFactorCriteria
    :returns: List[PriceFactor]
    :rtype: List[PriceFactor]
    """
    path = "/api/ProductPrices/PriceFactors"
    params = dict()
    data = criteria.model_dump_json(exclude_unset=True)
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[PriceFactor])
    return result


async def GetQuantitativeDiscounts(
    api: AsyncAPI, 
) -> IHttpActionResult[List[QuantitativeDiscountListElement]]:
    """
    ['List[QuantitativeDiscountListElement]']
    :param api:
    :type api: AsyncAPI
    :returns: List[QuantitativeDiscountListElement]
    :rtype: List[QuantitativeDiscountListElement]
    """
    path = "/api/ProductPrices/QuantitativeDiscounts"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[QuantitativeDiscountListElement])
    return result


async def GetQuantitativeDiscountsByProduct(
    api: AsyncAPI,
    productCode: str = Unset(),
    productId: int = Unset()
) -> IHttpActionResult[List[QuantitativeDiscount]]:
    match productCode, productId:
        case str(), Unset():
            path = "/api/ProductPrices/QuantitativeDiscounts"
            params = dict()
            data = None
            params["productCode"] = productCode
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[QuantitativeDiscount])
            return result
        case Unset(), int():
            path = "/api/ProductPrices/QuantitativeDiscounts"
            params = dict()
            data = None
            params["productId"] = productId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[QuantitativeDiscount])
            return result


async def GetQuantitativeDiscountsByProductKind(
    api: AsyncAPI, productKindId: int
) -> IHttpActionResult[List[QuantitativeDiscountListElement]]:
    """
    ['List[QuantitativeDiscountListElement]']
    :param api:
    :type api: AsyncAPI
    :param productKindId:
    :type productKindId: int
    :returns: List[QuantitativeDiscountListElement]
    :rtype: List[QuantitativeDiscountListElement]
    """
    path = "/api/ProductPrices/QuantitativeDiscounts"
    params = dict()
    data = None
    params["productKindId"] = productKindId

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[QuantitativeDiscountListElement])
    return result


async def GetSalePrices(
    api: AsyncAPI, 
) -> IHttpActionResult[List[ProductPriceListElement]]:
    """
    ['List[ProductPriceListElement]']
    :param api:
    :type api: AsyncAPI
    :returns: List[ProductPriceListElement]
    :rtype: List[ProductPriceListElement]
    """
    path = "/api/ProductPrices/SalePrices"
    params = dict()
    data = None
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[ProductPriceListElement])
    return result


async def GetSalePricesByProduct(
    api: AsyncAPI,
    productCode: str = Unset(),
    productId: int = Unset()
) -> IHttpActionResult[List[ProductSalePriceBase]]:
    match productCode, productId:
        case str(), Unset():
            path = "/api/ProductPrices/SalePrices"
            params = dict()
            data = None
            params["productCode"] = productCode
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[ProductSalePriceBase])
            return result
        case Unset(), int():
            path = "/api/ProductPrices/SalePrices"
            params = dict()
            data = None
            params["productId"] = productId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
            result = await IHttpActionResult.create(response, List[ProductSalePriceBase])
            return result


async def GetSalePricesByProductKind(
    api: AsyncAPI, productKindId: int
) -> IHttpActionResult[List[ProductPriceListElement]]:
    """
    ['List[ProductPriceListElement]']
    :param api:
    :type api: AsyncAPI
    :param productKindId:
    :type productKindId: int
    :returns: List[ProductPriceListElement]
    :rtype: List[ProductPriceListElement]
    """
    path = "/api/ProductPrices/SalePrices"
    params = dict()
    data = None
    params["productKindId"] = productKindId

    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="GET", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, List[ProductPriceListElement])
    return result


async def OrderPrices(
    api: AsyncAPI, criteria: PriceOrderCriteria
) -> IHttpActionResult[PriceOrderResult]:
    """
    ['PriceOrderResult']
    :param api:
    :type api: AsyncAPI
    :param criteria:
    :type criteria: PriceOrderCriteria
    :returns: PriceOrderResult
    :rtype: PriceOrderResult
    """
    path = "/api/ProductPrices/OrderPrices"
    params = dict()
    data = criteria.model_dump_json(exclude_unset=True)
    headers = dict()
    headers["Content-Type"] = "application/json; charset=utf-8"
    response = await api.request(method="PATCH", path=path, params=params, headers=headers, data=data)
    result = await IHttpActionResult.create(response, PriceOrderResult)
    return result


async def Recalculate(
    api: AsyncAPI,
    productCode: str = Unset(),
    productId: int = Unset()
) -> IHttpActionResult[None]:
    match productCode, productId:
        case str(), Unset():
            path = "/api/ProductPrices/Recalculate"
            params = dict()
            data = None
            params["productCode"] = productCode
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PATCH", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result
        case Unset(), int():
            path = "/api/ProductPrices/Recalculate"
            params = dict()
            data = None
            params["productId"] = productId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PATCH", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result


async def Update(
    api: AsyncAPI,
    prices: ProductPricesEdit = Unset(),
    productCode: str = Unset(),
    productId: int = Unset()
) -> IHttpActionResult[None]:
    match prices, productCode, productId:
        case ProductPricesEdit(), Unset(), int():
            path = "/api/ProductPrices/Update"
            params = dict()
            data = prices.model_dump_json(exclude_unset=True)
            params["productId"] = productId
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result
        case ProductPricesEdit(), str(), Unset():
            path = "/api/ProductPrices/Update"
            params = dict()
            data = prices.model_dump_json(exclude_unset=True)
            params["productCode"] = productCode
            headers = dict()
            headers["Content-Type"] = "application/json; charset=utf-8"
            response = await api.request(method="PUT", path=path, params=params, headers=headers, data=data)
            # no return
            result = await IHttpActionResult.create(response, None)
            return result
