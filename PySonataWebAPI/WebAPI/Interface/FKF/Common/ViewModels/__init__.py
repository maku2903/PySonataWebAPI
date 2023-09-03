from ....Enums import (
    enumVatRegisterKind,
    enumVatRegisterType,
    enumYearClosingStatus,
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
class Country(BaseModel):
    Code: str
    Id: int
    Name: str
    Active: bool
class CurrencyTable(BaseModel):
    Description: str
    Id: int
    Table: str
    SaleCurrencyRate: Decimal
    CurrencyId: int
    Date: datetime
    PurchaseCurrencyRate: Decimal
class VatRate(BaseModel):
    Code: str
    DateTo: Optional[datetime]
    Rate: str
    Id: int
    IsActive: bool
    DateFrom: Optional[datetime]
class Year(BaseModel):
    Length: int
    Code: str
    Archived: bool
    EndDate: datetime
    StartDate: datetime
    Closed: "enumYearClosingStatus"
    Id: int
class Marker(BaseModel):
    Subtype: int
    Active: bool
    Name: str
class VatRegisterMarker(BaseModel):
    Code: str
    IsActive: bool
    Id: int
class Dimension(BaseModel):
    Name: str
    Type: str
    Value: str
    Code: str
    DictionaryValue: str
class FilterCriteria(BaseModel):
    Value: str
    Code: str
class Currency(BaseModel):
    Name: str
    Id: int
    Shortcut: str
    Active: bool
class DimensionClassification(BaseModel):
    Name: str
    Type: str
    Code: str
    Id: int
    DictionaryId: Optional[int]
    Index: Optional[int]
class Region(BaseModel):
    Name: str
    Active: bool
    Description: str
    Id: int
class TaxOffice(BaseModel):
    Name: str
    Id: int
    Code: str
    Position: int
    City: str
    IsActive: bool
class VatRegister(BaseModel):
    Type: "enumVatRegisterType"
    Name: str
    Period: Optional[int]
    Kind: "enumVatRegisterKind"
    Id: int
    Correction: bool
    Active: bool
class Catalog(BaseModel):
    FullPath: str
    Id: int
    Name: str
    ParentId: int
class FilterOption(BaseModel):
    TypeName: str
    Size: int
    Code: str
    Type: int
class Account(BaseModel):
    Analytic4: int
    Analytic5: int
    Analytic1: int
    Synthetic: int
    Analytic2: int
    Analytic3: int
