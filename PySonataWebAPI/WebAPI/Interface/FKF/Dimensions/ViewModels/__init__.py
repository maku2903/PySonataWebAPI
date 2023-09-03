from ....Enums import (
    enumDocumentSource,
    enumSideType,
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
class DocumentRecordDimension(BaseModel):
    Index: int
    Value: str
class DocumentRecordDimensionSplit(BaseModel):
    Dimensions: List["DocumentRecordDimension"]
    SplitValue: Decimal
    Percent: Decimal
class DocumentRecord(BaseModel):
    ValuePLN: Decimal
    DimensionSplits: List["DocumentRecordDimensionSplit"]
    Value: Decimal
    SplitNo: int
    Currency: str
    Id: int
    Side: "enumSideType"
    Account: str
    No: int
class Document(BaseModel):
    Records: List["DocumentRecord"]
    Id: int
    Source: "enumDocumentSource"
    YearId: int
    DocumentNumber: str
    DocumentDate: datetime
    ContractorPosition: int
