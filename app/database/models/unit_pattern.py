from dataclasses import dataclass

from app.database.enums import UnitType


@dataclass
class UnitPattern:
    id: int
    article: str
    name: str
    image_path: str
    type: UnitType
