from dataclasses import dataclass
from typing import Optional


@dataclass
class UnitOrders:
    id: int
    units_count: Optional[int]
    unit_id: Optional[int]
    orders_id: int
    unit_pattern_id: int
