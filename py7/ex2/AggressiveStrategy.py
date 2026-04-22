from ex2.BattleStrategy import BattleStrategy
from ex0.Creature import Creature
from ex1.TransformCapability import TransformCapability


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Creature):
        if not isinstance(creature, TransformCapability):
            raise Exception(
                "Invalid Creature "
                f"'{creature.name}' "
                "for this aggressive strategy"
            )
        return "\n".join(
            [creature.transform(), creature.attack(True), creature.revert()]
        )

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)
