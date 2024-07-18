from app.database import Example
from app.repositories import ExampleRepository


class ExampleService:
    @staticmethod
    def read_all() -> list[Example]:
        examples = ExampleRepository.read_all()

        return examples if examples is not None else []

    @staticmethod
    def insert_example(name: str) -> bool:
        return ExampleRepository.insert(name)
