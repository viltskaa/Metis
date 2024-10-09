from typing import Optional

from flask import current_app

from app.database import database as db, TablePattern, Tables


class TableRepository:
    last_error: Optional[Exception] = None

    @staticmethod
    def read_by_id(table_id: int) -> Optional[Tables]:
        try:
            database = db.get_database()
            table_row = database.execute('SELECT * FROM tables '
                                                     'WHERE id = ?', (table_id,)).fetchone()
            if table_row:
                table = Tables(*table_row)
                return table
            return None
        except Exception as e:
            TableRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def read_by_tt_id(table_top_id: int) -> Optional[Tables]:
        try:
            database = db.get_database()
            table_row = database.execute('SELECT * FROM tables '
                                                     'WHERE table_top_id = ?', (table_top_id,)).fetchone()
            if table_row:
                table = Tables(*table_row)
                return table
            return None
        except Exception as e:
            TableRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def read_by_tp_id(table_pattern_id: int) -> Optional[Tables]:
        try:
            database = db.get_database()
            table_row = database.execute('SELECT * FROM tables '
                                                     'WHERE table_pattern_id = ?', (table_pattern_id,)).fetchone()
            if table_row:
                table = Tables(*table_row)
                return table
            return None
        except Exception as e:
            TableRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def read_all() -> Optional[list[Tables]]:
        try:
            database = db.get_database()
            tables = database.execute('SELECT * FROM tables').fetchall()
            tables = list(map(lambda table: Tables(*table), tables))

            return tables
        except Exception as e:
            TableRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def insert(table_pattern_id: int, time_start_assembly: int, table_top_id: int) -> Optional[int]:
        try:
            database = db.get_database()
            cursor = database.cursor()

            cursor.execute('INSERT INTO tables (table_pattern_id, time_start_assembly, table_top_id) '
                           'VALUES (?, ?, ?)',
                           (table_pattern_id, time_start_assembly, table_top_id,))

            database.commit()
            last_id = cursor.lastrowid

            return last_id
        except Exception as e:
            TableRepository.last_error = e
            current_app.logger.error(f"An error occurred during the insert operation: {e}")
            return None
