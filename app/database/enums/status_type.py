import enum


class StatusType(enum.Enum):
    created = 0
    processing = 1
    completed = 2
    cancelled = 3
    change_worker = 4
