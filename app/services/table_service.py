from typing import Optional

from app.database import Table
from app.repositories import TableRepository


class TableService:
    @staticmethod
    def read_all_by_user_id(user_id: int) -> Optional[list[Table]]:
        tables = TableRepository.read_by_user_id(user_id)

        return tables if tables is not None else []

    @staticmethod
    def read_all() -> Optional[list[Table]]:
        tables = TableRepository.read_all()

        return tables if tables is not None else []

    @staticmethod
    def get_table(table_id: int) -> Optional[Table]:
        return TableRepository.read_by_id(table_id)

    @staticmethod
    def update_table(table_id: int,
                     article: str,
                     qr_code: str,
                     table_top_id: int,
                     marketplace_id: int,
                     time_end_assembly: int) -> bool:
        return TableRepository.update(table_id,
                                      article,
                                      qr_code,
                                      table_top_id,
                                      marketplace_id,
                                      time_end_assembly)

    @staticmethod
    def insert_table(time_start_assembly: int, user_id: int) -> bool:
        return TableRepository.insert(time_start_assembly, user_id)
