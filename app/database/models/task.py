from dataclasses import dataclass
from typing import Optional

from app.database.enums import StatusType, WorkerType


@dataclass
class Task:
    id: int
    start_date: int
    status: StatusType
    worker_type: Optional[WorkerType]
    orders_id: int
