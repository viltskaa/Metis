from typing import Optional

from flask import current_app

from app.database import database as db, Unit


class UnitRepository:
    last_error: Optional[Exception] = None

    @staticmethod
    def read_by_id(unit_id: int) -> Optional[Unit]:
        try:
            database = db.get_database()
            unit_row = database.execute('SELECT * FROM unit WHERE id = ?', (unit_id,)).fetchone()
            if unit_row:
                unit = Unit(*unit_row)
                return unit
            return None
        except Exception as e:
            UnitRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def read_all() -> Optional[list[Unit]]:
        try:
            database = db.get_database()
            units = database.execute('SELECT * FROM unit').fetchall()
            units = list(map(lambda u: Unit(*u), units))

            return units
        except Exception as e:
            UnitRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def insert(time_start_assembly: int,
               up_id: int) -> Optional[int]:
        try:
            database = db.get_database()
            cursor = database.cursor()

            cursor.execute('INSERT INTO unit (time_start_assembly, unit_pattern_id) '
                           'VALUES (?, ?)',
                           (time_start_assembly, up_id, ))

            database.commit()
            last_id = cursor.lastrowid

            return last_id
        except Exception as e:
            UnitRepository.last_error = e
            current_app.logger.error(f"An error occurred during the insert operation: {e}")
            return None
