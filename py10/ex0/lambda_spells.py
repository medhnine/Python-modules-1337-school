def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda value: value["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda value: value["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    try:
        return {
            "max_power": int(max(mages, key=lambda x: x["power"])["power"]),
            "min_power": int(min(mages, key=lambda x: x["power"])["power"]),
            "avg_power": float(
                round(sum(map(lambda x: x["power"], mages)) / len(mages), 2)
            ),
        }
    except Exception as e:
        print(f"an error aquired {e}")
        exit(1)


def main() -> None:
    print("Testing artifact sorter...")
    artifacts: list[dict] = [
        {"name": "Crystal Orb", "power": 85, "type": "relic"},
        {"name": "Fire Staff", "power": 92, "type": "weapon"},
        {"name": "Shadow Dagger", "power": 70, "type": "weapon"},
    ]
    try:
        result = artifact_sorter(artifacts)
        left_name = result[1].get("name", None)
        left_power = result[1].get("power", None)
        right_name = result[0].get("name", None)
        right_power = result[0].get("power", None)
    except Exception as e:
        print(f"an error aquired {e}")
        exit(1)
    print(
        f"{right_name} ({right_power} power) comes before "
        f"{left_name} ({left_power} power)\n"
    )
    words = ["fireball", "heal", "shield"]
    print("Testing spell transformer...")
    print(*spell_transformer(words))

    print("\nTesting mage states...")
    stats = mage_stats(artifacts)
    print(f"max_power: {stats['max_power']}")
    print(f"min_power: {stats['min_power']}")
    print(f"avg_power: {stats['avg_power']}")

    print("\nTesting power filter...")
    min_power: int = 60
    names: list[dict] = power_filter(artifacts, min_power)
    for item in names:
        print(f"item with power >= {min_power} : {item['name']}")


if __name__ == "__main__":
    main()
