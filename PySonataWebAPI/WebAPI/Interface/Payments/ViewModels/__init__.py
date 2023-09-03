from ...Enums import (
    enumCancelationType,
    enumPaymentSubjectType,
    enumPaymentType,
    enumSettlementType,
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
class SettlementPosition(BaseModel):
    ValueSettlement: Decimal
    ValuePLN: Decimal
    DocumentNumber: str
    ValuePayment: Decimal
    Id: int
    CurrencyRatePayment: Decimal
    CurrencyRateSettlement: Decimal
class Settlement(BaseModel):
    Positions: List["SettlementPosition"]
    IssuerId: int
    Buffer: bool
    SettlementType: "enumSettlementType"
    DocumentId: Optional[int]
    Active: bool
    MaturityDate: Optional[datetime]
    ContractorId: Optional[int]
    LeftToPayValuePLN: Decimal
    PaidValue: Decimal
    IssueDate: Optional[datetime]
    SubjectId: Optional[int]
    Settled: bool
    Canceled: "enumCancelationType"
    TotalValue: Decimal
    PaidValuePLN: Decimal
    SubjectType: "enumPaymentSubjectType"
    SettlementDate: Optional[datetime]
    LeftToPayValue: Decimal
    NumberInSeries: int
    DocumentNumber: str
    PaymentRegistryId: int
    Id: int
    Description: str
    CurrencyRate: Decimal
    Currency: str
    Series: str
    TypeCode: str
class PaymentListElement(BaseModel):
    ReceivingPaymentRegistryId: Optional[int]
    SubjectType: "enumPaymentSubjectType"
    TotalValue: Decimal
    Currency: str
    SettlementDate: Optional[datetime]
    DocumentNumber: str
    MaturityDate: Optional[datetime]
    SettledValue: Decimal
    Id: int
    PaymentType: "enumPaymentType"
    IssueDate: Optional[datetime]
    SubjectId: Optional[int]
    CurrencyRate: Decimal
    PaymentRegistryId: Optional[int]
    SettledValuePLN: Decimal
class SettlementListElement(BaseModel):
    Id: int
    PaidValue: Decimal
    IssueDate: Optional[datetime]
    Currency: str
    DocumentId: Optional[int]
    TotalValue: Decimal
    LeftToPayValuePLN: Decimal
    SettlementType: "enumSettlementType"
    DocumentNumber: str
    SettlementDate: Optional[datetime]
    SubjectId: Optional[int]
    PaidValuePLN: Decimal
    MaturityDate: Optional[datetime]
    SubjectType: "enumPaymentSubjectType"
    CurrencyRate: Decimal
    LeftToPayValue: Decimal
    ContractorId: Optional[int]
class PaymentPosition(BaseModel):
    DocumentNumber: str
    CurrencyRateSettlement: Decimal
    ValuePayment: Decimal
    Id: int
    CurrencyRatePayment: Decimal
    ValueSettlement: Decimal
    ValuePLN: Decimal
class Payment(BaseModel):
    Id: int
    TotalValue: Decimal
    PaymentType: "enumPaymentType"
    SettledValue: Decimal
    DocumentNumber: str
    Currency: str
    ReceivingPaymentRegistryId: Optional[int]
    SubjectType: "enumPaymentSubjectType"
    Settled: bool
    Description: str
    PaymentRegistryId: int
    SettlementDate: Optional[datetime]
    IssueDate: Optional[datetime]
    Canceled: "enumCancelationType"
    Series: str
    IssuerId: int
    Active: bool
    TypeCode: str
    Buffer: bool
    SubjectId: Optional[int]
    NumberInSeries: int
    SettledValuePLN: Decimal
    CurrencyRate: Decimal
    MaturityDate: Optional[datetime]
    Positions: List["PaymentPosition"]
