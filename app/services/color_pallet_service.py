from typing import Optional, List

from app.database import ColorPallet
from app.repositories import ColorPalletRepository


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
    def insert_all_cp(surface_type: int, colors: List[str], table_top_id: int) -> bool:
        try:
            for hex_str in colors:
                ColorPalletRepository.insert(surface_type, hex_str, table_top_id)

            return True
        except Exception as e:
            print(f"An error occurred during the insert_all_cp operation: {e}")
            return False
