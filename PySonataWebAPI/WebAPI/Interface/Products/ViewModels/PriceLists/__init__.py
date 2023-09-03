from ....Enums import (
    enumPriceFactorType,
    enumPriceKind,
    enumPriceListConnectionType,
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
class PriceListDetails(BaseModel):
    Currency: str
    PriceType: "enumSalePriceType"
    Value: Optional[Decimal]
    Type: "enumPriceFactorType"
    PriceKind: "enumPriceKind"
class PriceListSubject(BaseModel):
    Name: str
    Code: str
    Id: int
class PriceListSubjectDetails(PriceListSubject):
    Prices: List["PriceListDetails"]
class PriceListListElement(BaseModel):
    DateTo: Optional[datetime]
    DateFrom: Optional[datetime]
    Active: bool
    Id: int
    Code: str
    DepartmentId: Optional[int]
class PriceList(BaseModel):
    AvailableOnTuesday: bool
    AvailableOnWednesday: bool
    Code: str
    SpecificWeekdays: bool
    Type: "enumPriceFactorType"
    Contractors: List["PriceListSubject"]
    AvailableOnSaturday: bool
    DepartmentId: Optional[int]
    AvailableOnFriday: bool
    AvailableOnMonday: bool
    AvailableOnThursday: bool
    Id: int
    Products: List["PriceListSubjectDetails"]
    MinimalPriority: int
    AvailableOnSunday: bool
    ProductKinds: List["PriceListSubjectDetails"]
    ConnectionType: List["enumPriceListConnectionType"]
    DateTo: Optional[datetime]
    Active: bool
    Description: str
    Priority: int
    ContractorKinds: List["PriceListSubject"]
    DateFrom: Optional[datetime]
    ForAllContractors: bool
