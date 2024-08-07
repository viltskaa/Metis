from dataclasses import dataclass
from typing import Optional


@dataclass
class Orders:
    id: int
    table_top_id: Optional[int]
    table_top_pattern_id: int
    table_pattern_id: int
