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
class DocumentRecordAccountIssue(BaseModel):
    Analytic1: int
    Analytic5: int
    Analytic2: int
    Synthetic: int
    Analytic4: int
    Analytic3: int
