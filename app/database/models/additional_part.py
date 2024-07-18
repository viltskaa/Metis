from dataclasses import dataclass


@dataclass(
    frozen=True
)
class AdditionalPart:
    id: int
    time_assembly: int
    article: str
    user: 'User'
    table: 'Table'
