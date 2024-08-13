from dataclasses import dataclass
from typing import Optional


@dataclass
class Tables:
    id: int
    table_pattern_id: int
    time_start_assembly: Optional[int]
    time_end_assembly: Optional[int]
    table_top_id: Optional[int]
