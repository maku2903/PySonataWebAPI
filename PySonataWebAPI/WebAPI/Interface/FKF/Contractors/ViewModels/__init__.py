from ....Enums import (
    enumContractorSplitPayment,
    enumContractorType,
)
from ...Common.ViewModels import (
    Dimension,
)
from ...Common.ViewModels.CriteriaFilter import (
    IntCriteriaFilter,
    StringCriteriaFilter,
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
class ContractorCriteriaFilter(BaseModel):
    CatalogId: Optional[int]
    EmailDomain: "StringCriteriaFilter"
    Marker: "IntCriteriaFilter"
    NIP: "StringCriteriaFilter"
    Code: "StringCriteriaFilter"
    Name: "StringCriteriaFilter"
    City: "StringCriteriaFilter"
    Active: Optional[bool]
    KindId: Optional[int]
    Province: "StringCriteriaFilter"
    Country: "StringCriteriaFilter"
class ContractorAddress(BaseModel):
    HouseNo: str
    PostCode: str
    Province: str
    Country: str
    Street: str
    ApartmentNo: str
    City: str
class ContractorBankInfo(BaseModel):
    AccountNumber: str
    BankName: str
class ContractorContact(BaseModel):
    Fax: str
    Email: str
    Name: str
    WWW: str
    Phone2: str
    Telex: str
    Phone1: str
    Surname: str
    Facebook: str
class ContractorListElement(BaseModel):
    Id: int
    Code: str
    Type: Optional["enumContractorType"]
    Place: str
    Name: str
    Active: bool
    NIP: str
    Position: int
    PostCode: str
class Contractor(BaseModel):
    CreditLimit: bool
    VATTaxPayer: bool
    Address: "ContractorAddress"
    BankInfo: "ContractorBankInfo"
    CreditCurrency: str
    Active: bool
    Regon: str
    Name: str
    Dimensions: List["Dimension"]
    Id: Optional[int]
    Contact: "ContractorContact"
    SplitPayment: "enumContractorSplitPayment"
    MaxCreditValue: Decimal
    Type: "enumContractorType"
    NIP: str
    Position: Optional[int]
    Code: str
    Vies: bool
    Pesel: str
