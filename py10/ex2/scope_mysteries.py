from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    count = 0

    def add_to() -> int:
        nonlocal count
        count += 1
        return count
    return add_to


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    result = initial_power

    def accumulator(value: int) -> int:
        nonlocal result
        result += value
        return result
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def factory(name: str) -> str:
        return f"{enchantment_type} {name}"
    return factory


def memory_vault() -> dict:
    result: dict = {}

    def store(key: str, value: Any) -> None:
        result[key] = value

    def recall(key: str) -> Any:
        return result.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main() -> None:
    print("Testing mage counter...")
    res1 = mage_counter()
    for count in range(1, 3):
        print(f"counter_a call {count}: {res1()}")
    res1 = mage_counter()
    print(f"counter_b call {count}: {res1()}")

    print("\nTesting spell accumulator...")
    res2 = spell_accumulator(100)
    print(f"Base 100, add 20: {res2(20)}")
    print(f"Base 100, add 30: {res2(30)}")

    print("\nTesting enchantment factory...")
    res3 = enchantment_factory("Flaming")
    print(res3("Sword"))
    res3 = enchantment_factory("Frozen")
    print(res3("Shield"))

    print("\nTesting memory vault...")
    res5 = memory_vault()
    a = res5["store"]
    a("secret", 42)
    b = res5["recall"]
    c = b("secret")
    print(f"Store 'secret' = {42}")
    print(f"Recall 'secret': {c}")
    print(f"Recall 'unknown': {b('unknown')}")


if __name__ == "__main__":
    main()
