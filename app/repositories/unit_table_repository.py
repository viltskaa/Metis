from typing import Optional

from flask import current_app

from app.database import database as db, UnitTables


class UnitTablesRepository:
    last_error: Optional[Exception] = None

    @staticmethod
    def read_by_id(ut_id: int) -> Optional[UnitTables]:
        try:
            database = db.get_database()
            ut_row = database.execute('SELECT * FROM unit_tables '
                                                     'WHERE id = ?', (ut_id,)).fetchone()
            if ut_row:
                ut = UnitTables(*ut_row)
                return ut
            return None
        except Exception as e:
            UnitTablesRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def read_by_table_id(table_id: int) -> Optional[UnitTables]:
        try:
            database = db.get_database()
            ut_row = database.execute('SELECT * FROM unit_tables '
                                                     'WHERE tables_id = ?', (table_id,)).fetchone()
            if ut_row:
                ut = UnitTables(*ut_row)
                return ut
            return None
        except Exception as e:
            UnitTablesRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def read_by_unit_id(unit_id: int) -> Optional[UnitTables]:
        try:
            database = db.get_database()
            ut_row = database.execute('SELECT * FROM unit_tables '
                                                     'WHERE unit_id = ?', (unit_id,)).fetchone()
            if ut_row:
                ut = UnitTables(*ut_row)
                return ut
            return None
        except Exception as e:
            UnitTablesRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def read_all() -> Optional[list[UnitTables]]:
        try:
            database = db.get_database()
            uts = database.execute('SELECT * FROM unit_tables').fetchall()
            uts = list(map(lambda ut: UnitTables(*ut), uts))

            return uts
        except Exception as e:
            UnitTablesRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def insert(table_id: int, unit_id: int) -> Optional[int]:
        try:
            database = db.get_database()
            cursor = database.cursor()

            cursor.execute('INSERT INTO unit_tables (tables_id, unit_id) '
                           'VALUES (?, ?)',
                           (table_id, unit_id,))

            database.commit()
            last_id = cursor.lastrowid

            return last_id
        except Exception as e:
            UnitTablesRepository.last_error = e
            current_app.logger.error(f"An error occurred during the insert operation: {e}")
            return None
