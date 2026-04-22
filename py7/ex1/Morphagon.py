from ex0.Creature import Creature
from ex1.TransformCapability import TransformCapability


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__('Morphagon', "Normal/Dragon")

    def attack(self, again: bool = False) -> str:
        if again:
            return f"{self.name} unleashes a devastating morph strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        return f"{self.name} stabilizes its form."
