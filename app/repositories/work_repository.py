from typing import Optional

from flask import current_app

from app.database import database as db, Work


class WorkRepository:
    last_error: Optional[Exception] = None

    @staticmethod
    def read_by_id(work_id: int) -> Optional[Work]:
        try:
            database = db.get_database()
            work_row = database.execute('SELECT * FROM works WHERE id = ?', (work_id,)).fetchone()
            if work_row:
                work = Work(*work_row)
                return work
            return None
        except Exception as e:
            WorkRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def read_all() -> Optional[list[Work]]:
        try:
            database = db.get_database()
            works = database.execute('SELECT * FROM works').fetchall()
            print(works)
            works = list(map(lambda wrk: Work(*wrk), works))

            return works
        except Exception as e:
            WorkRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def read_by_user_id(user_id: int) -> Optional[list[Work]]:
        try:
            database = db.get_database()
            works = database.execute('SELECT * FROM works WHERE user_id = ?', (user_id,)).fetchall()
            print(works)
            works = list(map(lambda wrk: Work(*wrk), works))

            return works
        except Exception as e:
            WorkRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def insert(work_start: int, user_id: int) -> bool:
        try:
            database = db.get_database()
            database.execute('INSERT INTO works (work_start, user_id) VALUES (?, ?)', (work_start, user_id,))
            database.commit()
            return True
        except Exception as e:
            WorkRepository.last_error = e
            current_app.logger.error(e)
            return False

    @staticmethod
    def update(work_id: int, work_end: int) -> bool:
        try:
            database = db.get_database()
            database.execute('UPDATE works SET work_end = ? WHERE id = ?', (work_end, work_id,))
            database.commit()
            return True
        except Exception as e:
            WorkRepository.last_error = e
            current_app.logger.error(e)
            return False
