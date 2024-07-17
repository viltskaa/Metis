from dataclasses import dataclass


@dataclass(
    frozen=True
)
class Example:
    id: int
    name: str
