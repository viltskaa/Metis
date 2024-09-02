import enum


class StatusType(enum.Enum):
    CREATED = 0
    PROCESSING = 1
    COMPLETED = 2
    CANCELLED = 3
    CHANGE_WORKER = 4
