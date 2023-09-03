from datetime import (
    datetime,
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
class BankAccount(BaseModel):
    Active: bool
    Main: bool
    SWIFT_BIC: str
    BankName: str
    WhiteList: Optional[List[bool]]
    WhiteListDate: Optional[List[datetime]]
    AccountNumber: str
    Id: int
