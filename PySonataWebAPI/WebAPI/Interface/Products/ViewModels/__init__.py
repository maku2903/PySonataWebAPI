from ...Common.ViewModels import (
    Catalog,
    Dimension,
    FilterDimensionCriteria,
    Kind,
    VatRateBase,
)
from ...Common.ViewModels.CriteriaFilter import (
    IntCriteriaFilter,
    StringCriteriaFilter,
)
from ...Enums import (
    enumDefaultUnitOfMeasurementKind,
    enumFilterCriteriaMode,
    enumJPK_V7ProductGroup,
    enumPriceParameter,
    enumPriceRecalculateType,
    enumPriceRounding,
    enumProductType,
    enumSettlementMethod,
)
from .Prices import (
    ProductBasePrice,
    ProductListElementSalePrice,
    ProductPrice,
    ProductSalePrice,
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
from uuid import (
    UUID,
)
class ProductFK(BaseModel):
    IdFK: str
    ParameterFK: str
class ProductLogisticField(BaseModel):
    UnitTypeName: str
    Name: str
    Value: Optional[Decimal]
    Unit: str
class ProductBarcode(BaseModel):
    UnitOfMeasurementGuid: Optional[UUID]
    UnitOfMeasurement: str
    Barcode: Optional[str]
    UnitName: str
class ProductIntrastat(BaseModel):
    RatioOfWeight: Decimal
    ComplementaryUM: str
    RatioOfComplementaryUM: Decimal
    UseComplementaryUM: bool
class ProductUnitsOfMeasurement(BaseModel):
    DisplayUM: str
    AdditionalUM1: str
    RecordUM: str
    AdditionalUM2: str
    RatioOfAdditionalUM2: Decimal
    DefaultUMKind: "enumDefaultUnitOfMeasurementKind"
    RatioOfDefaultUM: Decimal
    DefaultUM: str
    RatioOfAdditionalUM1: Decimal
class ProductSetElement(BaseModel):
    DisplayUM: str
    DisplayQuantity: Decimal
    Name: str
    Id: int
    Quantity: Decimal
    Code: str
class Product(BaseModel):
    CalcOther: "ProductPrice"
    Name: str
    CNFull: str
    CollationSetMode: bool
    PriceSetMode: bool
    CalcDuty: "ProductPrice"
    CurrencyConversion: int
    PriceNegotiation: bool
    SettlementMethod: Optional["enumSettlementMethod"]
    VatRate: "VatRateBase"
    Id: Optional[int]
    Barcode: str
    MinState: Decimal
    SplitPayment: bool
    FiscalName: str
    LogisticFields: List["ProductLogisticField"]
    SalePrices: List["ProductSalePrice"]
    Code: str
    Catalog: "Catalog"
    Barcodes: List["ProductBarcode"]
    Dimensions: List["Dimension"]
    Kind: "Kind"
    CN: str
    SalePriceRecalculate: bool
    ReverseCharge: bool
    StaticSet: bool
    VAT50Minus: bool
    Intrastat: "ProductIntrastat"
    CurrencyMode: bool
    PurchasePriceInCurrency: "ProductPrice"
    Marker: int
    MaxState: Decimal
    CurrencyRateDate: datetime
    Type: "enumProductType"
    Active: bool
    AgriculturalPromotionFund: str
    PriceRounding: Optional["enumPriceRounding"]
    PriceRecalculateType: Optional["enumPriceRecalculateType"]
    PurchasePrice: "ProductPrice"
    JPK_V7ProductGroup: Optional["enumJPK_V7ProductGroup"]
    UnitsOfMeasurement: "ProductUnitsOfMeasurement"
    CurrencyRateWithoutConversion: Decimal
    SetElements: Optional[List["ProductSetElement"]]
    Note: str
    CalcExcise: "ProductPrice"
    PriceParameter: Optional["enumPriceParameter"]
    DeliveryScheme: str
    CurrencyRate: Decimal
    FK: "ProductFK"
    BasePrice: "ProductBasePrice"
    PKWiU: str
class ProductListElement(BaseModel):
    DefaultUnit: str
    VatRate: Optional[str]
    Barcode: str
    FiscalName: str
    Code: str
    Type: Optional["enumProductType"]
    Unit: str
    CN: str
    Active: bool
    Id: int
    PKWiU: str
    Name: str
class ProductBarcodes(BaseModel):
    Barcodes: List["ProductBarcode"]
    Code: str
    Id: int
class ProductListElementWithDimensions(ProductListElement):
    Dimensions: List["Dimension"]
class ProductListElementWithSalePrices(ProductListElement):
    SalePrices: List["ProductListElementSalePrice"]
class ProductFilterCriteria(BaseModel):
    Marker_To: int
    Marker_Mode: Optional["enumFilterCriteriaMode"]
    Marker_From: int
    CN_Mode: Optional["enumFilterCriteriaMode"]
    FiscalName_From: str
    Name_From: str
    Name_Mode: Optional["enumFilterCriteriaMode"]
    Code_To: str
    Name_To: str
    Barcode_To: str
    CN_To: int
    Dimensions: List["FilterDimensionCriteria"]
    Code_From: str
    Active: Optional[bool]
    Barcode_Mode: Optional["enumFilterCriteriaMode"]
    Barcode_From: str
    Code_Mode: Optional["enumFilterCriteriaMode"]
    FiscalName_To: str
    FiscalName_Mode: Optional["enumFilterCriteriaMode"]
    CN_From: int
class ProductCriteriaFilter(BaseModel):
    Name: "StringCriteriaFilter"
    CN: "StringCriteriaFilter"
    Code: "StringCriteriaFilter"
    FiscalName: "StringCriteriaFilter"
    Type: Optional["enumProductType"]
    KindId: Optional[int]
    Marker: "IntCriteriaFilter"
    CatalogId: Optional[int]
    Active: Optional[bool]
    Barcode: "StringCriteriaFilter"
