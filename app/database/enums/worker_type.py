import enum


class WorkerType(enum.Enum):
    taskmaster = 0
    packer = 1
    assembler = 2
