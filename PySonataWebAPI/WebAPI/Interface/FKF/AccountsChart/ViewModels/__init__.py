from ....Enums import (
    enumSubjectType,
)
from ...Common.ViewModels import (
    Account,
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
class AccountChartElementSimple(BaseModel):
    Code: str
    Settlement: bool
    SubjectCode: str
    Level: int
    Id: int
    Account: str
    Account_Full: "Account"
    SubjectType: "enumSubjectType"
    Name: str
class AccountChartElement(AccountChartElementSimple):
    Childs: List["AccountChartElement"]
