from .. import (
    DocumentRecordAccountIssue,
)
from ......Enums import (
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
class DocumentSettlementIssue(BaseModel):
    Value: Decimal
    TransactionId: Optional[int]
    SettledDocument: str
    ValuePLN: Decimal
class DocumentRecordDimensionIssue(BaseModel):
    Index: int
    Value: str
class DocumentTransactionIssue(BaseModel):
    InterestType: "enumTransactionInterestType"
    InterestRate: Decimal
    Advance: bool
    MaturityDate: datetime
    ValuePLN: Decimal
class DocumentRecordDimensionSplitIssue(BaseModel):
    Dimensions: List["DocumentRecordDimensionIssue"]
    SplitValue: Decimal
class DocumentRecordIssue(BaseModel):
    DescriptionKind: "enumRecordDecsriptionKind"
    Side: "enumSideType"
    Features: List[int]
    Account: "DocumentRecordAccountIssue"
    No: int
    Settlements: List["DocumentSettlementIssue"]
    Transactions: List["DocumentTransactionIssue"]
    DimensionSplits: List["DocumentRecordDimensionSplitIssue"]
    ParallelType: "enumParallelType"
    ValuePLN: Decimal
    SplitNo: int
    Description: str
class DocumentIssue(BaseModel):
    Marker: int
    OperationDate: Optional[datetime]
    IssueDate: datetime
    DocumentNumber: str
    TypeCode: str
    YearId: int
    Records: List["DocumentRecordIssue"]
    Content: str
    Features: List[int]
    DocumentDate: Optional[datetime]
