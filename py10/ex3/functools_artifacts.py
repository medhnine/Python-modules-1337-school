from functools import reduce, partial, lru_cache, singledispatch
import operator
from collections.abc import Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": lambda a, b: a if a > b else b,
        "min": lambda a, b: a if a < b else b,
    }
    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")
    return reduce(operations[operation], spells)


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 2) + memoized_fibonacci(n - 1)


def partial_enchanter(base_enchantment: Callable) -> dict:
    return {
        "fire": partial(base_enchantment, power=50, element="Fire"),
        "ice": partial(base_enchantment, power=50, element="Ice"),
        "lightning": partial(base_enchantment, power=50, element="Lightning"),
    }


def spell_dispatcher() -> Callable:
    @singledispatch
    def cast_spell(spell: object) -> str:
        return "Unknown spell type"

    @cast_spell.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @cast_spell.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @cast_spell.register(list)
    def _(spell: list[object]) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return cast_spell


def my_enchantment(power: int, element: str, target: str) -> str:
    return f"{element} enchantment hits {target} for {power}"


def main() -> None:
    print("Testing spell reducer...")
    val = [10, 20, 50, 20]
    print(f"Sum: {spell_reducer(val, 'add')}")
    print(f"Product: {spell_reducer(val, 'multiply')}")
    print(f"Max: {spell_reducer(val, 'max')}\n")

    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}\n")

    print("Testing partial enchanter...")
    try:
        enchanters = partial_enchanter(my_enchantment)
        print(enchanters["fire"](target="Sword"))
        print(enchanters["ice"](target="Shield"))
        print(enchanters["lightning"](target="Staff"))
    except Exception as e:
        print(f"an error aquired {e}")
        exit(1)

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher(["fireball", "heal", "shield"]))
    print(dispatcher(4.6))


if __name__ == "__main__":
    main()
