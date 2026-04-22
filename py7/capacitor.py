from ex1 import HealingCreatureFactory
from ex1 import TransformCreatureFactory
from ex1.Bloomelle import Bloomelle
from ex1.Morphagon import Morphagon
from ex1.Shiftling import Shiftling
from ex1.Sproutling import Sproutling


if __name__ == "__main__":
    healing: HealingCreatureFactory = HealingCreatureFactory()
    f1: Sproutling = healing.create_base()
    f2: Bloomelle = healing.create_evolved()

    print("Testing Creature with healing capability\n base:")
    print(f1.describe())
    print(f1.attack())
    print(f1.heal())

    print(" evolved:")

    print(f2.describe())
    print(f2.attack())
    print(f2.heal())
    print()
    print("Testing Creature with transform capability\n base:")
    transform: TransformCreatureFactory = TransformCreatureFactory()
    t1: Shiftling = transform.create_base()
    t2: Morphagon = transform.create_evolved()
    print(f"{t1.describe()}")
    print(f"{t1.attack()}")
    print(f"{t1.transform()}")
    print(f"{t1.attack(True)}")
    print(f"{t1.revert()}")

    print(" evolved:")

    print(f"{t2.describe()}")
    print(f"{t2.attack()}")
    print(f"{t2.transform()}")
    print(f"{t2.attack(True)}")
    print(f"{t2.revert()}")
