from dataclasses import dataclass


@dataclass(
    frozen=True
)
class Pallet:
    id: int
    hex_color: str
    tables_id: int
    surface_type: int
