from .. import (
    DocumentRecordAccountIssue,
)
from ......Enums import (
    enumCurrencyRateType,
    enumFKSplitPaymentType,
    enumJPK_V7DocumentAttribute,
    enumJPK_V7ProductGroup,
    enumParallelType,
    enumRecordDecsriptionKind,
    enumSideType,
    enumTransactionInterestType,
    enumVatRegisterPeriodType,
    enumVatRegisterTypeABCD,
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
class DocumentSettlementIssue(BaseModel):
    CurrencyForeign: str
    Currency: str
    ValueForeign: Optional[Decimal]
    ValuePLN: Optional[Decimal]
    CurrencyRateForeign: Optional[Decimal]
    TransactionId: Optional[int]
    CurrencyRate: Optional[Decimal]
    Value: Optional[Decimal]
    SettledDocument: str
class DocumentTransactionIssue(BaseModel):
    InterestType: Optional["enumTransactionInterestType"]
    InterestRate: Optional[Decimal]
    Advance: Optional[bool]
    CurrencyRate: Optional[Decimal]
    Currency: str
    MaturityDate: Optional[datetime]
    ValuePLN: Optional[Decimal]
    TransactionId: Optional[int]
    RKP: Optional[Decimal]
    Value: Optional[Decimal]
class DocumentVatRegisterIssue(BaseModel):
    Chargable: Optional[bool]
    VatRate: str
    GrossValuePLN: Optional[Decimal]
    PeriodType: Optional["enumVatRegisterPeriodType"]
    GrossValue: Optional[Decimal]
    UE: Optional[bool]
    VatValue: Optional[Decimal]
    Type: Optional["enumVatRegisterTypeABCD"]
    JPK_V7ProductGroups: Optional["enumJPK_V7ProductGroup"]
    VatValuePLN: Optional[Decimal]
    Marker: Optional[int]
    NetValue: Optional[Decimal]
    SplitNo: Optional[int]
    ContractorPosition: Optional[int]
    Service: Optional[bool]
    DefinitionId: int
    Period: Optional[datetime]
    NetValuePLN: Optional[Decimal]
    DocumentDate: Optional[datetime]
    ReceiptDate: Optional[datetime]
class DocumentRecordDimensionIssue(BaseModel):
    Value: str
    Index: int
class DocumentRecordDimensionSplitIssue(BaseModel):
    SplitValue: Decimal
    Dimensions: List["DocumentRecordDimensionIssue"]
class DocumentRecordIssue(BaseModel):
    DescriptionKind: Optional["enumRecordDecsriptionKind"]
    Features: List[int]
    Description: str
    ParallelType: Optional["enumParallelType"]
    KPKWDate: Optional[datetime]
    SplitNo: int
    Value: Optional[Decimal]
    Transactions: List["DocumentTransactionIssue"]
    Settlements: List["DocumentSettlementIssue"]
    Side: "enumSideType"
    ReportAccount: Optional[bool]
    ValuePLN: Optional[Decimal]
    CurrencyRateType: Optional["enumCurrencyRateType"]
    Currency: str
    CurrencyRateTableId: Optional[int]
    DimensionSplits: List["DocumentRecordDimensionSplitIssue"]
    DocumentNumber: str
    Account: "DocumentRecordAccountIssue"
    No: int
    CurrencyRate: Optional[Decimal]
class DocumentRelationIssue(BaseModel):
    DocumentDate: datetime
    DocumentNumber: str
    ContractorPosition: int
class DocumentVatRegisterCurrencyIssue(BaseModel):
    Currency: str
    CurrencyRate: Optional[Decimal]
    CurrencyRateTableId: Optional[int]
    CurrencyRateTableDate: Optional[datetime]
class DocumentIssue(BaseModel):
    VatRegisters: List["DocumentVatRegisterIssue"]
    CurrencyRateTableId: Optional[int]
    TypeCode: str
    Transactions: List["DocumentTransactionIssue"]
    Settlements: List["DocumentSettlementIssue"]
    Marker: Optional[int]
    OperationDate: Optional[datetime]
    SplitPaymentType: Optional["enumFKSplitPaymentType"]
    ContractorPosition: Optional[int]
    CurrencyRateType: Optional["enumCurrencyRateType"]
    YearId: int
    ReceiptDate: Optional[datetime]
    Value: Optional[Decimal]
    ValueOffVatRegistry: Optional[Decimal]
    Content: str
    ValueParallel: Optional[Decimal]
    JPK_V7Attributes: Optional["enumJPK_V7DocumentAttribute"]
    Currency: str
    DocumentDate: Optional[datetime]
    PeriodDate: Optional[datetime]
    IssueDate: datetime
    Features: List[int]
    DocumentNumber: str
    CurrencyRate: Optional[Decimal]
    OpeningBalance: Optional[Decimal]
    ValuePLN: Optional[Decimal]
    RecordsBalance: Optional[Decimal]
    CurrencyCIT_PIT: "DocumentVatRegisterCurrencyIssue"
    Relations: List["DocumentRelationIssue"]
    CurrencyVAT: "DocumentVatRegisterCurrencyIssue"
    Records: List["DocumentRecordIssue"]
