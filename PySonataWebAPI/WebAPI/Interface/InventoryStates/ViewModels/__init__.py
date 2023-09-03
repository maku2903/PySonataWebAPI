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
class InventoryState(BaseModel):
    AmountInStore: Decimal
    ProductId: int
    WarehouseId: int
    AmountToSale: Decimal
