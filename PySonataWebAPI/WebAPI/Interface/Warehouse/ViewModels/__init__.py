from ...Enums import (
    enumCancelationType,
    enumDocumentReservationType,
    enumDocumentStatus,
    enumManualSettledState,
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
class WarehouseDocumentIssueDelivery(BaseModel):
    Id: Optional[int]
    Quantity: Decimal
    Code: str
class WarehouseDocumentListElement(BaseModel):
    OutcomeValue: Decimal
    DocumentValue: Decimal
    Buffer: bool
    DocumentNumber: str
    WarehouseId: int
    NumberInSeries: int
    IncomeValue: Decimal
    IssueDate: Optional[datetime]
    Id: int
    IssuerId: int
    Active: bool
    Canceled: "enumCancelationType"
    NetValue: Decimal
    Description: str
    Settled: bool
    MaturityDate: Optional[datetime]
    ContractorId: Optional[int]
    OperationDate: Optional[datetime]
    TypeCode: str
    ReceivingWarehouseId: Optional[int]
    Series: str
class WarehouseRegistry(BaseModel):
    Name: str
    Code: str
    Id: int
class WarehouseDocumentIssueContractorData(BaseModel):
    HouseNo: str
    NIP: str
    Country: str
    Street: str
    ApartmentNo: str
    City: str
    PostCode: str
    Name: str
class WarehouseDocumentIssueCatalog(BaseModel):
    AddIfNotExist: bool
    FullPath: str
class WarehouseDocumentIssueContractor(BaseModel):
    Code: str
    Id: Optional[int]
    DeliveryAddressCode: str
    Data: "WarehouseDocumentIssueContractorData"
class WarehouseDocumentIssueReceivingWarehouse(BaseModel):
    Id: Optional[int]
    Code: str
class WarehouseDocumentssueKind(BaseModel):
    AddIfNotExist: bool
    Code: str
class WarehouseDocumentBase(BaseModel):
    Description: str
    Catalog: "WarehouseDocumentIssueCatalog"
    Note: str
    Contractor: "WarehouseDocumentIssueContractor"
    ReceivingWarehouse: "WarehouseDocumentIssueReceivingWarehouse"
    Kind: "WarehouseDocumentssueKind"
    IssueDate: Optional[datetime]
    ReservationType: Optional["enumDocumentReservationType"]
    ReceivedBy: str
    Warehouse: str
    Marker: int
    MaturityDate: Optional[datetime]
    TypeCode: str
    WarehouseRegistry: str
    NumberInSeries: Optional[int]
    OperationDate: Optional[datetime]
    Series: str
class WarehouseDocumentIssuePositionElement(BaseModel):
    UnitOfMeasurement: str
    Deliveries: List["WarehouseDocumentIssueDelivery"]
    Name: str
    Value: Optional[Decimal]
    Quantity: Decimal
    Code: str
class WarehouseDocumentIssuePosition(WarehouseDocumentIssuePositionElement):
    Elements: List["WarehouseDocumentIssuePositionElement"]
class WarehouseDocumentEditPosition(WarehouseDocumentIssuePosition, WarehouseDocumentIssuePositionElement):
    Delete: bool
    PositionId: Optional[int]
class WarehouseDocumentEdit(WarehouseDocumentBase):
    Positions: List["WarehouseDocumentEditPosition"]
    Id: int
class WarehouseDocumentPositionReservation(BaseModel):
    Quantity: Decimal
    Id: int
class WarehouseDocumentPositionDelivery(BaseModel):
    Quantity: Decimal
    Code: str
    Id: int
    ReservationId: Optional[int]
    Date: datetime
class WarehouseDocumentPosition(BaseModel):
    UnitOfMeasurement: str
    EnteredQuantity: Decimal
    SetHeaderId: Optional[int]
    EnteredUnitOfMeasurement: str
    Description: str
    WrittenQuantity: Decimal
    WrittenUnitOfMeasurement: str
    Id: int
    Quantity: Decimal
    No: int
    NetValue: Decimal
    PriceValue: Decimal
    ProductId: int
    Reservations: List["WarehouseDocumentPositionReservation"]
    Deliveries: List["WarehouseDocumentPositionDelivery"]
    ProductCode: str
class WarehouseDocument(BaseModel):
    Marker: int
    MaturityDate: Optional[datetime]
    Buffer: bool
    NetValue: Decimal
    Canceled: "enumCancelationType"
    Description: str
    NumberInSeries: int
    OperationDate: Optional[datetime]
    Series: str
    ReceivingWarehouseId: Optional[int]
    DocumentValue: Decimal
    IssueDate: Optional[datetime]
    IncomeValue: Decimal
    TypeCode: str
    ContractorAddressId: Optional[int]
    WarehouseId: int
    CatalogId: int
    OutcomeValue: Decimal
    IssuerId: int
    Id: int
    Note: str
    ContractorId: Optional[int]
    KindId: int
    Active: bool
    Positions: List["WarehouseDocumentPosition"]
    Settled: bool
    DocumentNumber: str
class WarehouseDocumentStatus(BaseModel):
    Buffer: bool
    WarehouseSettled: int
    ManualSettled: "enumManualSettledState"
    DocumentStatusText: str
    PaymentSettled: int
    Id: int
    DocumentStatus: "enumDocumentStatus"
    RDFStatus: "enumRDFStatus"
    DocumentNumber: str
class WarehouseDocumentIssue(WarehouseDocumentBase):
    Positions: List["WarehouseDocumentIssuePosition"]
class WarehouseDocumentFV(BaseModel):
    Contractor1Id: int
    IssueDate: Optional[datetime]
    Contractor2Id: int
    DocumentNumber: str
    Id: int
    OperationDate: Optional[datetime]
class DeliveryListElement(BaseModel):
    Code: str
    QuantityInWarehouse: Decimal
    DeliveryDate: datetime
    WarehouseId: int
    Id: int
    ContractorId: Optional[int]
    QuantityForSale: Decimal
    ProductId: int
