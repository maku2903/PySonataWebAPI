from ......Enums import (
    enumCurrencyRateType,
    enumParallelType,
    enumRecordDecsriptionKind,
    enumSideType,
    enumTransactionInterestType,
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
class IDocumentIssue(BaseModel):
    DocumentNumber: str
    TypeCode: str
    Features: List[int]
    Content: str
    YearId: int
class IDocumentIssueExtended(IDocumentIssue):
    Currency: str
    ContractorPosition: int
    CurrencyRate: Decimal
    CurrencyRateType: "enumCurrencyRateType"
    CurrencyRateTableId: int
class IDocumentSettlementIssue(BaseModel):
    TransactionId: Optional[int]
    ValuePLN: Decimal
    SettledDocument: str
    Value: Decimal
class IDocumentTransactionIssue(BaseModel):
    InterestRate: Decimal
    Advance: bool
    InterestType: "enumTransactionInterestType"
    MaturityDate: datetime
    ValuePLN: Decimal
class IDocumentTransactionIssueExtended(IDocumentTransactionIssue):
    Value: Decimal
    RKP: Decimal
class IDocumentRecordIssue(BaseModel):
    Side: "enumSideType"
    Description: str
    ValuePLN: Decimal
    SplitNo: int
    No: int
    DescriptionKind: "enumRecordDecsriptionKind"
    Features: List[int]
    ParallelType: "enumParallelType"
class IDocumentRecordIssueExtended(IDocumentRecordIssue):
    Value: Decimal
