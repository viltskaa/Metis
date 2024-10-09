from typing import Optional

from app.database import UnitTables
from app.repositories import UnitTablesRepository


class UnitTableService:

    @staticmethod
    def read_all() -> Optional[list[UnitTables]]:
        uts = UnitTablesRepository.read_all()

        return uts if uts is not None else []

    @staticmethod
    def read_by_id(ut_id: int) -> Optional[UnitTables]:
        return UnitTablesRepository.read_by_id(ut_id)

    @staticmethod
    def read_by_table_id(table_id: int) -> Optional[UnitTables]:
        return UnitTablesRepository.read_by_table_id(table_id)

    @staticmethod
    def read_by_unit_id(unit_id: int) -> Optional[UnitTables]:
        return UnitTablesRepository.read_by_unit_id(unit_id)

    @staticmethod
    def insert(table_id: int, unit_id: int) -> Optional[int]:
        return UnitTablesRepository.insert(table_id, unit_id)
