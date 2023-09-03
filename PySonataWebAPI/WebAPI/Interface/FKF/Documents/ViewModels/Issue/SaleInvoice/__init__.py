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
    Value: str
    Index: int
class DocumentRecordDimensionSplitIssue(BaseModel):
    Dimensions: List["DocumentRecordDimensionIssue"]
    SplitValue: Decimal
class DocumentTransactionIssue(BaseModel):
    RKP: Decimal
    Advance: bool
    InterestType: "enumTransactionInterestType"
    InterestRate: Decimal
    ValuePLN: Decimal
    Value: Decimal
    MaturityDate: datetime
class DocumentSettlementIssue(BaseModel):
    ValuePLN: Decimal
    TransactionId: Optional[int]
    Value: Decimal
    SettledDocument: str
class DocumentRecordIssue(BaseModel):
    Description: str
    DimensionSplits: List["DocumentRecordDimensionSplitIssue"]
    Value: Decimal
    Account: "DocumentRecordAccountIssue"
    Transactions: List["DocumentTransactionIssue"]
    SplitNo: int
    No: int
    DescriptionKind: "enumRecordDecsriptionKind"
    Settlements: List["DocumentSettlementIssue"]
    Features: List[int]
    ParallelType: "enumParallelType"
    ValuePLN: Decimal
    Side: "enumSideType"
class DocumentVatRegisterIssue(BaseModel):
    VatRate: str
    GrossValuePLN: Decimal
    Type: "enumVatRegisterTypeABCD"
    NetValuePLN: Decimal
    JPK_V7ProductGroups: Optional["enumJPK_V7ProductGroup"]
    PeriodType: "enumVatRegisterPeriodType"
    Marker: int
    VatValuePLN: Decimal
    DefinitionId: int
    Period: datetime
class DocumentIssue(BaseModel):
    ContractorPosition: int
    CurrencyRateTableId: int
    Transactions: List["DocumentTransactionIssue"]
    JPK_V7Attributes: Optional["enumJPK_V7DocumentAttribute"]
    CurrencyRateType: "enumCurrencyRateType"
    SplitPaymentType: "enumFKSplitPaymentType"
    Content: str
    VatRegisters: List["DocumentVatRegisterIssue"]
    IssueDate: datetime
    DocumentNumber: str
    TypeCode: str
    PeriodDate: Optional[datetime]
    Records: List["DocumentRecordIssue"]
    OperationDate: Optional[datetime]
    YearId: int
    Marker: int
    Currency: str
    ReceiptDate: Optional[datetime]
    CurrencyRate: Decimal
    Features: List[int]
    Settlements: List["DocumentSettlementIssue"]
    DocumentDate: Optional[datetime]
