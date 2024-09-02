from typing import Optional

from flask import current_app

from app.database import database as db, TableTopPattern


class TableTopPatternRepository:
    last_error: Optional[Exception] = None

    @staticmethod
    def read_by_id(table_top_pattern_id: int) -> Optional[TableTopPattern]:
        try:
            database = db.get_database()
            table_top_pattern_row = database.execute('SELECT * FROM table_top_pattern '
                                                     'WHERE id = ?', (table_top_pattern_id,)).fetchone()
            if table_top_pattern_row:
                table_top_pattern = TableTopPattern(*table_top_pattern_row)
                return table_top_pattern
            return None
        except Exception as e:
            TableTopPatternRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def read_all() -> Optional[list[TableTopPattern]]:
        try:
            database = db.get_database()
            tops = database.execute('SELECT * FROM table_top_pattern').fetchall()
            tops = list(map(lambda tpp: TableTopPattern(*tpp), tops))

            return tops
        except Exception as e:
            TableTopPatternRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def insert(width: float, height: float, perimeter: float, image_path: str) -> Optional[int]:
        try:
            database = db.get_database()
            cursor = database.cursor()

            cursor.execute('INSERT INTO table_top_pattern (width, height, perimeter, image_path) '
                           'VALUES (?, ?, ?, ?)',
                           (width, height, perimeter, image_path,))

            database.commit()
            last_id = cursor.lastrowid

            return last_id
        except Exception as e:
            TableTopPatternRepository.last_error = e
            current_app.logger.error(f"An error occurred during the insert operation: {e}")
            return None

    @staticmethod
    def update(ttp_id: int, article: str, name: str, material: str, image_path: str) -> Optional[int]:
        try:
            database = db.get_database()
            cursor = database.cursor()

            cursor.execute('UPDATE table_top_pattern SET (article, name, material, image_path) = (?, ?, ?, ?) '
                           'WHERE id = ?',
                           (article, name, material, ttp_id, image_path, ))

            database.commit()
            last_id = cursor.lastrowid

            return last_id
        except Exception as e:
            TableTopPatternRepository.last_error = e
            current_app.logger.error(f"An error occurred during the update operation: {e}")
            return None
