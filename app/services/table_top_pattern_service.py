from typing import Optional

from app.database import TableTopPattern
from app.repositories import TableTopPatternRepository


class TableTopPatternService:

    @staticmethod
    def read_all() -> Optional[list[TableTopPattern]]:
        tops = TableTopPatternRepository.read_all()

        return tops if tops is not None else []

    @staticmethod
    def get_top_pattern(top_id: int) -> Optional[TableTopPattern]:
        return TableTopPatternRepository.read_by_id(top_id)

    @staticmethod
    def insert_top_pattern(width: float, height: float, perimeter: float, image_path: str) -> Optional[int]:
        return TableTopPatternRepository.insert(width, height, perimeter, image_path)

    @staticmethod
    def update_top_pattern(ttp_id: int, article: str, name: str, material: str) -> Optional[int]:
        return TableTopPatternRepository.update(ttp_id, article, name, material)
