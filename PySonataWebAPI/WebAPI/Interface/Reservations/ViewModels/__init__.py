from ...Enums import (
    enumDocumentReservationType,
    enumReservationDocumentType,
    enumReservationKind,
    enumReservationMode,
    enumReservationPositionType,
    enumReservationType,
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
class ReservationNewUnitInfo(BaseModel):
    Id: Optional[int]
    Code: str
class ReservationNewProduct(ReservationNewUnitInfo):
    pass
class ReservationListElement(BaseModel):
    Id: int
    ContractorId: Optional[int]
    Kind: "enumReservationKind"
    MaturityDate: Optional[datetime]
    StandardPositionType: Optional["enumReservationPositionType"]
    Type: "enumReservationType"
    PositionType: int
    WarehouseId: Optional[int]
    Value: Decimal
    DocumentId: Optional[int]
    Quantity: Decimal
    PositionId: Optional[int]
    DocumentType: int
    ReservationDate: Optional[datetime]
    ProductId: Optional[int]
    StandardDocumentType: Optional["enumReservationDocumentType"]
class ReservationNewWarehouse(ReservationNewUnitInfo):
    pass
class ReservationNewContractor(ReservationNewUnitInfo):
    pass
class ReservationNewDelivery(BaseModel):
    Quantity: Decimal
    Id: Optional[int]
    Code: str
class ReservationNew(BaseModel):
    MaturityDate: Optional[datetime]
    Type: "enumDocumentReservationType"
    Product: "ReservationNewProduct"
    Warehouse: "ReservationNewWarehouse"
    Quantity: Optional[Decimal]
    Contractor: "ReservationNewContractor"
    ReserveToMax: bool
    Deliveries: List["ReservationNewDelivery"]
    MustReserveAllIndicatedDeliveries: bool
    ReservationDate: Optional[datetime]
class AdvancedReservationNew(ReservationNew):
    DocumentId: int
    PositionId: int
    Mode: "enumReservationMode"
    DocumentType: int
    PositionType: int
class ReservationDelivery(BaseModel):
    RealizedQuantity: Decimal
    Date: datetime
    Id: int
    Quantity: Decimal
    Value: Decimal
    Code: str
class Reservation(ReservationListElement):
    Deliveries: List["ReservationDelivery"]
