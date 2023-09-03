from ...Common.ViewModels import (
    Catalog,
    Dimension,
    FilterDimensionCriteria,
    Kind,
    PaymentFormBase,
    PaymentRegistryBase,
)
from ...Common.ViewModels.CriteriaFilter import (
    IntCriteriaFilter,
    StringCriteriaFilter,
)
from ...Enums import (
    enumContractorSplitPayment,
    enumContractorType,
    enumFilterCriteriaMode,
    enumPriceKind,
    enumSalePriceType,
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
class ContractorListElement(BaseModel):
    Code: str
    PostCode: str
    PaymentFormOid: int
    Active: bool
    Id: int
    PriceKind: Optional["enumPriceKind"]
    Type: Optional["enumContractorType"]
    PriceType: Optional["enumSalePriceType"]
    Pesel: str
    Place: str
    Name: str
    PaymentRegistryOid: int
    NIP: str
class ContractorListElementWithDimensions(ContractorListElement):
    Dimensions: List["Dimension"]
class ContractorAddress(BaseModel):
    City: str
    HouseNo: str
    Street: str
    ApartmentNo: str
    PostCode: str
    Province: str
    Country: str
    FullAddress: str
class ContractorCorrespondenceAddress(ContractorAddress):
    pass
class ContractorDeliveryAddress(ContractorAddress):
    Id: Optional[int]
    Code: str
class ContractorFilterCriteria(BaseModel):
    Dimensions: List["FilterDimensionCriteria"]
    Code_From: str
    City_To: str
    Country: str
    Province_Mode: Optional["enumFilterCriteriaMode"]
    Marker_To: int
    Marker_Mode: Optional["enumFilterCriteriaMode"]
    Code_To: str
    Active: Optional[bool]
    Name_Mode: Optional["enumFilterCriteriaMode"]
    NIP_From: str
    Province_From: str
    Name_From: str
    Name_To: str
    NIP_Mode: Optional["enumFilterCriteriaMode"]
    Code_Mode: Optional["enumFilterCriteriaMode"]
    NIP_To: str
    Province_To: str
    Marker_From: int
    City_Mode: Optional["enumFilterCriteriaMode"]
    City_From: str
class ContractorCriteriaFilter(BaseModel):
    Name: "StringCriteriaFilter"
    Province: "StringCriteriaFilter"
    NIP: "StringCriteriaFilter"
    Country: "StringCriteriaFilter"
    Marker: "IntCriteriaFilter"
    EmailDomain: "StringCriteriaFilter"
    CatalogId: Optional[int]
    Code: "StringCriteriaFilter"
    City: "StringCriteriaFilter"
    Active: Optional[bool]
    KindId: Optional[int]
class ContractorContact(BaseModel):
    Fax: str
    WWW: str
    Name: str
    Surname: str
    Phone1: str
    Email: str
    Phone2: str
    Facebook: str
class ContractorBankInfo(BaseModel):
    AccountNumer: str
    AccountNumber: str
    BankName: str
    SWIFT_BIC: str
class ContractorFK(BaseModel):
    IdFK: str
    ParameterFK: str
    IdFKSync: Optional[int]
    IdentFK: str
class ContractorDefaultAddress(ContractorAddress):
    pass
class Contractor(BaseModel):
    MaxCreditValue: Decimal
    DeliveryAddresses: List["ContractorDeliveryAddress"]
    PriceKind: "enumPriceKind"
    BankInfo: "ContractorBankInfo"
    CorrespondenceAddress: "ContractorCorrespondenceAddress"
    DefaultDiscountPercent: Decimal
    Catalog: "Catalog"
    CreditLimit: bool
    Dimensions: List["Dimension"]
    Id: Optional[int]
    NIP: str
    VATTaxPayer: bool
    Obligation: Decimal
    PriceNegotiation: bool
    FK: "ContractorFK"
    SplitPayment: "enumContractorSplitPayment"
    Kind: "Kind"
    PaymentRegistry: "PaymentRegistryBase"
    Vies: bool
    CreditCurrency: str
    Code: str
    PaymentForm: "PaymentFormBase"
    Due: Decimal
    Note: str
    Pesel: str
    Contact: "ContractorContact"
    Active: bool
    PriceType: "enumSalePriceType"
    Marker: int
    Type: "enumContractorType"
    DefaultAddress: "ContractorDefaultAddress"
    Name: str
    Regon: str
