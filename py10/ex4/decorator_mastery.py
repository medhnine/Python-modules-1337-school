from collections.abc import Callable
from typing import Any
from functools import wraps
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> str:
        print(f"casting {func.__name__}...")
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed_time = time.perf_counter() - start_time
        print(f"Spell completed in {elapsed_time:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            power = args[1]
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying..."
                          f"(attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


@retry_spell(3)
def cast_fireball(stats: dict[str, int]) -> str:
    """Fails if number of goals is below 3."""
    if stats["goal"] < 3:
        stats["goal"] += 1
        raise Exception("Insufficient goals!")

    return "FIREBALL CAST SUCCESSFULLY!"


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and name.replace(" ", "").isalpha()

    @power_validator(10)
    def cast_spell(self, power: int, spell_name: str) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("Testing spell timer...")

    @spell_timer
    def fireball(target: str) -> str:
        return "Fireball cast!"
    print(f"Result: {fireball('Dragon')}\n")

    print("Testing retrying spell...")
    counter: list[int] = [0]

    @retry_spell(3)
    def unstable(target: str, power: int) -> str:
        if counter[0] < 3:
            counter[0] += 1
            raise Exception("Unstable!")
        return "Waaaaaaagh spelled!"
    print(f"{unstable('Dragon', 50)}")

    @retry_spell(1)
    def stable(target: str, power: int) -> str:
        if counter[0] < 1:
            counter[0] += 1
            raise Exception("Unstable!")
        return "Waaaaaaagh spelled!"
    print(f"{stable('Dragon', 50)}\n")

    print("Testing MageGuild...")
    guild: MageGuild = MageGuild()
    print(MageGuild.validate_mage_name("Alex"))
    print(MageGuild.validate_mage_name("X2"))
    print(guild.cast_spell(15, "Lightning"))
    print(guild.cast_spell(5, "Lightning"))


if __name__ == "__main__":
    main()
