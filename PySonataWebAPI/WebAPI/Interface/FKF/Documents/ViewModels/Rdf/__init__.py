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
class RdfDocumentLink(BaseModel):
    Description: str
    URL: str
class RdfDocumentAttachment(BaseModel):
    Description: str
    FileName: str
    Content: str
