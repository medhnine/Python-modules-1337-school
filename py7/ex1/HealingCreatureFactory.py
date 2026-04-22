from ex0 import CreatureFactory
from ex1.Bloomelle import Bloomelle
from ex1.Sproutling import Sproutling


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Sproutling:
        return Sproutling()

    def create_evolved(self) -> Bloomelle:
        return Bloomelle()
