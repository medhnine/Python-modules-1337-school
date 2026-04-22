from ex0 import FlameFactory, AquaFactory
from ex0.Creature import Creature
from ex0.CreatureFactory import CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base: Creature = factory.create_base()
    evolved: Creature = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    c1: Creature = factory1.create_base()
    c2: Creature = factory2.create_base()
    print("Testing battle")
    print(c1.describe())
    print(" vs.")
    print(c2.describe())
    print(" fight!")
    print(c1.attack())
    print(c2.attack())


if __name__ == "__main__":
    flame: FlameFactory = FlameFactory()
    aqua: AquaFactory = AquaFactory()
    test_factory(flame)
    print()
    test_factory(aqua)
    print()
    battle(flame, aqua)
