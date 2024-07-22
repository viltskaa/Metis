from dataclasses import dataclass


@dataclass(
    frozen=True
)
class AdditionalPart:
    id: int
    time_end_assembly: int
    time_start_assembly: int
    article: str
    user: 'User'
    table: 'Table'
