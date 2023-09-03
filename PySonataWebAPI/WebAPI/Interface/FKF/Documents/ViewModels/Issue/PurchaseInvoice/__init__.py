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
class DocumentRecordDimensionIssue(BaseModel):
    Index: int
    Value: str
class DocumentRecordDimensionSplitIssue(BaseModel):
    Dimensions: List["DocumentRecordDimensionIssue"]
    SplitValue: Decimal
class DocumentSettlementIssue(BaseModel):
    TransactionId: Optional[int]
    SettledDocument: str
    Value: Decimal
    ValuePLN: Decimal
class DocumentTransactionIssue(BaseModel):
    Advance: bool
    InterestType: "enumTransactionInterestType"
    MaturityDate: datetime
    InterestRate: Decimal
    Value: Decimal
    RKP: Decimal
    ValuePLN: Decimal
class DocumentVatRegisterIssue(BaseModel):
    VatRate: str
    VatValuePLN: Decimal
    GrossValuePLN: Decimal
    PeriodType: "enumVatRegisterPeriodType"
    DefinitionId: int
    Period: datetime
    Type: "enumVatRegisterTypeABCD"
    Marker: int
    NetValuePLN: Decimal
    JPK_V7ProductGroups: Optional["enumJPK_V7ProductGroup"]
class DocumentRecordIssue(BaseModel):
    DimensionSplits: List["DocumentRecordDimensionSplitIssue"]
    ValuePLN: Decimal
    DescriptionKind: "enumRecordDecsriptionKind"
    Transactions: List["DocumentTransactionIssue"]
    Side: "enumSideType"
    Settlements: List["DocumentSettlementIssue"]
    Value: Decimal
    Features: List[int]
    No: int
    SplitNo: int
    ParallelType: "enumParallelType"
    Account: "DocumentRecordAccountIssue"
    Description: str
class DocumentIssue(BaseModel):
    Features: List[int]
    Settlements: List["DocumentSettlementIssue"]
    ReceiptDate: Optional[datetime]
    CurrencyRate: Decimal
    PeriodDate: Optional[datetime]
    Marker: int
    CurrencyRateTableId: int
    DocumentDate: Optional[datetime]
    SplitPaymentType: "enumFKSplitPaymentType"
    Content: str
    CurrencyRateType: "enumCurrencyRateType"
    ContractorPosition: int
    DocumentNumber: str
    JPK_V7Attributes: Optional["enumJPK_V7DocumentAttribute"]
    IssueDate: datetime
    OperationDate: Optional[datetime]
    TypeCode: str
    VatRegisters: List["DocumentVatRegisterIssue"]
    YearId: int
    Records: List["DocumentRecordIssue"]
    Currency: str
    Transactions: List["DocumentTransactionIssue"]
