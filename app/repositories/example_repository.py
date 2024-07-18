from typing import Optional

from flask import current_app

from app.database import database as db, Example


class ExampleRepository:
    last_error: Optional[Exception] = None

    @staticmethod
    def read_all() -> Optional[list[Example]]:
        try:
            database = db.get_database()
            examples = database.execute('SELECT * FROM example').fetchall()
            print(examples)
            examples = list(map(lambda exmpl: Example(*exmpl), examples))

            return examples
        except Exception as e:
            ExampleRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def insert(name: str) -> bool:
        try:
            database = db.get_database()
            database.execute('INSERT INTO example (name) VALUES (?)', (name,))
            database.commit()
            return True
        except Exception as e:
            ExampleRepository.last_error = e
            current_app.logger.error(e)
            return False
