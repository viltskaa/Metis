from typing import Optional

from app.database import TablePattern, Tables
from app.repositories import TablePatternRepository, TableRepository


class TableService:

    @staticmethod
    def read_all() -> Optional[list[Tables]]:
        tables = TableRepository.read_all()

        return tables if tables is not None else []

    @staticmethod
    def read_by_id(table_id: int) -> Optional[Tables]:
        return TableRepository.read_by_id(table_id)

    @staticmethod
    def read_by_tt_id(table_top_id: int) -> Optional[Tables]:
        return TableRepository.read_by_tt_id(table_top_id)

    @staticmethod
    def read_by_tp_id(table_pattern_id: int) -> Optional[Tables]:
        return TableRepository.read_by_tp_id(table_pattern_id)

    @staticmethod
    def insert(table_pattern_id: int, time_start_assembly: int, table_top_id: int) -> Optional[int]:
        return TableRepository.insert(table_pattern_id, time_start_assembly, table_top_id)
