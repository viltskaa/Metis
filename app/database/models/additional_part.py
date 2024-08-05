from dataclasses import dataclass
from typing import Optional


@dataclass(
    frozen=True
)
class AdditionalPart:
    id: int
    time_start_assembly: int
    time_end_assembly: int
    time_end_scanning: Optional[int]
    article: str
    user_id: int
    table_id: int
