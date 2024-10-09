from typing import Optional

from app.database import UnitPatternTablePattern
from app.repositories import UnitPatternTablePatternRepository


class UnitPatternTablePatternService:

    @staticmethod
    def read_all() -> Optional[list[UnitPatternTablePattern]]:
        up_tps = UnitPatternTablePatternRepository.read_all()

        return up_tps if up_tps is not None else []

    @staticmethod
    def read_by_id(up_tp_id: int) -> Optional[UnitPatternTablePattern]:
        return UnitPatternTablePatternRepository.read_by_id(up_tp_id)

    @staticmethod
    def read_by_tp_id(table_pattern_id: int) -> Optional[UnitPatternTablePattern]:
        return UnitPatternTablePatternRepository.read_by_tp_id(table_pattern_id)

    @staticmethod
    def read_by_up_id(unit_pattern_id: int) -> Optional[UnitPatternTablePattern]:
        return UnitPatternTablePatternRepository.read_by_up_id(unit_pattern_id)

    @staticmethod
    def insert(table_pattern_id: int, unit_pattern_id: int, units_count: int) -> Optional[int]:
        return UnitPatternTablePatternRepository.insert(table_pattern_id, unit_pattern_id, units_count)
