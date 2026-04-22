from ex2.BattleStrategy import BattleStrategy
from ex0.Creature import Creature
from ex1.HealCapability import HealCapability


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> str:
        if not isinstance(creature, HealCapability):
            raise Exception(
                "Invalid Creature "
                f"'{creature.name}' for this defensive strategy"
            )
        return f"{creature.attack()}\n{creature.heal()}"
