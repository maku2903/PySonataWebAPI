from ...Common.ViewModels import (
    PaymentRegistryBase,
    VatRateBase,
)
from ...Enums import (
    enumCancelationType,
    enumDocumentReservationType,
    enumDocumentStatus,
    enumFiscalizationStatus,
    enumJPK_V7DocumentAttribute,
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
class SaleDocumentListElement(BaseModel):
    IncomeValue: Decimal
    IssuerId: int
    BuyerId: Optional[int]
    DepartmentId: int
    Buffer: int
    NetValuePLN: Decimal
    IssueDate: Optional[datetime]
    VatValuePLN: Decimal
    Canceled: "enumCancelationType"
    Currency: str
    TypeCode: str
    NumberInSeries: int
    Settled: int
    Active: bool
    RecipientId: Optional[int]
    Id: int
    NetValue: Decimal
    SaleDate: Optional[datetime]
    Series: str
    MaturityDate: Optional[datetime]
    DocumentNumber: str
    GrossValue: Decimal
    Description: str
class AdvancePaymentOptions(BaseModel):
    IsLast: bool
    Value: Decimal
    AutomaticFillPositions: bool
class SaleDocumentIssueDelivery(BaseModel):
    Code: str
    Id: Optional[int]
    Quantity: Decimal
class SaleDocumentStatus(BaseModel):
    DocumentNumber: str
    RDFStatus: "enumRDFStatus"
    PaymentSettled: int
    Buffer: bool
    DocumentStatusText: str
    WarehouseSettled: int
    Id: int
    ManualSettled: "enumManualSettledState"
    DocumentStatus: "enumDocumentStatus"
class SaleDocumentIssueCatalog(BaseModel):
    FullPath: str
    AddIfNotExist: bool
class SaleDocumentCorrection(BaseModel):
    DocumentNumber: str
    SaleDate: Optional[datetime]
    IssueDate: Optional[datetime]
    Id: int
    No: int
class SaleDocumentWZ(BaseModel):
    Id: int
    IssueDate: Optional[datetime]
    RecipientId: int
    DocumentNumber: str
    OperationDate: Optional[datetime]
class SaleCorrectionPositionElement(BaseModel):
    PriceKind: "enumPriceKind"
    Description: str
    Quantity: Decimal
    SetHeaderId: Optional[int]
    ProductCode: str
    WrittenUnitOfMeasurement: str
    VatValuePLN: Decimal
    PriceValuePLN: Decimal
    ProductId: Optional[int]
    SalePriceType: "enumSalePriceType"
    Id: int
    VatRate: "VatRateBase"
    PriceValue: Decimal
    WrittenQuantity: Decimal
    UnitOfMeasurement: str
    NetValuePLN: Decimal
    NetValue: Decimal
    GrossValue: Decimal
class SaleCorrectionPosition(BaseModel):
    BeforeCorrection: "SaleCorrectionPositionElement"
    AfterCorrection: "SaleCorrectionPositionElement"
    No: int
class SaleCorrection(BaseModel):
    KindId: int
    NetValuePLN: Decimal
    IssuerId: int
    RecipientAddressId: Optional[int]
    Id: int
    TypeCode: str
    CorrectionReason: str
    Settled: bool
    MaturityDate: Optional[datetime]
    GrossValue: Decimal
    SaleDate: Optional[datetime]
    PaymentFormId: int
    ReceivedBy: str
    IssueDate: Optional[datetime]
    MasterDocumentOid: Optional[int]
    CurrencyRateCIT: Decimal
    PaymentRegistryId: int
    Note: str
    eInvoice: bool
    NetValue: Decimal
    Canceled: "enumCancelationType"
    Currency: str
    Series: str
    SplitPayment: bool
    JPK_V7Attributes: "enumJPK_V7DocumentAttribute"
    RecipientId: Optional[int]
    Positions: List["SaleCorrectionPosition"]
    BuyerId: Optional[int]
    Active: bool
    Buffer: bool
    CatalogId: int
    DocumentNumber: str
    SalePriceType: "enumSalePriceType"
    NumberInSeries: int
    VatValuePLN: Decimal
    Marker: int
    CurrencyRate: Decimal
    Fisacal: "enumFiscalizationStatus"
    DepartmentId: int
    BuyerAddressId: Optional[int]
    PriceKind: "enumPriceKind"
class SaleDocumentIssueContractorData(BaseModel):
    Name: str
    HouseNo: str
    NIP: str
    PostCode: str
    City: str
    Street: str
    Country: str
    ApartmentNo: str
class SaleDocumentIssueContractor(BaseModel):
    Data: "SaleDocumentIssueContractorData"
    RecalculatePrices: bool
    Code: str
    DeliveryAddressCode: str
    Id: Optional[int]
class SaleCorrectionIssuePositionElement(BaseModel):
    Quantity: Decimal
    UnitOfMeasurement: str
    Code: str
    Value: Decimal
    Name: str
class SaleDocumentIssueKind(BaseModel):
    AddIfNotExist: bool
    Code: str
class SaleCorrectionIssueContractor(BaseModel):
    Data: "SaleDocumentIssueContractorData"
    DeliveryAddressCode: str
    RecalculatePrices: bool
class SaleCorrectionIssuePosition(SaleCorrectionIssuePositionElement):
    No: Optional[int]
    Elements: List["SaleCorrectionIssuePositionElement"]
    VatRate: "VatRateBase"
class SaleCorrectionIssue(BaseModel):
    NumberInSeries: Optional[int]
    ReceivedBy: str
    Marker: int
    IssueDate: Optional[datetime]
    CorrectionReason: str
    Catalog: "SaleDocumentIssueCatalog"
    MasterDocumentId: Optional[int]
    Kind: "SaleDocumentIssueKind"
    JPK_V7Attributes: Optional["enumJPK_V7DocumentAttribute"]
    Recipient: "SaleCorrectionIssueContractor"
    TypeCode: str
    SplitPayment: bool
    Note: str
    PaymentFormId: Optional[int]
    MaturityDate: Optional[datetime]
    CurrencyRate: Optional[Decimal]
    Positions: List["SaleCorrectionIssuePosition"]
    Series: str
    MasterDocumentNumber: str
    PaymentRegistry: "PaymentRegistryBase"
    Buyer: "SaleCorrectionIssueContractor"
    SaleDate: Optional[datetime]
class SaleDocumentIssuePositionElement(BaseModel):
    Name: str
    Value: Decimal
    UnitOfMeasurement: str
    Quantity: Decimal
    Deliveries: List["SaleDocumentIssueDelivery"]
    Code: str
class SaleDocumentIssuePosition(SaleDocumentIssuePositionElement):
    Elements: List["SaleDocumentIssuePositionElement"]
    VatRate: "VatRateBase"
class SaleDocumentIssue(BaseModel):
    Description: str
    Marker: int
    MaturityDate: Optional[datetime]
    Currency: str
    Kind: "SaleDocumentIssueKind"
    SplitPayment: bool
    ReceivedBy: str
    NumberInSeries: Optional[int]
    CurrencyRateCIT: Decimal
    PaymentFormId: int
    Positions: List["SaleDocumentIssuePosition"]
    CurrencyRate: Decimal
    ReservationType: Optional["enumDocumentReservationType"]
    Catalog: "SaleDocumentIssueCatalog"
    SalePriceType: "enumSalePriceType"
    Series: str
    JPK_V7Attributes: Optional["enumJPK_V7DocumentAttribute"]
    Note: str
    PaymentRegistry: "PaymentRegistryBase"
    Department: str
    PriceKind: "enumPriceKind"
    IssueDate: Optional[datetime]
    SaleDate: Optional[datetime]
    Buyer: "SaleDocumentIssueContractor"
    TypeCode: str
    Recipient: "SaleDocumentIssueContractor"
class SaleDocumentPosition(BaseModel):
    VatValuePLN: Decimal
    ProductCode: str
    NetValue: Decimal
    No: int
    ProductId: Optional[int]
    GrossValue: Decimal
    PriceValue: Decimal
    WrittenUnitOfMeasurement: str
    PriceValuePLN: Decimal
    SalePriceType: "enumSalePriceType"
    Description: str
    Id: int
    EnteredQuantity: Decimal
    SetHeaderId: Optional[int]
    WrittenQuantity: Decimal
    UnitOfMeasurement: str
    NetValuePLN: Decimal
    PriceKind: "enumPriceKind"
    Quantity: Decimal
    EnteredUnitOfMeasurement: str
    VatRate: "VatRateBase"
class SaleDocument(BaseModel):
    TypeCode: str
    Canceled: "enumCancelationType"
    ReceivedBy: str
    Id: int
    CurrencyRate: Decimal
    SaleDate: Optional[datetime]
    JPK_V7Attributes: "enumJPK_V7DocumentAttribute"
    PaymentRegistryId: int
    NetValuePLN: Decimal
    Description: str
    Note: str
    Buffer: bool
    SalePriceType: "enumSalePriceType"
    Settled: bool
    PaymentFormId: int
    BuyerId: Optional[int]
    eInvoice: bool
    Fisacal: "enumFiscalizationStatus"
    GrossValue: Decimal
    RecipientAddressId: Optional[int]
    VatValuePLN: Decimal
    RecipientId: Optional[int]
    IssuerId: int
    KindId: int
    PriceKind: "enumPriceKind"
    Marker: int
    Series: str
    Positions: List["SaleDocumentPosition"]
    NetValue: Decimal
    IssueDate: Optional[datetime]
    DocumentNumber: str
    DepartmentId: int
    CatalogId: int
    NumberInSeries: int
    CurrencyRateCIT: Decimal
    BuyerAddressId: Optional[int]
    MaturityDate: Optional[datetime]
    SplitPayment: bool
    Currency: str
    Active: bool
class SaleDocumentZMO(BaseModel):
    SaleDate: Optional[datetime]
    BuyerId: int
    Id: int
    IssueDate: Optional[datetime]
    RecipientId: int
    DocumentNumber: str
