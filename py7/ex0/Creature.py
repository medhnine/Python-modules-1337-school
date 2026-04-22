from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, creature_type: str) -> None:
        self.name = name
        self.type = creature_type

    @abstractmethod
    def attack(self, again: bool = False) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"
