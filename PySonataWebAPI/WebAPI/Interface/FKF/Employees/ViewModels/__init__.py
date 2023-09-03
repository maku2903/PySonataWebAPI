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
class EmployeeBankInfo(BaseModel):
    AccountNumber: str
    BankName: str
class EmployeeListElement(BaseModel):
    Position: int
    Place: str
    Code: str
    NIP: str
    Id: int
    Name: str
    Pesel: str
    Surname: str
    Active: bool
class EmployeeAddress(BaseModel):
    Street: str
    City: str
    ApartmentNo: str
    PostCode: str
    HouseNo: str
class Employee(BaseModel):
    SecondName: str
    Surname: str
    Phone: str
    Name: str
    Pesel: str
    BankInfo: "EmployeeBankInfo"
    Id: Optional[int]
    Position: Optional[int]
    Address: "EmployeeAddress"
    NIP: str
    Code: str
    Active: bool
