from dataclasses import dataclass


@dataclass
class Table:
    id: int
    article: str
    time_start_assembly: int
    time_end_assembly: int
    qr_code: str
    table_top_id: int
    marketplace_id: int
    user_id: int
