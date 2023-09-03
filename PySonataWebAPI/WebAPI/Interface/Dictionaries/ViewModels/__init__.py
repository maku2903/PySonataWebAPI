from ...Enums.FKConfigurator import (
    DictionaryType,
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
class DictionaryElement(BaseModel):
    Description: str
    Position: Optional[int]
    Id: Optional[int]
    Code: str
    Active: bool
    Name: str
class Dictionary(BaseModel):
    Name: str
    Active: bool
    NonSetElementId: Optional[int]
    Id: int
    SuggestedElementId: Optional[int]
    Elements: List["DictionaryElement"]
    Code: str
    DefaultElementId: Optional[int]
class BusinessDictionaryElement(BaseModel):
    Code: str
    Id: Optional[int]
    Position: str
class ContractorPosition(BaseModel):
    Position: int
    Id: int
class DictionaryListElement(BaseModel):
    Code: str
    Id: int
    Name: str
    Active: Optional[bool]
class BusinessDictionary(BaseModel):
    Id: "DictionaryType"
    Elements: List["BusinessDictionaryElement"]
    Code: str
    Name: str
