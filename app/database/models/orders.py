from dataclasses import dataclass
from typing import Optional


@dataclass
class Orders:
    id: int
    table_pattern_id: int
    table_id: Optional[int]
