from typing import Annotated, Optional, Sequence, List

from app.database import UnitPattern
from app.database.enums import UnitType
from app.repositories import UnitPatternRepository


class UnitPatternService:

    @staticmethod
    def read_all() -> Optional[list[UnitPattern]]:
        ups = UnitPatternRepository.read_all()

        return ups if ups is not None else []

    @staticmethod
    def read_by_id(unit_pattern_id: int) -> Optional[UnitPattern]:
        return UnitPatternRepository.read_by_id(unit_pattern_id)

    @staticmethod
    def insert(article: str, name: str, image_path: str, unit_type: UnitType) -> Optional[int]:
        return UnitPatternRepository.insert(article, name, image_path, unit_type)
