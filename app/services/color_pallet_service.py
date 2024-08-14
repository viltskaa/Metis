from typing import Optional, Sequence, Annotated

from app.database import ColorPallet
from app.repositories import ColorPalletRepository
from app.services.parse_color import convert_rgb_to_hex_list


class ColorPalletService:

    @staticmethod
    def read_all() -> Optional[list[ColorPallet]]:
        cps = ColorPalletRepository.read_all()

        return cps if cps is not None else []

    @staticmethod
    def read_all_by_tt_id(tt_id: int) -> Optional[list[ColorPallet]]:
        cps = ColorPalletRepository.read_all_by_tt_id(tt_id)

        return cps if cps is not None else []

    @staticmethod
    def get_cp(cp_id: int) -> Optional[ColorPallet]:
        return ColorPalletRepository.read_by_id(cp_id)

    @staticmethod
    def insert_all_cp(surface_type: int, rgb_values: Sequence[Annotated[Sequence[int], 3]], table_top_id: int) -> bool:
        try:
            list_hex = convert_rgb_to_hex_list(rgb_values)

            for hex_str in list_hex:
                ColorPalletRepository.insert(surface_type, hex_str, table_top_id)

            return True
        except Exception as e:
            print(f"An error occurred during the insert_all_cp operation: {e}")
            return False
