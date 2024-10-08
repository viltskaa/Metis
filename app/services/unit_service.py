from typing import Optional

from app.database import Unit
from app.repositories import UnitRepository


class UnitService:

    @staticmethod
    def read_all() -> Optional[list[Unit]]:
        units = UnitRepository.read_all()

        return units if units is not None else []

    @staticmethod
    def get_by_id(unit_id: int) -> Optional[Unit]:
        return UnitRepository.read_by_id(unit_id)

    @staticmethod
    def insert(time_start_assembly: int, up_id: int) -> int:
        return UnitRepository.insert(time_start_assembly, up_id)
