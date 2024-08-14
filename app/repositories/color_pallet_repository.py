from typing import Optional

from flask import current_app

from app.database import database as db, ColorPallet


class ColorPalletRepository:
    last_error: Optional[Exception] = None

    @staticmethod
    def read_by_id(color_pallet_id: int) -> Optional[ColorPallet]:
        try:
            database = db.get_database()
            color_pallet_row = database.execute('SELECT * FROM color_pallet WHERE id = ?',
                                                (color_pallet_id,)).fetchone()
            if color_pallet_row:
                color_pallet = ColorPallet(*color_pallet_row)
                return color_pallet
            return None
        except Exception as e:
            ColorPalletRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def read_all() -> Optional[list[ColorPallet]]:
        try:
            database = db.get_database()
            color_pallets = database.execute('SELECT * FROM color_pallet').fetchall()
            color_pallets = list(map(lambda cp: ColorPallet(*cp), color_pallets))

            return color_pallets
        except Exception as e:
            ColorPalletRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def read_all_by_tt_id(table_top_id: int) -> Optional[list[ColorPallet]]:
        try:
            database = db.get_database()
            color_pallets = database.execute('SELECT * FROM color_pallet WHERE table_top_id = ?',
                                             (table_top_id,)).fetchall()
            color_pallets = list(map(lambda cp: ColorPallet(*cp), color_pallets))

            return color_pallets
        except Exception as e:
            ColorPalletRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def insert(surface_type: int, hex_color: str, table_top_id: int) -> Optional[int]:
        try:
            database = db.get_database()
            cursor = database.cursor()

            cursor.execute('INSERT INTO color_pallet (surface_type, hex_color, table_top_id) '
                           'VALUES (?, ?, ?)',
                           (surface_type, hex_color, table_top_id,))

            database.commit()
            last_id = cursor.lastrowid

            return last_id
        except Exception as e:
            ColorPalletRepository.last_error = e
            current_app.logger.error(e)
            return None
