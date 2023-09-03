from ....Enums import (
    enumSplitValueType,
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
class Aspect(BaseModel):
    Value: str
    Index: int
    DictionaryValue: str
class AspectSplit(BaseModel):
    Aspects: List["Aspect"]
    SplitValue: Decimal
class AspectPosition(BaseModel):
    Id: int
class AspectPositionEdit(AspectPosition):
    AspectSplits: List["AspectSplit"]
    SplitValueType: "enumSplitValueType"
class AspectSplitDetails(AspectSplit):
    Percent: Decimal
class AspectPositionDetails(AspectPosition):
    ProductId: Optional[int]
    No: int
    Quantity: Decimal
    NetValuePLN: Decimal
    AspectSplits: List["AspectSplitDetails"]
class AspectDocument(BaseModel):
    DocumentNumber: str
    Buffer: bool
    Id: int
    IssueDate: Optional[datetime]
    Positions: List["AspectPositionDetails"]
