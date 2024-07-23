from typing import Optional

from app.database import AdditionalPart
from app.repositories import AdditionalPartRepository


class AdditionalPartService:
    @staticmethod
    def read_all_by_user_id(user_id: int) -> Optional[list[AdditionalPart]]:
        parts = AdditionalPartRepository.read_by_user_id(user_id)

        return parts if parts is not None else []

    @staticmethod
    def read_all_by_table_id(table_id: int) -> Optional[list[AdditionalPart]]:
        parts = AdditionalPartRepository.read_by_table_id(table_id)

        return parts if parts is not None else []

    @staticmethod
    def read_all() -> Optional[list[AdditionalPart]]:
        parts = AdditionalPartRepository.read_all()

        return parts if parts is not None else []

    @staticmethod
    def get_part(part_id: int) -> Optional[AdditionalPart]:
        return AdditionalPartRepository.read_by_id(part_id)

    @staticmethod
    def update_part(part_id: int,
                    time_end_assembly: int,
                    article: str,
                    table_id: int) -> bool:
        return AdditionalPartRepository.update(part_id,
                                               time_end_assembly,
                                               article,
                                               table_id)

    @staticmethod
    def insert_part(time_start_assembly: int, user_id: int) -> bool:
        return AdditionalPartRepository.insert(time_start_assembly, user_id)
