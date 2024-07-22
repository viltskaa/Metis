from dataclasses import dataclass


@dataclass(
    frozen=True
)
class TableTop:
    id: int
    width: float
    height: float
    perimeter: float
    depth: float
    color_main: str
    color_edge: str
    material: str
    article: str
    time_end_assembly: int
    time_start_assembly: int
    user: 'User'
