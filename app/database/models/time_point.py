from dataclasses import dataclass
from typing import Optional

from app.database.enums import StatusType


@dataclass
class TimePoint:
    id: int
    status: Optional[StatusType]
    time: Optional[int]
    task_id: int
    works_id: int
