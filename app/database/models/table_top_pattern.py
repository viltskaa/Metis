from dataclasses import dataclass
from typing import Optional


@dataclass
class TableTopPattern:
    id: int
    article: Optional[str]
    name: Optional[str]
    width: float
    height: float
    depth: Optional[float]
    perimeter: float
    material: Optional[str]
    image_path: str
