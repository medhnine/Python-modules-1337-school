from ex0.Creature import Creature
from ex1.TransformCapability import TransformCapability


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")

    def attack(self, again: bool = False) -> str:
        if again:
            return f"{self.name} performs a boosted strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        return f"{self.name} returns to normal."
