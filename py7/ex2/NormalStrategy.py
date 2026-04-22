from ex2.BattleStrategy import BattleStrategy
from ex0.Creature import Creature


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> str:
        return creature.attack()

    def is_valid(self, creature: Creature) -> bool:
        return True
