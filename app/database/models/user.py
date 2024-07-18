from dataclasses import dataclass
from typing import List


@dataclass(
    frozen=True
)
class User:
    id: int
    name: str
    works: List['Work']
    tables: List['Table']
    table_tops: List['TableTop']
    additional_parts: List['AdditionalPart']
