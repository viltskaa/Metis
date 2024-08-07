from dataclasses import dataclass


@dataclass
class TableTopPattern:
    id: int
    article: str
    name: str
    width: float
    height: float
    depth: float
    perimeter: float
    material: str
    image_path: str
