from typing import Optional

from app.database import Pallet
from app.repositories import PalletRepository


class PalletService:
    @staticmethod
    def read_all_by_table_id(table_id: int) -> Optional[list[Pallet]]:
        pallet = PalletRepository.read_by_table_id(table_id)

        return pallet if pallet is not None else []

    @staticmethod
    def read_all_by_table_id_and_surface(table_id: int, surface: int) -> Optional[list[Pallet]]:
        pallet = PalletRepository.read_by_table_id_and_surface(table_id, surface)

        return pallet if pallet is not None else []

    @staticmethod
    def read_all() -> Optional[list[Pallet]]:
        pallet = PalletRepository.read_all()

        return pallet if pallet is not None else []

    @staticmethod
    def get_pallet(pallet_id: int) -> Optional[Pallet]:
        return PalletRepository.read_by_id(pallet_id)

    @staticmethod
    def insert_pallet(hex_color: str, table_id: int, surface: int) -> bool:
        return PalletRepository.insert(hex_color, table_id, surface)
