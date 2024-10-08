from typing import Optional

from flask import current_app

from app.database import database as db, UnitPattern
from app.database.enums import UnitType


class UnitPatternRepository:
    last_error: Optional[Exception] = None

    @staticmethod
    def read_by_id(unit_pattern_id: int) -> Optional[UnitPattern]:
        try:
            database = db.get_database()
            unit_pattern_row = database.execute('SELECT * FROM unit_pattern WHERE id = ?',
                                                        (unit_pattern_id,)).fetchone()
            if unit_pattern_row:
                color_pallet_pattern = UnitPattern(*unit_pattern_row)
                return color_pallet_pattern
            return None
        except Exception as e:
            UnitPatternRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def read_all() -> Optional[list[UnitPattern]]:
        try:
            database = db.get_database()
            unit_patterns = database.execute('SELECT * FROM unit_pattern').fetchall()
            unit_patterns = list(map(lambda up: UnitPattern(*up), unit_patterns))

            return unit_patterns
        except Exception as e:
            UnitPatternRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def insert(article: str, name: str, image_path: str, unit_type: UnitType) -> Optional[int]:
        try:
            database = db.get_database()
            cursor = database.cursor()

            cursor.execute('INSERT INTO unit_pattern (article, name, image_path, type) '
                           'VALUES (?, ?, ?, ?)',
                           (article, name, image_path, unit_type.value, ))

            database.commit()
            last_id = cursor.lastrowid

            return last_id
        except Exception as e:
            UnitPatternRepository.last_error = e
            current_app.logger.error(e)
            return None
