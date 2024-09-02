from typing import Optional

from flask import current_app

from app.database import database as db
from app.database.enums import WorkerType


class WorkerRepository:
    last_error: Optional[Exception] = None

    @staticmethod
    def get_by_name_and_surname(name: str, surname: str, patronymic: str) -> Optional[dict]:
        try:
            database = db.get_database()
            worker_row = database.execute(
                'SELECT * FROM worker WHERE name = ? AND surname = ? AND patronymic = ?', (name, surname, patronymic,)
            ).fetchone()

            if worker_row:
                worker = {
                    'id': worker_row[0],
                    'name': worker_row[1],
                    'surname': worker_row[2],
                    'patronymic': worker_row[3],
                    'type': WorkerType(worker_row[4]),
                    'password_hash': worker_row[5]
                }
                return worker
            return None
        except Exception as e:
            current_app.logger.error(f"An error occurred during the get_by_name_and_surname operation: {e}")
            return None

    @staticmethod
    def insert(name: str, surname: str, patronymic: str, worker_type: WorkerType, password_hash: str) -> \
            Optional[int]:
        try:
            database = db.get_database()
            cursor = database.cursor()

            cursor.execute(
                'INSERT INTO worker (name, surname, patronymic, type, password_hash) VALUES (?, ?, ?, ?, ?)',
                (name, surname, patronymic, worker_type.value, password_hash, )
            )

            database.commit()
            return cursor.lastrowid
        except Exception as e:
            current_app.logger.error(f"An error occurred during the insert operation: {e}")
            return None

    @staticmethod
    def get_by_id(worker_id: int) -> Optional[dict]:
        try:
            database = db.get_database()
            worker_row = database.execute(
                'SELECT * FROM worker WHERE id = ?', (worker_id,)
            ).fetchone()

            if worker_row:
                worker = {
                    'id': worker_row[0],
                    'name': worker_row[1],
                    'surname': worker_row[2],
                    'patronymic': worker_row[3],
                    'type': WorkerType(worker_row[4]),
                    'password_hash': worker_row[5]
                }
                return worker
            return None
        except Exception as e:
            current_app.logger.error(f"An error occurred during the get_by_id operation: {e}")
            return None
