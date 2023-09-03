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
    SettlementDate: Optional[datetime]
    Value: Decimal
