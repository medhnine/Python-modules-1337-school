from ex0.CreatureFactory import CreatureFactory
from ex0.Aquabub import Aquabub
from ex0.Torragon import Torragon


class AquaFactory(CreatureFactory):
    def create_base(self) -> Aquabub:
        return Aquabub()

    def create_evolved(self) -> Torragon:
        return Torragon()
