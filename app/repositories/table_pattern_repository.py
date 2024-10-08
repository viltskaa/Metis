from typing import Optional

from flask import current_app

from app.database import database as db, TablePattern


class TablePatternRepository:
    last_error: Optional[Exception] = None

    @staticmethod
    def read_by_id(table_pattern_id: int) -> Optional[TablePattern]:
        try:
            database = db.get_database()
            table_pattern_row = database.execute('SELECT * FROM table_pattern '
                                                     'WHERE id = ?', (table_pattern_id,)).fetchone()
            if table_pattern_row:
                table_pattern = TablePattern(*table_pattern_row)
                return table_pattern
            return None
        except Exception as e:
            TablePatternRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def read_by_ttp_id(table_top_pattern_id: int) -> Optional[TablePattern]:
        try:
            database = db.get_database()
            table_pattern_row = database.execute('SELECT * FROM table_pattern '
                                                     'WHERE table_top_pattern_id = ?', (table_top_pattern_id,)).fetchone()
            if table_pattern_row:
                table_pattern = TablePattern(*table_pattern_row)
                return table_pattern
            return None
        except Exception as e:
            TablePatternRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def read_all() -> Optional[list[TablePattern]]:
        try:
            database = db.get_database()
            tps = database.execute('SELECT * FROM table_pattern').fetchall()
            tps = list(map(lambda tp: TablePattern(*tp), tps))

            return tps
        except Exception as e:
            TablePatternRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def insert(article: str, name: str, image_path: str, ttp_id: int) -> Optional[int]:
        try:
            database = db.get_database()
            cursor = database.cursor()

            cursor.execute('INSERT INTO table_pattern (article, name, image_path, table_top_pattern_id) '
                           'VALUES (?, ?, ?, ?)',
                           (article, name, image_path, ttp_id,))

            database.commit()
            last_id = cursor.lastrowid

            return last_id
        except Exception as e:
            TablePatternRepository.last_error = e
            current_app.logger.error(f"An error occurred during the insert operation: {e}")
            return None
