from dataclasses import dataclass
from typing import Optional


@dataclass
class Works:
    id: int
    start_time: int
    end_time: Optional[int]
    worker_id: int
    taskmaster_id: int
