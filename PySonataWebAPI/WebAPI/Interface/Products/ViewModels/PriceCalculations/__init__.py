from ....Enums import (
    enumPriceCalculationMethod,
    enumSalePriceType,
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
class PriceCalculationProduct(BaseModel):
    Quantity: Decimal
    Id: int
class PriceCalculationProductResult(PriceCalculationProduct):
    Price: Decimal
class PriceCalculationProductCriteria(PriceCalculationProduct):
    pass
class PriceCalculation(BaseModel):
    ContractorId: int
    Currency: str
    PriceType: "enumSalePriceType"
    Date: datetime
    DepartmentId: int
class PriceCalculationCriteria(PriceCalculation):
    CalculationMethod: "enumPriceCalculationMethod"
    Products: List["PriceCalculationProductCriteria"]
class PriceOrderContractor(BaseModel):
    Id: Optional[int]
    Code: str
class PriceOrderProduct(BaseModel):
    Quantity: Decimal
    Code: str
class PriceOrderProductResult(PriceOrderProduct):
    Price: Decimal
    Id: int
class PriceOrder(BaseModel):
    Department: str
    Date: datetime
    SalePriceType: "enumSalePriceType"
    Currency: str
class PriceOrderResult(PriceOrder):
    Products: List["PriceOrderProductResult"]
    Contractor: "PriceOrderContractor"
class PriceOrderProductCriteria(PriceOrderProduct):
    pass
class PriceOrderContractorCriteria(PriceOrderContractor):
    pass
class PriceOrderCriteria(PriceOrder):
    Products: List["PriceOrderProductCriteria"]
    TypeCode: str
    Series: str
    Contractor: "PriceOrderContractorCriteria"
class PriceCalculationResult(PriceCalculation):
    Products: List["PriceCalculationProductResult"]
