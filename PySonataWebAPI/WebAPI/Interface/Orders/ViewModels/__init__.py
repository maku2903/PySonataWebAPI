from ...Common.ViewModels import (
    PaymentRegistryBase,
    RelatedDocumentPosition,
    VatRateBase,
)
from ...Enums import (
    enumCancelationType,
    enumDocumentReservationType,
    enumDocumentStatus,
    enumManualSettledState,
    enumPriceKind,
    enumRDFStatus,
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
class OrderIssueDelivery(BaseModel):
    Code: str
    Quantity: Decimal
    Id: Optional[int]
class OrderPosition(BaseModel):
    ProductId: Optional[int]
    EnteredQuantity: Decimal
    Description: str
    WrittenQuantity: Decimal
    No: int
    SetHeaderId: Optional[int]
    NetValue: Decimal
    VatRate: "VatRateBase"
    VatValuePLN: Decimal
    Id: int
    UnitOfMeasurement: str
    PriceKind: "enumPriceKind"
    NetValuePLN: Decimal
    PriceValue: Decimal
    GrossValue: Decimal
    EnteredUnitOfMeasurement: str
    SalePriceType: "enumSalePriceType"
    Quantity: Decimal
    PriceValuePLN: Decimal
    WrittenUnitOfMeasurement: str
    ProductCode: str
class OrderWZ(BaseModel):
    Id: int
    DocumentNumber: str
    IssueDate: Optional[datetime]
    OperationDate: Optional[datetime]
    RecipientId: int
class OrderIssueCatalog(BaseModel):
    AddIfNotExist: bool
    FullPath: str
class OrderStatus(BaseModel):
    DocumentStatusText: str
    RDFStatus: "enumRDFStatus"
    Id: int
    Buffer: bool
    WarehouseSettled: int
    DocumentNumber: str
    PaymentSettled: int
    ManualSettled: "enumManualSettledState"
    DocumentStatus: "enumDocumentStatus"
class OrderIssuePositionElement(BaseModel):
    Code: str
    Name: str
    Quantity: Decimal
    Value: Decimal
    Deliveries: List["OrderIssueDelivery"]
    UnitOfMeasurement: str
class OrderIssueContractorData(BaseModel):
    City: str
    NIP: str
    PostCode: str
    Country: str
    Street: str
    Name: str
    HouseNo: str
    ApartmentNo: str
class OrderIssueContractor(BaseModel):
    DeliveryAddressCode: str
    RecalculatePrices: bool
    Data: "OrderIssueContractorData"
    Code: str
    Id: Optional[int]
class OrderIssueKind(BaseModel):
    AddIfNotExist: bool
    Code: str
class OrderIssuePosition(OrderIssuePositionElement):
    VatRate: "VatRateBase"
    Elements: List["OrderIssuePositionElement"]
class OrderBase(BaseModel):
    NumberInSeries: Optional[int]
    Buyer: "OrderIssueContractor"
    Department: str
    Catalog: "OrderIssueCatalog"
    PriceKind: "enumPriceKind"
    Series: str
    PaymentRegistry: "PaymentRegistryBase"
    Note: str
    Currency: str
    ReceivedBy: str
    Description: str
    MaturityDate: Optional[datetime]
    PaymentFormId: int
    SaleDate: Optional[datetime]
    CurrencyRate: Decimal
    ReservationType: "enumDocumentReservationType"
    SalePriceType: "enumSalePriceType"
    SplitPayment: bool
    Recipient: "OrderIssueContractor"
    IssueDate: Optional[datetime]
    Kind: "OrderIssueKind"
    Marker: int
    TypeCode: str
class OrderIssue(OrderBase):
    Positions: List["OrderIssuePosition"]
class OrderFV(BaseModel):
    BuyerId: int
    RecipientId: int
    IssueDate: Optional[datetime]
    SaleDate: Optional[datetime]
    Id: int
    DocumentNumber: str
class OrderPositionRelation(BaseModel):
    OrderNumber: str
    Description: str
    OrderId: int
    ProductCode: str
    RelatedFV: List["RelatedDocumentPosition"]
    ProductId: Optional[int]
    RelatedWZ: List["RelatedDocumentPosition"]
    Id: int
    NetValuePLN: Decimal
    Quantity: Decimal
    No: int
class OrderEditPosition(OrderIssuePosition, OrderIssuePositionElement):
    PositionId: Optional[int]
    Delete: bool
class Order(BaseModel):
    ReceivedBy: str
    CurrencyRate: Decimal
    NetValue: Decimal
    Buffer: bool
    VatValuePLN: Decimal
    Note: str
    RecipientId: Optional[int]
    BuyerAddressId: Optional[int]
    Description: str
    GrossValue: Decimal
    Marker: int
    TypeCode: str
    Active: bool
    Id: int
    DocumentNumber: str
    BuyerId: Optional[int]
    Positions: List["OrderPosition"]
    SplitPayment: bool
    DepartmentId: int
    IssuerId: int
    NumberInSeries: int
    PriceKind: "enumPriceKind"
    RecipientAddressId: Optional[int]
    SaleDate: Optional[datetime]
    SalePriceType: "enumSalePriceType"
    MaturityDate: Optional[datetime]
    Canceled: "enumCancelationType"
    Settled: bool
    IssueDate: Optional[datetime]
    NetValuePLN: Decimal
    Series: str
    KindId: int
    PaymentFormId: int
    PaymentRegistryId: int
    Currency: str
    CatalogId: int
class OrderEdit(OrderBase):
    Positions: List["OrderEditPosition"]
    Id: int
class OrderListElement(BaseModel):
    IssueDate: Optional[datetime]
    NetValuePLN: Decimal
    Settled: bool
    TypeCode: str
    NumberInSeries: int
    Description: str
    MaturityDate: Optional[datetime]
    GrossValue: Decimal
    DepartmentId: int
    Canceled: "enumCancelationType"
    BuyerId: Optional[int]
    Currency: str
    Active: bool
    IssuerId: int
    Series: str
    Id: int
    NetValue: Decimal
    SaleDate: Optional[datetime]
    Buffer: bool
    RecipientId: Optional[int]
    VatValuePLN: Decimal
    DocumentNumber: str
