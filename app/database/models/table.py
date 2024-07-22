from dataclasses import dataclass
from typing import List


@dataclass(
    frozen=True
)
class Table:
    id: int
    article: str
    time_end_assembly: int
    time_start_assembly: int
    qr_code: str
    table_top: 'TableTop'
    marketplace_id: int
    user: 'User'
    additional_parts: List['AdditionalPart']
