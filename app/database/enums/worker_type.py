import enum


class WorkerType(enum.Enum):
    TASKMASTER = 0
    PACKER = 1
    ASSEMBLER = 2
