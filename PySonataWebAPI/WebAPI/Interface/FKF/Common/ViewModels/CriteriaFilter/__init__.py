from .....Enums import (
    enumFilterSqlCriteriaMode,
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
class StringCriteriaFilter(BaseModel):
    Mode: "enumFilterSqlCriteriaMode"
    Value: str
class IntCriteriaFilter(BaseModel):
    Value_From: int
    Value_To: int
    Mode: "enumFilterSqlCriteriaMode"
