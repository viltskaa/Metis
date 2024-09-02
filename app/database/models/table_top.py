from dataclasses import dataclass
from typing import Optional


@dataclass
class TableTop:
    id: int
    width: Optional[float]
    height: Optional[float]
    perimeter: Optional[float]
    depth: Optional[float]
    time_start_assembly: Optional[int]
    time_end_assembly: Optional[int]
    response: Optional[int]
    image_path: Optional[str]
    table_top_pattern_id: Optional[int]
