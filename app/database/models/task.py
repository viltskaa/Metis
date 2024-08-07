from dataclasses import dataclass


@dataclass
class Task:
    id: int
    status: str
    created_date: int
    updated_date: int
    exist_table_id: int
    user_id: int
    work_id: int
