from dataclasses import dataclass
from typing import Optional


@dataclass
class Unit:
    id: int
    time_start_assembly: Optional[int]
    time_end_assembly: Optional[int]
    unit_pattern_id: Optional[int]
