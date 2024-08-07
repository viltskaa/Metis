from dataclasses import dataclass
from typing import Optional


@dataclass
class TablePattern:
    id: int
    article: Optional[str]
    image_path: str
    name: str
    table_top_pattern_id: int
    