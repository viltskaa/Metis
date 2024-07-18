from dataclasses import dataclass


@dataclass(
    frozen=True
)
class Work:
    id: int
    work_start: int
    work_end: int
    user: 'User'
