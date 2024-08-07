from dataclasses import dataclass

from app.database.enums import SurfaceType


@dataclass
class ColorPalletPattern:
    id: int
    surface_type: SurfaceType
    hex_color: str
    table_top_pattern_id: int
