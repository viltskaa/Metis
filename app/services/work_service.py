from app.database import Work
from app.repositories import WorkRepository


class WorkService:
    @staticmethod
    def read_all() -> list[Work]:
        works = WorkRepository.read_all()

        return works if works is not None else []

    @staticmethod
    def read_all_by_user_id(user_id: int) -> list[Work]:
        works = WorkRepository.read_by_user_id(user_id)

        return works if works is not None else []

    @staticmethod
    def get_work(work_id: int) -> Work:
        return WorkRepository.read_by_id(work_id)

    @staticmethod
    def insert_work(work_start: int, user_id: int) -> bool:
        return WorkRepository.insert(work_start, user_id)

    @staticmethod
    def update_work(work_end: int, work_id: int) -> bool:
        return WorkRepository.update(work_id, work_end)
