from typing import Optional

from flask import current_app

from app.database import database as db, ColorPalletPattern


class ColorPalletPatternRepository:
    last_error: Optional[Exception] = None

    @staticmethod
    def read_by_id(color_pallet_pattern_id: int) -> Optional[ColorPalletPattern]:
        try:
            database = db.get_database()
            color_pallet_pattern_row = database.execute('SELECT * FROM color_pallet_pattern WHERE id = ?',
                                                        (color_pallet_pattern_id,)).fetchone()
            if color_pallet_pattern_row:
                color_pallet_pattern = ColorPalletPattern(*color_pallet_pattern_row)
                return color_pallet_pattern
            return None
        except Exception as e:
            ColorPalletPatternRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def read_all() -> Optional[list[ColorPalletPattern]]:
        try:
            database = db.get_database()
            color_pallet_patterns = database.execute('SELECT * FROM color_pallet_pattern').fetchall()
            color_pallet_patterns = list(map(lambda cpp: ColorPalletPattern(*cpp), color_pallet_patterns))

            return color_pallet_patterns
        except Exception as e:
            ColorPalletPatternRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def read_all_by_ttp_id(table_top_pattern_id: int) -> Optional[list[ColorPalletPattern]]:
        try:
            database = db.get_database()
            color_pallet_patterns = database.execute(
                'SELECT * FROM color_pallet_pattern WHERE table_top_pattern_id = ?',
                (table_top_pattern_id,)).fetchall()
            color_pallet_patterns = list(map(lambda cp: ColorPalletPattern(*cp), color_pallet_patterns))

            return color_pallet_patterns
        except Exception as e:
            ColorPalletPatternRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def insert(surface_type: int, hex_color: str, table_top_pattern_id: int) -> Optional[int]:
        try:
            database = db.get_database()
            cursor = database.cursor()

            cursor.execute('INSERT INTO color_pallet_pattern (surface_type, hex_color, table_top_pattern_id) '
                           'VALUES (?, ?, ?)',
                           (surface_type, hex_color, table_top_pattern_id,))

            database.commit()
            last_id = cursor.lastrowid

            return last_id
        except Exception as e:
            ColorPalletPatternRepository.last_error = e
            current_app.logger.error(e)
            return None
