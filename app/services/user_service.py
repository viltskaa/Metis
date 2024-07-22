from app.database import User
from app.repositories import UserRepository


class UserService:
    @staticmethod
    def read_all() -> list[User]:
        users = UserRepository.read_all()

        return users if users is not None else []

    @staticmethod
    def get_user(user_id: int) -> User:
        return UserRepository.read_by_id(user_id)

    @staticmethod
    def insert_user(name: str) -> bool:
        return UserRepository.insert(name)
