from ex0 import CreatureFactory
from ex1.Shiftling import Shiftling
from ex1.Morphagon import Morphagon


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()
