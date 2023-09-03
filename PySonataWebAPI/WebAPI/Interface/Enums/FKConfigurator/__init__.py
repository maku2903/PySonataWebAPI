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
class SettingSide(Enum):
    Debit: 0
    Credit: 1

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class SettingPeriodType(Enum):
    IssueDate: 0
    DocumentDate: 1
    OperationDate: 2

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class SettingKind(Enum):
    Net: 0
    Gross: 1
    Vat: 2

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class DictionaryType(Enum):
    ProductType: 1
    Product: 2
    ContractorType: 3
    Contractor: 4
    Department: 5
    CostType: 6
    A01: 101
    A02: 102
    A03: 103
    A04: 104
    A05: 105
    A06: 106
    A07: 107
    A08: 108
    A09: 109
    A10: 110
    A11: 111
    A12: 112
    A13: 113
    A14: 114
    A15: 115
    A16: 116
    A17: 117
    A18: 118
    A19: 119
    A20: 120

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
class ContentTag(Enum):
    DocumentNumber: 1
    DocumentDate: 2
    DocumentDescription: 3
    ContractorCode: 4
    ProductCode: 5
    ProductName: 6

    @classmethod
    def _missing_(cls, value):
        return cls.Undocumented

    Undocumented = auto()
