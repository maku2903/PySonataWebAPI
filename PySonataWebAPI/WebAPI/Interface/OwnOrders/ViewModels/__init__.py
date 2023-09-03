from ...Common.ViewModels import (
    PaymentRegistryBase,
    RelatedDocumentPosition,
    VatRateBase,
)
from ...Enums import (
    enumCancelationType,
    enumDocumentStatus,
    enumManualSettledState,
    enumPriceKind,
    enumRDFStatus,
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
class OwnOrderIssuePositionElement(BaseModel):
    Value: Decimal
    Name: str
    Quantity: Decimal
    UnitOfMeasurement: str
    Code: str
class OwnOrderPosition(BaseModel):
    WrittenQuantity: Decimal
    Quantity: Decimal
    VatRate: "VatRateBase"
    NetValuePLN: Decimal
    VatValuePLN: Decimal
    ProductId: Optional[int]
    PriceKind: "enumPriceKind"
    Id: int
    GrossValue: Decimal
    WrittenUnitOfMeasurement: str
    Description: str
    NetValue: Decimal
    ProductCode: str
    SetHeaderId: Optional[int]
    EnteredQuantity: Decimal
    UnitOfMeasurement: str
    PriceValue: Decimal
    No: int
    PriceValuePLN: Decimal
    EnteredUnitOfMeasurement: str
class OwnOrder(BaseModel):
    Active: bool
    GrossValue: Decimal
    PaymentRegistryId: int
    Positions: List["OwnOrderPosition"]
    TypeCode: str
    NetValuePLN: Decimal
    Description: str
    ReceiveDate: Optional[datetime]
    DelivererAddressId: Optional[int]
    SellerAddressId: Optional[int]
    PriceKind: "enumPriceKind"
    IssuerId: int
    Canceled: "enumCancelationType"
    KindId: int
    VatValuePLN: Decimal
    NetValue: Decimal
    Id: int
    DocumentNumber: str
    Series: str
    Note: str
    DepartmentId: int
    Settled: bool
    Marker: int
    CurrencyRate: Decimal
    MaturityDate: Optional[datetime]
    NumberInSeries: int
    Currency: str
    Buffer: bool
    IssueDate: Optional[datetime]
    SellerId: Optional[int]
    CatalogId: int
    DelivererId: Optional[int]
    PaymentFormId: int
class OwnOrderIssueCatalog(BaseModel):
    FullPath: str
    AddIfNotExist: bool
class OwnOrderIssueKind(BaseModel):
    Code: str
    AddIfNotExist: bool
class OwnOrderIssueContractorData(BaseModel):
    PostCode: str
    Name: str
    NIP: str
    ApartmentNo: str
    HouseNo: str
    Country: str
    Street: str
    City: str
class OwnOrderIssuePosition(OwnOrderIssuePositionElement):
    VatRate: "VatRateBase"
    Elements: List["OwnOrderIssuePositionElement"]
class OwnOrderIssueContractor(BaseModel):
    Code: str
    DeliveryAddressCode: str
    Id: Optional[int]
    Data: "OwnOrderIssueContractorData"
    RecalculatePrices: bool
class OwnOrderIssue(BaseModel):
    Kind: "OwnOrderIssueKind"
    TypeCode: str
    Catalog: "OwnOrderIssueCatalog"
    Department: str
    MaturityDate: Optional[datetime]
    PaymentRegistry: "PaymentRegistryBase"
    ReceiveDate: Optional[datetime]
    IssueDate: Optional[datetime]
    Currency: str
    Positions: List["OwnOrderIssuePosition"]
    Seller: "OwnOrderIssueContractor"
    CurrencyRate: Decimal
    Deliverer: "OwnOrderIssueContractor"
    Series: str
    PaymentFormId: int
    Marker: int
    PriceKind: "enumPriceKind"
    Description: str
    Note: str
    NumberInSeries: Optional[int]
class OwnOrderPZ(BaseModel):
    IssueDate: Optional[datetime]
    DelivererId: int
    Id: int
    OperationDate: Optional[datetime]
    DocumentNumber: str
class OwnOrderPositionRelation(BaseModel):
    NetValuePLN: Decimal
    Description: str
    ProductCode: str
    OwnOrderNumber: str
    RelatedFV: List["RelatedDocumentPosition"]
    RelatedPZ: List["RelatedDocumentPosition"]
    Id: int
    No: int
    ProductId: Optional[int]
    Quantity: Decimal
    OwnOrderId: int
class OwnOrderListElement(BaseModel):
    Canceled: "enumCancelationType"
    IssuerId: int
    VatValuePLN: Decimal
    DepartmentId: int
    Active: bool
    Currency: str
    GrossValue: Decimal
    NetValuePLN: Decimal
    TypeCode: str
    MaturityDate: Optional[datetime]
    DocumentNumber: str
    ReceiveDate: Optional[datetime]
    DelivererId: Optional[int]
    IssueDate: Optional[datetime]
    NetValue: Decimal
    Series: str
    NumberInSeries: int
    Id: int
    Description: str
    SellerId: Optional[int]
    Buffer: bool
    Settled: bool
class OwnOrderStatus(BaseModel):
    PaymentSettled: int
    DocumentStatus: "enumDocumentStatus"
    DocumentNumber: str
    DocumentStatusText: str
    Id: int
    ManualSettled: "enumManualSettledState"
    Buffer: bool
    RDFStatus: "enumRDFStatus"
    WarehouseSettled: int
class OwnOrderFV(BaseModel):
    IssueDate: Optional[datetime]
    BuyDate: Optional[datetime]
    SellerId: int
    DocumentNumber: str
    DelivererId: int
    Id: int
