from dataclasses import dataclass

from app.database.enums import WorkerType


@dataclass
class Worker:
    id: int
    name: str
    surname: str
    patronymic: str
    type: WorkerType
