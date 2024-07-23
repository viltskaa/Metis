from dataclasses import dataclass


@dataclass(
    frozen=True
)
class AdditionalPart:
    id: int
    time_start_assembly: int
    time_end_assembly: int
    article: str
    user_id: int
    table_id: int
