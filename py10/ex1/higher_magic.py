from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifier(target: str, power: int) -> str:
        return (base_spell(target, power * multiplier))
    return amplifier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(target: str, power: int) -> str:
        if condition(target, power):
            return f"{spell(target, power)}"
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return sequence


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heals restores {target} for {power} HP"


def test2(target: str, power: int) -> bool:
    if power > 10 and target:
        return True
    return False


def condition() -> str:
    return "Spell succsed"


def main() -> None:
    try:
        print("Testing spell combiner...")
        combined = spell_combiner(fireball, heal)
        result: tuple = combined('dragon', 30)
        print(f"Combined spell result: {result[0]}, {result[1]}\n")

        print("Testing power amplifier...")
        amplified = power_amplifier(fireball, 3)
        print(f"{amplified('dragon', 30)}\n")

        print("Testing conditional caster...")
        casted = conditional_caster(test2, fireball)
        print(f"{casted('dargon', 13)}\n")

        print("Testing spell sequence...")
        sequenced = spell_sequence([fireball, heal])
        print(f"{sequenced('dragon', 40)}")

    except Exception as e:
        print(f"an error has been aquired {e}")


if __name__ == "__main__":
    main()
