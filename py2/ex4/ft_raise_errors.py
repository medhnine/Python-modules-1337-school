def check_plant_health(
    plant_name: str,
    water_level: int,
    sunlight_hours: int
) -> None:
    """Validate plant health parameters and
      raise ValueError for invalid inputs."""
    try:
        int(water_level)
        int(sunlight_hours)
    except ValueError as e:
        print(e)
        return
    if plant_name and (1 <= water_level <= 10) and (2 <= sunlight_hours <= 12):
        print(
            f"Plant '{plant_name}' is healthy!\n"
        )
    elif not plant_name:
        raise ValueError(
            "Error: Plant name cannot be empty!\n"
        )
    elif water_level < 1 or water_level > 10:
        if water_level > 10:
            raise ValueError(
                f"Error: Water level {water_level} is too high (max 10)\n"
            )
        else:
            raise ValueError(
                f"Error: Water level {water_level} is too low (min 1)\n"
            )
    elif sunlight_hours < 2 or sunlight_hours > 12:
        if sunlight_hours < 2:
            raise ValueError(
                f"Error: Sunlight hours {sunlight_hours} is too low (min 2)\n"
            )
        else:
            raise ValueError(
                f"Error: Sunlight hours {sunlight_hours} "
                "is too high (max 12)\n"
            )


def test_plant_checks() -> None:
    """Test check_plant_health with valid and invalid inputs."""
    print("=== Garden Plant Health Checker ===\n")
    try:
        print("Testing good values...")
        check_plant_health("tomato", 9, 3)
    except ValueError as e:
        print(e)
    try:
        print("Testing empty plant name...")
        check_plant_health("", 14, 0)
    except ValueError as e:
        print(e)
    try:
        print("Testing bad water level...")
        check_plant_health("tomato", 15, 4)
    except ValueError as e:
        print(e)
    try:
        print("Testing bad sunlight hours...")
        check_plant_health("tomato", 5, 13)
    except ValueError as e:
        print(e)
    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
