from ex0.Creature import Creature


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__("Torragon", "Water")

    def attack(self, again: bool = False) -> str:
        return f"{self.name} uses Hydro Pump!"
