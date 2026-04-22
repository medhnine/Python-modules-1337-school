from ex0 import AquaFactory, FlameFactory
from ex0.CreatureFactory import CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import AggressiveStrategy
from ex2 import BattleStrategy
from ex2 import DefensiveStrategy
from ex2 import NormalStrategy


def battle(
    opponents: list[tuple[CreatureFactory, BattleStrategy]],
    Tournament: str,
) -> None:
    print(f"*** {Tournament} ***")
    print(f"{len(opponents)} opponents involved")
    print()

    for i in range(len(opponents) - 1):
        for j in range(i + 1, len(opponents)):
            res1 = opponents[i][0].create_base()
            res2 = opponents[j][0].create_base()
            print("* Battle *")
            print(res1.describe())
            print(" vs.")
            print(res2.describe())
            print(" now fight!")
            try:
                print(opponents[i][1].act(res1))
                print(opponents[j][1].act(res2))
            except Exception as e:
                print(f"Battle error, aborting tournament: {e}")


def main() -> None:
    f1 = AquaFactory()
    f2 = FlameFactory()
    f3 = HealingCreatureFactory()

    f4 = TransformCreatureFactory()

    st1 = AggressiveStrategy()
    st2 = DefensiveStrategy()
    st3 = NormalStrategy()

    opponents1 = [(f2, st3), (f3, st2)]
    opponents2 = [(f2, st1), (f3, st2)]
    opponents3 = [(f1, st3), (f3, st2), (f4, st1)]

    print("Tournament 0 (basic)")
    print("  [ (Flameling+Normal), (Healing+Defensive) ]")
    battle(opponents1, 'Tournament')
    print()
    print("Tournament 1 (error)")
    print("  [ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle(opponents2, 'Tournament 1')
    print()
    print("Tournament 2 (multiple)")
    print("  [ (Aquabub+Normal), "
          "(Healing+Defensive), (Transform+Aggressive) ]")
    battle(opponents3, 'Tournament 2')


if __name__ == "__main__":
    main()
