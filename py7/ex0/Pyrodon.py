from ex0.Creature import Creature


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self, again: bool = False) -> str:
        return f"{self.name} uses Flamethrower!"
