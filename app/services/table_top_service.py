from typing import Optional

from app.database import TableTop
from app.repositories import TableTopRepository


class TableTopService:

    @staticmethod
    def read_all() -> Optional[list[TableTop]]:
        tops = TableTopRepository.read_all()

        return tops if tops is not None else []

    @staticmethod
    def get_top(top_id: int) -> Optional[TableTop]:
        return TableTopRepository.read_by_id(top_id)

    @staticmethod
    def insert_top(time_start_assembly: int, width: float, height: float, perimeter: float, image_path: str) -> int:
        return TableTopRepository.insert(time_start_assembly, width, height, perimeter, image_path)
