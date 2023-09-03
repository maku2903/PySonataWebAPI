from ..Enums import (
    enumOrderByType,
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
    Any,
    Generic,
    List,
    Optional,
    TypeVar,
)

T = TypeVar('T', bound=BaseModel)
class LicenceInfo(BaseModel):
    ValueObject: Any
    Feature: str
    ValueInt: int
    ValueBool: bool
    ValueDateTime: Optional[datetime]
    ValueString: str
    ValueDecimal: Decimal
    Module: str
class LoadedModuleInfo(BaseModel):
    AssemblyName: str
    ModuleVersion: str
    ModuleName: str
class InstanceInfo(BaseModel):
    Firm: str
    User: str
    Seed: str
    ServerName: str
    DatabaseName: str
class Ping(BaseModel):
    OpenSessionsNumber: int
    LoadedModuleInfo: List["LoadedModuleInfo"]
    ActiveHMFInfo: List["InstanceInfo"]
    ActiveITGInfo: List["InstanceInfo"]
class SessionInformation(BaseModel):
    DeviceName: str
    ExpireTime: datetime
    TotalSessionsCount: int
    RegisterTime: datetime
    Token: str
class CompanyInfo(BaseModel):
    NIP: str
    Name: str
    LicensesInfo: List["LicenceInfo"]
    Address: str
class Page(BaseModel, Generic[T]):
    Data: List[T]
    OrderBy: "enumOrderByType"
    NextPage: str
    TotalItems: int
    PageNumber: int
    PreviousPage: str
    LimitPerPage: int
