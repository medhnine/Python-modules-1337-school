from abc import ABC, abstractmethod
from ex0.Creature import Creature


class BattleStrategy(ABC):

    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass
