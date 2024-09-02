from typing import Optional

from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token

from app.database.enums import WorkerType
from app.repositories import WorkerRepository

bcrypt = Bcrypt()


class AuthorizationService:

    @staticmethod
    def register(name: str, surname: str, patronymic: str, password: str, worker_type: WorkerType) -> Optional[int]:
        if not all([name, surname, password, worker_type, patronymic]):
            return None

        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

        worker_id = WorkerRepository.insert(name, surname, patronymic, worker_type, password_hash)

        if worker_id:
            return worker_id
        else:
            return None

    @staticmethod
    def login(name: str, surname: str, patronymic: str, password: str) -> Optional[str]:
        if not all([name, surname, patronymic, password]):
            return None

        worker = WorkerRepository.get_by_name_and_surname(name, surname, patronymic)

        if worker and bcrypt.check_password_hash(worker['password_hash'], password):
            access_token = create_access_token(identity=worker['id'])
            return access_token
        else:
            return None
