from typing import Optional

from app.database import TablePattern
from app.repositories import TablePatternRepository


class TablePatternService:

    @staticmethod
    def read_all() -> Optional[list[TablePattern]]:
        tps = TablePatternRepository.read_all()

        return tps if tps is not None else []

    @staticmethod
    def read_by_id(table_pattern_id: int) -> Optional[TablePattern]:
        return TablePatternRepository.read_by_id(table_pattern_id)

    @staticmethod
    def read_by_ttp_id(table_top_pattern_id: int) -> Optional[TablePattern]:
        return TablePatternRepository.read_by_ttp_id(table_top_pattern_id)

    @staticmethod
    def insert(article: str, name: str, image_path: str, ttp_id: int) -> Optional[int]:
        return TablePatternRepository.insert(article, name, image_path, ttp_id)
