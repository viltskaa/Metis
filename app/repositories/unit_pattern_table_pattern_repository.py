from typing import Optional

from flask import current_app

from app.database import database as db, TablePattern, Tables, UnitPatternTablePattern


class UnitPatternTablePatternRepository:
    last_error: Optional[Exception] = None

    @staticmethod
    def read_by_id(up_tp_id: int) -> Optional[UnitPatternTablePattern]:
        try:
            database = db.get_database()
            up_tp_row = database.execute('SELECT * FROM unit_pattern_table_pattern '
                                                     'WHERE id = ?', (up_tp_id,)).fetchone()
            if up_tp_row:
                up_tp = UnitPatternTablePattern(*up_tp_row)
                return up_tp
            return None
        except Exception as e:
            UnitPatternTablePatternRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def read_by_tp_id(table_pattern_id: int) -> Optional[UnitPatternTablePattern]:
        try:
            database = db.get_database()
            up_tp_row = database.execute('SELECT * FROM unit_pattern_table_pattern '
                                                     'WHERE table_pattern_id = ?', (table_pattern_id,)).fetchone()
            if up_tp_row:
                up_tp = UnitPatternTablePattern(*up_tp_row)
                return up_tp
            return None
        except Exception as e:
            UnitPatternTablePatternRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def read_by_up_id(unit_pattern_id: int) -> Optional[UnitPatternTablePattern]:
        try:
            database = db.get_database()
            up_tp_row = database.execute('SELECT * FROM unit_pattern_table_pattern '
                                                     'WHERE unit_pattern_id = ?', (unit_pattern_id,)).fetchone()
            if up_tp_row:
                up_tp = UnitPatternTablePattern(*up_tp_row)
                return up_tp
            return None
        except Exception as e:
            UnitPatternTablePatternRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def read_all() -> Optional[list[UnitPatternTablePattern]]:
        try:
            database = db.get_database()
            up_tps = database.execute('SELECT * FROM unit_pattern_table_pattern').fetchall()
            up_tps = list(map(lambda up_tp: UnitPatternTablePattern(*up_tp), up_tps))

            return up_tps
        except Exception as e:
            UnitPatternTablePatternRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def insert(table_pattern_id: int, unit_pattern_id: int, units_count: int) -> Optional[int]:
        try:
            database = db.get_database()
            cursor = database.cursor()

            cursor.execute('INSERT INTO unit_pattern_table_pattern (table_pattern_id, unit_pattern_id, units_count) '
                           'VALUES (?, ?, ?)',
                           (table_pattern_id, unit_pattern_id, units_count,))

            database.commit()
            last_id = cursor.lastrowid

            return last_id
        except Exception as e:
            UnitPatternTablePatternRepository.last_error = e
            current_app.logger.error(f"An error occurred during the insert operation: {e}")
            return None
