from typing import Optional

from flask import current_app

from app.database import database as db, Table


class TableRepository:
    last_error: Optional[Exception] = None

    @staticmethod
    def read_by_id(table_id: int) -> Optional[Table]:
        try:
            database = db.get_database()
            table_row = database.execute('SELECT * FROM tables WHERE id = ?', (table_id,)).fetchone()
            if table_row:
                table = Table(*table_row)
                return table
            return None
        except Exception as e:
            TableRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def read_all() -> Optional[list[Table]]:
        try:
            database = db.get_database()
            tables = database.execute('SELECT * FROM tables').fetchall()
            print(tables)
            tables = list(map(lambda tbl: Table(*tbl), tables))

            return tables
        except Exception as e:
            TableRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def insert(time_start_assembly: int, user_id: int) -> bool:
        try:
            database = db.get_database()
            database.execute('INSERT INTO tables (time_start_assembly, user_id) VALUES (?)',
                             (time_start_assembly, user_id,))
            database.commit()
            return True
        except Exception as e:
            TableRepository.last_error = e
            current_app.logger.error(e)
            return False

    @staticmethod
    def update(table_id: int, article: str, qr_code: str, table_top_id: int, marketplace_id: int, time_end_assembly: int) -> bool:
        try:
            database = db.get_database()
            database.execute('UPDATE table_top SET article = ?, qr_code = ?, table_top_id = ?, marketplace_id = ?, '
                             'time_end_assembly = ? WHERE id = ?',
                             (article, qr_code, table_top_id,
                              marketplace_id, time_end_assembly,
                              table_id,))
            database.commit()
            return True
        except Exception as e:
            TableRepository.last_error = e
            current_app.logger.error(e)
            return False
