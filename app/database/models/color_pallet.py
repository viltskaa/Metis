from dataclasses import dataclass
from typing import Optional

from app.database.enums import SurfaceType


@dataclass
class ColorPallet:
    id: int
    surface_type: Optional[SurfaceType]
    hex_color: Optional[str]
    table_top_id: Optional[int]
