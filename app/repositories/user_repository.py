from typing import Optional

from flask import current_app

from app.database import database as db, User


class UserRepository:
    last_error: Optional[Exception] = None

    @staticmethod
    def read_by_id(user_id: int) -> Optional[User]:
        try:
            database = db.get_database()
            user_row = database.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
            if user_row:
                user = User(*user_row)
                return user
            return None
        except Exception as e:
            UserRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def read_all() -> Optional[list[User]]:
        try:
            database = db.get_database()
            users = database.execute('SELECT * FROM users').fetchall()
            print(users)
            users = list(map(lambda usr: User(*usr), users))

            return users
        except Exception as e:
            UserRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def insert(name: str) -> bool:
        try:
            database = db.get_database()
            database.execute('INSERT INTO users (name) VALUES (?)', (name,))
            database.commit()
            return True
        except Exception as e:
            UserRepository.last_error = e
            current_app.logger.error(e)
            return False
