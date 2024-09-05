from typing import Annotated, Optional, Sequence, List

from app.database import ColorPalletPattern
from app.repositories import ColorPalletPatternRepository
from app.services.parse_color import colors_to_hex_list
from cv import Color


class ColorPalletPatternService:

    @staticmethod
    def read_all() -> Optional[list[ColorPalletPattern]]:
        cps = ColorPalletPatternRepository.read_all()

        return cps if cps is not None else []

    @staticmethod
    def read_all_by_ttp_id(ttp_id: int) -> Optional[list[ColorPalletPattern]]:
        cps = ColorPalletPatternRepository.read_all_by_ttp_id(ttp_id)

        return cps if cps is not None else []

    @staticmethod
    def get_cpp(cpp_id: int) -> Optional[ColorPalletPattern]:
        return ColorPalletPatternRepository.read_by_id(cpp_id)

    @staticmethod
    def insert_all_cpp(surface_type: int,
                       color_objects: List[Color],
                       table_top_pattern_id: int) -> bool:
        try:
            list_hex = colors_to_hex_list(color_objects)

            for hex_str in list_hex:
                ColorPalletPatternRepository.insert(surface_type, hex_str, table_top_pattern_id)

            return True
        except Exception as e:
            print(f"An error occurred during the insert_all_cpp operation: {e}")
            return False
