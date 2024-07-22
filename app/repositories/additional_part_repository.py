from typing import Optional

from flask import current_app

from app.database import database as db, AdditionalPart


class AdditionalPartRepository:
    last_error: Optional[Exception] = None

    @staticmethod
    def read_by_id(add_part_id: int) -> Optional[AdditionalPart]:
        try:
            database = db.get_database()
            add_part_row = database.execute('SELECT * FROM additional_part WHERE id = ?', (add_part_id,)).fetchone()
            if add_part_row:
                add_part = AdditionalPart(*add_part_row)
                return add_part
            return None
        except Exception as e:
            AdditionalPartRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def read_all() -> Optional[list[AdditionalPart]]:
        try:
            database = db.get_database()
            parts = database.execute('SELECT * FROM additional_part').fetchall()
            print(parts)
            parts = list(map(lambda prt: AdditionalPart(*prt), parts))

            return parts
        except Exception as e:
            AdditionalPartRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def insert(time_start_assembly: int, user_id: int) -> bool:
        try:
            database = db.get_database()
            database.execute('INSERT INTO additional_part (time_start_assembly, user_id) VALUES (?)',
                             (time_start_assembly, user_id,))
            database.commit()
            return True
        except Exception as e:
            AdditionalPartRepository.last_error = e
            current_app.logger.error(e)
            return False

    @staticmethod
    def update(ad_part_id: int, time_end_assembly: int, article: str, table_id: int) -> bool:
        try:
            database = db.get_database()
            database.execute('UPDATE additional_part SET time_end_assembly = ?, article = ?, table_id = ? WHERE id = ?',
                             (time_end_assembly, article, table_id, ad_part_id,))
            database.commit()
            return True
        except Exception as e:
            AdditionalPartRepository.last_error = e
            current_app.logger.error(e)
            return False
