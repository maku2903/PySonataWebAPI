from ....Enums import (
    enumCalculationState,
    enumCalculationType,
    enumSideType,
    enumSubjectType,
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
class CalculationFilterAccountOptions(BaseModel):
    Synthetic: int
    Analytic2: int
    Analytic5: int
    Analytic4: int
    Analytic3: int
    Analytic1: int
class CalculationFilterOptions(BaseModel):
    DateTo: Optional[datetime]
    Currency: str
    ForDay: Optional[datetime]
    State: Optional["enumCalculationState"]
    SubjectType: Optional["enumSubjectType"]
    Type: Optional["enumCalculationType"]
    ValueTo: Optional[Decimal]
    Account: "CalculationFilterAccountOptions"
    SubjectPosition: Optional[int]
    ValueFrom: Optional[Decimal]
    OrderBy: List[str]
    WithoutDate: Optional[bool]
    DateFrom: Optional[datetime]
    GroupBy: List[str]
    DocumentName: str
class CalculationListElement(BaseModel):
    DocumentNumber: str
    SettlementId: int
    Account: str
    Currency: str
    ValuePLN: Decimal
    DocumentDate: datetime
    Note: str
    CurrencyRate: Decimal
    SubjectType: "enumSubjectType"
    RecordNumber: str
    Buffer: bool
    SubjectPosition: int
    Value: Decimal
    PeriodDate: datetime
    TransactionId: int
    DocumentId: int
    Side: "enumSideType"
    DaysToMaturity: int
    MaturityDate: datetime
    State: "enumCalculationState"
    YearId: int
class CalculationListElementGrouped(BaseModel):
    ValuePLN: Decimal
    SubjectPosition: int
    SubjectType: "enumSubjectType"
