from ...Enums import (
    enumDocumentCharacter,
    enumIncrementalSyncModifyType,
    enumJPKDocumentKind,
    enumJPK_V7DocumentAttribute,
    enumPaymentRegistryType,
    enumPriceKind,
    enumPriceType,
    enumPrintParameterDocumentStatus,
    enumPrintParameterNotSettledDocuments,
    enumPrintParameterOperationDateFormat,
    enumVatRateType,
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
    Generic,
    List,
    Optional,
    TypeVar,
)
from uuid import (
    UUID,
)

T = TypeVar('T', bound=BaseModel)
class Country(BaseModel):
    Name: str
    Active: bool
    Code: str
    Id: int
class Marker(BaseModel):
    Name: str
    Active: bool
    Subtype: int
class DocumentSeries(BaseModel):
    Id: int
    Code: str
class PDFDimensionSetting(BaseModel):
    PrintLabel: bool
    Code: str
class UnitOfMeasurement(BaseModel):
    Id: int
    Description: str
    Active: bool
    Name: str
class Dimension(BaseModel):
    Code: str
    DictionaryValue: Optional[str]
    Type: str
    Value: str
    Name: str
class Kind(BaseModel):
    Active: bool
    Code: str
    Id: Optional[int]
class FilterDimensionCriteria(BaseModel):
    Id: Optional[int]
    Value: str
    DictionaryValue: str
    Code: str
class PriceType(BaseModel):
    Name: str
    Kind: "enumPriceKind"
    Code: str
    Type: "enumPriceType"
    Active: bool
class VatRateBase(BaseModel):
    Code: str
    Id: Optional[int]
class VatRate(VatRateBase):
    RR: bool
    Value: Decimal
    Type: "enumVatRateType"
    Fiscal: bool
    Description: str
    Active: bool
    DateTo: Optional[datetime]
    DateFrom: Optional[datetime]
class PaymentRegistryBase(BaseModel):
    AccountNumber: str
    Code: str
    Id: Optional[int]
class CNCode(BaseModel):
    Name: str
    Description: str
    Id: int
    Active: bool
class PaymentRegistry(PaymentRegistryBase):
    BankName: str
    BankAccountId: int
    Type: "enumPaymentRegistryType"
    Name: str
    DefaultPaymentFormId: Optional[int]
class Warehouse(BaseModel):
    Name: str
    Code: str
    Id: int
class UnitOfMeasurementDefinition(BaseModel):
    Name: str
    Guid: UUID
    No: int
class PositionDimension(BaseModel):
    PositionId: int
    Dimensions: List["Dimension"]
class DimensionClassification(BaseModel):
    Type: str
    DictionaryId: Optional[int]
    Name: str
    Code: str
    Index: Optional[int]
    Id: int
class Catalog(BaseModel):
    ParentId: int
    Name: str
    FullPath: str
    Id: int
class Department(BaseModel):
    Name: str
    Code: str
    Id: int
class CharacterRelation(BaseModel):
    Corrections: "enumDocumentCharacter"
    Related: "enumDocumentCharacter"
    Character: "enumDocumentCharacter"
class PDF(BaseModel):
    Hash_SHA1: str
    CreateDate: datetime
    ContentFile_Base64: str
class PaymentFormBase(BaseModel):
    Client: int
    Id: Optional[int]
class PaymentForm(PaymentFormBase):
    Active: bool
    Name: str
    Type: "enumPaymentRegistryType"
    Days: int
class DocumentType(BaseModel):
    CorrectionSerieId: Optional[int]
    RelatedTypeId: Optional[int]
    Code: str
    Id: int
    JPK_V7Attributes: "enumJPK_V7DocumentAttribute"
    CorrectionTypeId: Optional[int]
    Active: bool
    Name: str
    RelatedSerieId: Optional[int]
    JPKDocumentKind: "enumJPKDocumentKind"
    Character: "enumDocumentCharacter"
class PKWiUCode(BaseModel):
    Active: bool
    Name: str
    Id: int
    Description: str
class IncrementalSyncListElement(BaseModel, Generic[T]):
    ModifyType: "enumIncrementalSyncModifyType"
    ModifiedAt: datetime
    Object: T
    Id: int
class AgriculturalPromotionFund(BaseModel):
    Code: str
    Active: bool
    AccountFK: str
    Rate: Decimal
class RelatedDocumentPosition(BaseModel):
    DocumentId: int
    NetValuePLN: Decimal
    No: int
    Id: int
    Quantity: Decimal
    NetValuePLNCorrected: Decimal
    DocumentNumber: str
    QuantityCorrected: Decimal
class PDFSettings(BaseModel):
    PrintRemarks: bool
    PrintReceiptNumber: bool
    PrintExecutiveSubject: bool
    NotSettledDocuments: "enumPrintParameterNotSettledDocuments"
    DocumentStatus: "enumPrintParameterDocumentStatus"
    PrintLeftToPay: bool
    PrintNote: bool
    OperationDateFormat: "enumPrintParameterOperationDateFormat"
    IncludedDimensions: List["PDFDimensionSetting"]
    DocumentStatusText: str
    PrintFooter: bool
    PrintDiscountColumns: bool
class CurrencyRate(BaseModel):
    CurrencyId: int
    Rate: Decimal
    Date: datetime
class Region(BaseModel):
    Active: bool
    Description: str
    Id: int
    Name: str
class Currency(BaseModel):
    Id: int
    Active: bool
    Name: str
    Shortcut: str
