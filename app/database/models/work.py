from dataclasses import dataclass


@dataclass
class Work:
    id: int
    work_start: int
    work_end: int
    user_id: int
