from dataclasses import dataclass
from typing import Optional


@dataclass
class UnitTables:
    id: int
    unit_id: Optional[int]
    table_id: Optional[int]
