from flask import current_app

from app.database import Example
from app.database import database as db


class ExampleService:
    LAST_ERROR: Exception | None = None

    @staticmethod
    def read_all() -> list[Example] | None:
        try:
            database = db.get_database()
            examples = database.execute('SELECT * FROM example').fetchall()
            print(examples)
            examples = list(map(lambda exmpl: Example(*exmpl), examples))

            return examples
        except Exception as e:
            LAST_ERROR = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def insert_example(name: str) -> bool:
        try:
            database = db.get_database()
            database.execute('INSERT INTO example (name) VALUES (?)', (name, ))
            database.commit()
            return True
        except Exception as e:
            LAST_ERROR = e
            current_app.logger.error(e)
            return False
