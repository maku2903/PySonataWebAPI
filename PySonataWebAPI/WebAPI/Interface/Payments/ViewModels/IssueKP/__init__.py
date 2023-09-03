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
class PaymentKPIssueInvoice(BaseModel):
    Id: Optional[int]
    SettlementDate: Optional[datetime]
    Value: Decimal
    DocumentNumber: str
class PaymentKPIssueContractor(BaseModel):
    Code: str
    Id: Optional[int]
class PaymentKPIssue(BaseModel):
    PaymentRegistry: "PaymentRegistryBase"
    Currency: str
    Series: str
    TypeCode: str
    PaymentDate: Optional[datetime]
    CurrencyRate: Decimal
    Invoices: List["PaymentKPIssueInvoice"]
    Contractor: "PaymentKPIssueContractor"
    TotalValue: Optional[Decimal]
    Note: str
