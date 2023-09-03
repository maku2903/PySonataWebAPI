from ....Enums import (
    enumIndividualDiscountSubjectType,
    enumPriceFactorType,
    enumPriceKind,
    enumPriceListConnectionType,
    enumPriceParameter,
    enumPriceRecalculateType,
    enumPriceType,
    enumSalePriceType,
)

from datetime import (
    datetime,
)
from decimal import (
    Decimal,
)
from enum import (
    Enum,
    auto,
)
from pydantic import (
    BaseModel,
)
from typing import (
    List,
    Optional,
)
class IndividualDiscount(BaseModel):
    Name: str
    Id: int
    Active: bool
    SubjectType: "enumIndividualDiscountSubjectType"
    Code: str
    Type: "enumPriceFactorType"
    Currency: str
    Value: Decimal
class PriceFactor(BaseModel):
    ProductId: Optional[int]
    ContractorKindId: Optional[int]
    MinimalPriority: int
    PriceType: "enumPriceType"
    Value: Decimal
    ConnectionType: List["enumPriceListConnectionType"]
    Type: "enumPriceFactorType"
    Code: str
    PriceListId: Optional[List[int]]
    TimeLimited: bool
    Currency: str
    Priority: int
    ProductKindId: Optional[int]
    DepartmentId: Optional[int]
    ContractorId: Optional[int]
class ProductPrice(BaseModel):
    Currency: str
    Value: Decimal
class ProductSalePriceBase(ProductPrice):
    ProfitPercent: Decimal
    MarkupPercent: Decimal
    PriceParameter: "enumPriceParameter"
    Type: "enumSalePriceType"
    Kind: "enumPriceKind"
    LinkedWithBasePrice: bool
class ProductBasePrice(ProductPrice):
    Date: datetime
class ProductSalePrice(ProductSalePriceBase, ProductPrice):
    AutomaticValue: bool
class ProductPricesEdit(BaseModel):
    CurrencyRateDate: datetime
    CurrencyRateWithoutConversion: Decimal
    CalcOther: "ProductPrice"
    PurchasePriceInCurrency: "ProductPrice"
    CurrencyRate: Decimal
    BasePrice: "ProductBasePrice"
    CurrencyMode: bool
    PriceRecalculateType: Optional["enumPriceRecalculateType"]
    SalePriceRecalculate: bool
    PurchasePrice: "ProductPrice"
    SalePrices: List["ProductSalePrice"]
    CalcDuty: "ProductPrice"
    CalcExcise: "ProductPrice"
    PriceParameter: Optional["enumPriceParameter"]
class PriceFactorCriteria(BaseModel):
    PriceType: "enumSalePriceType"
    DatePrice: Optional[datetime]
    DepartmentId: Optional[int]
    ProductId: Optional[int]
    ContractorKindId: Optional[int]
    Quantity: Decimal
    ContractorId: Optional[int]
    PeriodPricing: bool
    ProductKindId: Optional[int]
class ProductPriceListElement(BaseModel):
    Active: bool
    Name: str
    Code: str
    SalePrices: List["ProductSalePriceBase"]
    Id: int
class QuantitativeDiscount(BaseModel):
    QuantityTo: Optional[Decimal]
    Type: "enumPriceFactorType"
    Currency: str
    QuantityFrom: Decimal
    Value: Decimal
class QuantitativeDiscountListElement(BaseModel):
    Name: str
    Discounts: List["QuantitativeDiscount"]
    Code: str
    Id: int
    Active: bool
class ProductListElementSalePrice(BaseModel):
    Kind: "enumPriceKind"
    Currency: str
    Value: Decimal
    Type: "enumSalePriceType"
class IndividualDiscountListElement(BaseModel):
    Id: int
    IndividualDiscounts: List["IndividualDiscount"]
    Code: str
    SubjectType: "enumIndividualDiscountSubjectType"
    Active: bool
    Name: str
