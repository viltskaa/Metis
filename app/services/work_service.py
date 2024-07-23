import time
from datetime import datetime
from typing import Optional

from app.database import Work
from app.repositories import WorkRepository
from .parse_datetime import parse_datetime


class WorkService:
    @staticmethod
    def read_all() -> Optional[list[Work]]:
        works = WorkRepository.read_all()

        return works if works is not None else []

    @staticmethod
    def read_all_by_user_id(user_id: int) -> Optional[list[Work]]:
        works = WorkRepository.read_by_user_id(user_id)

        return works if works is not None else []

    @staticmethod
    def get_work(work_id: int) -> Optional[Work]:
        return WorkRepository.read_by_id(work_id)

    @staticmethod
    def insert_work(work_start: str, user_id: int) -> bool:
        return WorkRepository.insert(parse_datetime(work_start), user_id)

    @staticmethod
    def update_work(work_end: str, work_id: int) -> bool:
        return WorkRepository.update(work_id, parse_datetime(work_end))
