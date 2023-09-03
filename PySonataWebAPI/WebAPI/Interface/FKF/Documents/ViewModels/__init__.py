from ....Enums import (
    enumCurrencyRateType,
    enumDocumentSource,
    enumFKDocumentCharacter,
    enumFKDocumentMessageType,
    enumFKSplitPaymentType,
    enumJPK_V7DocumentAttribute,
    enumJPK_V7ProductGroup,
    enumParallelType,
    enumRecordDecsriptionKind,
    enumSideType,
    enumSplitOpposingAccountType,
    enumSplitType,
    enumTransactionInterestType,
    enumVatRegisterPeriodType,
    enumVatRegisterTypeABCD,
)
from ...Common.ViewModels import (
    Account,
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
class Feature(BaseModel):
    BufferOnly: bool
    YearId: int
    Name: str
    Description: str
    Id: int
class DocumentVatRegister(BaseModel):
    ReceiptDate: datetime
    ToPay: Decimal
    DocumentDate: datetime
    ContractorPosition: int
    UE: bool
    GrossValuePLN: Decimal
    VatRate: str
    NetValuePLN: Decimal
    PeriodType: "enumVatRegisterPeriodType"
    Marker: int
    SplitNo: int
    VatValuePLN: Decimal
    DefinitionId: int
    VatValue: Decimal
    Chargable: bool
    JPK_V7ProductGroups: "enumJPK_V7ProductGroup"
    GrossValue: Decimal
    Service: bool
    NetValue: Decimal
    Type: "enumVatRegisterTypeABCD"
    Id: int
    CorrectionNumber: str
    CorrectionDate: datetime
    Period: datetime
class DocumentTransaction(BaseModel):
    ValuePLN: Decimal
    InterestType: "enumTransactionInterestType"
    MaturityDate: datetime
    InterestRate: Decimal
    Value: Decimal
    CurrencyRate: Decimal
    Advance: bool
    Account: str
    Id: int
    Account_Full: "Account"
    Currency: str
    Side: "enumSideType"
    RKP: Decimal
class DocumentSettlement(BaseModel):
    CurrencyRateForeign: Decimal
    SettledDocument: str
    Account_Full: "Account"
    CurrencyForeign: str
    Account: str
    Id: int
    CurrencyRate: Decimal
    Side: "enumSideType"
    TransactionId: int
    Currency: str
    ValuePLN: Decimal
    Value: Decimal
    ValueForeign: Decimal
class DocumentRecord(BaseModel):
    Value: Decimal
    Id: int
    SplitNo: int
    Account_Full: "Account"
    CurrencyRate: Decimal
    ValuePLN: Decimal
    DocumentNumber: str
    SplitOpposingAccountType: "enumSplitOpposingAccountType"
    ParallelType: "enumParallelType"
    No: int
    DescriptionKind: "enumRecordDecsriptionKind"
    SplitType: "enumSplitType"
    CurrencyRateType: "enumCurrencyRateType"
    Features: List[int]
    ReportAccount: bool
    Side: "enumSideType"
    CurrencyRateTableId: int
    KPKWDate: datetime
    Account: str
    Currency: str
    Description: str
    Transactions: List["DocumentTransaction"]
    RecordVat: bool
    Settlements: List["DocumentSettlement"]
class DocumentVatRegisterCurrency(BaseModel):
    Currency: str
    CurrencyRate: Optional[Decimal]
    CurrencyRateTableDate: Optional[datetime]
    CurrencyRateTableId: Optional[int]
class DocumentRelation(BaseModel):
    DocumentDate: datetime
    DocumentNumber: str
    YearId: int
    DocumentId: int
class DocumentMessage(BaseModel):
    Message: str
    Type: "enumFKDocumentMessageType"
class Document(BaseModel):
    VatRegisters: List["DocumentVatRegister"]
    Transactions: List["DocumentTransaction"]
    CorrectionNumber: str
    CurrencyCIT_PIT: "DocumentVatRegisterCurrency"
    DocumentNumber: str
    ReceiptDate: datetime
    OperationDate: datetime
    CurrencyRate: Decimal
    YearId: int
    ValueParallel: Decimal
    TrilateralContractorPosition: int
    SplitPaymentType: "enumFKSplitPaymentType"
    Value: Decimal
    ValueOffVatRegistry: Decimal
    CorrectionDate: datetime
    CurrencyRateType: "enumCurrencyRateType"
    OpeningBalance: Decimal
    Settlements: List["DocumentSettlement"]
    ContractorPosition: int
    TypeCode: str
    Content: str
    SettlementId: int
    Marker: int
    Currency: str
    RecordsBalance: Decimal
    ValuePLN: Decimal
    Source: "enumDocumentSource"
    DocumentDate: datetime
    Id: int
    CurrencyVAT: "DocumentVatRegisterCurrency"
    Records: List["DocumentRecord"]
    Features: List[int]
    IssueDate: datetime
    CurrencyRateTableId: int
    Relations: List["DocumentRelation"]
    PeriodDate: datetime
    JPK_V7Attributes: "enumJPK_V7DocumentAttribute"
    NumberInSeries: int
    FKMessages: List["DocumentMessage"]
class DocumentListElement(BaseModel):
    ValuePLN: Decimal
    PeriodDate: Optional[datetime]
    NumberInSeries: int
    Value: Decimal
    ContractorPosition: Optional[int]
    Content: str
    DocumentDate: Optional[datetime]
    ReceiptDate: Optional[datetime]
    Source: "enumDocumentSource"
    TypeCode: str
    Id: int
    Currency: str
    IssueDate: Optional[datetime]
    YearId: int
    DocumentNumber: str
    OperationDate: Optional[datetime]
class DocumentType(BaseModel):
    Character: "enumFKDocumentCharacter"
    Id: int
    YearId: int
    Name: str
    Code: str
