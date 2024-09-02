from typing import Optional

from flask import current_app

from app.database import database as db, TableTop


class TableTopRepository:
    last_error: Optional[Exception] = None

    @staticmethod
    def read_by_id(table_top_id: int) -> Optional[TableTop]:
        try:
            database = db.get_database()
            table_top_row = database.execute('SELECT * FROM table_top WHERE id = ?', (table_top_id,)).fetchone()
            if table_top_row:
                table_top = TableTop(*table_top_row)
                return table_top
            return None
        except Exception as e:
            TableTopRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def read_all() -> Optional[list[TableTop]]:
        try:
            database = db.get_database()
            tops = database.execute('SELECT * FROM table_top').fetchall()
            tops = list(map(lambda tp: TableTop(*tp), tops))

            return tops
        except Exception as e:
            TableTopRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def insert(time_start_assembly: int,
               width: float,
               height: float,
               perimeter: float,
               image_path: str,
               ttp_id: int) -> Optional[int]:
        try:
            database = db.get_database()
            cursor = database.cursor()

            cursor.execute('INSERT INTO table_top (time_start_assembly, width, height, perimeter, image_path, table_top_pattern_id) '
                           'VALUES (?, ?, ?, ?, ?, ?)',
                           (time_start_assembly, width, height, perimeter, image_path, ttp_id, ))

            database.commit()
            last_id = cursor.lastrowid

            return last_id
        except Exception as e:
            TableTopRepository.last_error = e
            current_app.logger.error(f"An error occurred during the insert operation: {e}")
            return None
