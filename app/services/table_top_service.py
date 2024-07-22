from app.database import TableTop
from app.repositories import TableTopRepository


class TableTopService:
    @staticmethod
    def read_all() -> list[TableTop]:
        tops = TableTopRepository.read_all()

        return tops if tops is not None else []

    @staticmethod
    def get_top(top_id: int) -> TableTop | None:
        return TableTopRepository.read_by_id(top_id)

    @staticmethod
    def update_top(table_top_id: int, width: float, height: float,
                   perimeter: float, depth: float, color_main: str,
                   color_edge: str, material: str, article: str, time_end_assembly: int) -> bool:
        return TableTopRepository.update(table_top_id, )

    @staticmethod
    def insert_top(time_start_assembly: int, user_id: int) -> bool:
        return TableTopRepository.insert(time_start_assembly, user_id)
