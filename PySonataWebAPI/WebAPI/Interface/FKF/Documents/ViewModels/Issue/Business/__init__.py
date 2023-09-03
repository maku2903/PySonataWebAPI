from ......Enums import (
    enumFKSplitPaymentType,
    enumJPK_V7ProductGroup,
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
class BusinessDocumentPositionIssue(BaseModel):
    Account06: str
    Account11: str
    Account20: str
    JPK_V7ProductGroups: Optional["enumJPK_V7ProductGroup"]
    Account16: str
    Account04: str
    Account13: str
    NetValuePLN: Decimal
    Description: str
    CostType: str
    VatValue: Decimal
    Account09: str
    Account17: str
    Account15: str
    Account01: str
    VatRate: str
    GrossValuePLN: Decimal
    Account08: str
    Account10: str
    GrossValue: Decimal
    ProductType: str
    NetValue: Decimal
    Account19: str
    Account12: str
    Account05: str
    Account07: str
    Account18: str
    Product: str
    Account03: str
    Account02: str
    VatValuePLN: Decimal
    Account14: str
class BusinessDocumentCorrectionIssue(BaseModel):
    DocumentNumber: str
    DocumentDate: datetime
class BusinessDocumentIssue(BaseModel):
    OperationDate: Optional[datetime]
    Positions: List["BusinessDocumentPositionIssue"]
    ReceiptDate: Optional[datetime]
    Contractor: str
    IssueDate: Optional[datetime]
    Marker: int
    Currency: str
    ContractorPosition: Optional[int]
    CurrencyRate: Optional[Decimal]
    Department: str
    ContractorType: str
    Description: str
    SplitPaymentType: "enumFKSplitPaymentType"
    DocumentDate: Optional[datetime]
    MaturityDate: Optional[datetime]
    DocumentType: str
    Corrections: List["BusinessDocumentCorrectionIssue"]
    DocumentNumber: str
