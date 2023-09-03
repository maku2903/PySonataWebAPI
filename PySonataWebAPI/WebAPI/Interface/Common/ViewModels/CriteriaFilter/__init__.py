from ....Enums import (
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
class IntCriteriaFilter(BaseModel):
    Value_To: int
    Mode: "enumFilterSqlCriteriaMode"
    Value_From: int
class StringCriteriaFilter(BaseModel):
    Value: str
    Mode: "enumFilterSqlCriteriaMode"
