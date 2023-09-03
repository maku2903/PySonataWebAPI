from ....Common.ViewModels import (
    PaymentRegistryBase,
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
class DocumentIssueSettlement(BaseModel):
    DocumentId: Optional[int]
    Id: Optional[int]
    SettlementDate: Optional[datetime]
    Value: Decimal
    DocumentNumber: str
class DocumentIssueSubject(BaseModel):
    Id: Optional[int]
    Code: str
class PaymentIssue(BaseModel):
    Subject: "DocumentIssueSubject"
    TypeCode: str
    Settlements: List["DocumentIssueSettlement"]
    Series: str
    CurrencyRate: Decimal
    PaymentRegistry: "PaymentRegistryBase"
    PaymentDate: Optional[datetime]
    TotalValue: Optional[Decimal]
    Currency: str
    Note: str
class SettlementIssue(PaymentIssue):
    MaturityDate: Optional[datetime]
