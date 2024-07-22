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
            print(tops)
            tops = list(map(lambda tp: TableTop(*tp), tops))

            return tops
        except Exception as e:
            TableTopRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def insert(time_start_assembly: int, user_id: int) -> bool:
        try:
            database = db.get_database()
            database.execute('INSERT INTO table_top (time_start_assembly, user_id) VALUES (?)',
                             (time_start_assembly, user_id,))
            database.commit()
            return True
        except Exception as e:
            TableTopRepository.last_error = e
            current_app.logger.error(e)
            return False

    @staticmethod
    def update(table_top_id: int, width: float, height: float, perimeter: float,
               depth: float, color_main: str, color_edge: str,
               material: str, article: str, time_end_assembly: int) -> bool:
        try:
            database = db.get_database()
            database.execute('UPDATE table_top SET width = ?, height = ?, perimeter = ?, depth = ?, color_main = ?, '
                             'color_edge = ?, material = ?, article = ?, time_end_assembly = ? WHERE id = ?',
                             (width, height, perimeter,
                              depth, color_main, color_edge,
                              material, article, time_end_assembly,
                              table_top_id,))
            database.commit()
            return True
        except Exception as e:
            TableTopRepository.last_error = e
            current_app.logger.error(e)
            return False
