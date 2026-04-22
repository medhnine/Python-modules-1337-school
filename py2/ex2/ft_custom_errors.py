class GardenError(Exception):
    """Base exception for all garden-related errors."""

    def __init__(self, message: str = "A garden error occurred") -> None:
        super().__init__(message)


class PlantError(GardenError):
    """Raised when a plant-related problem is detected."""

    def __init__(self, message: str = "The plant is wilting!") -> None:
        super().__init__(message)


class WaterError(GardenError):
    """Raised when a water-related problem is detected."""

    def __init__(self, message: str = "Not enough water in the tank!") -> None:
        super().__init__(message)


def raise_plant_error(height: int) -> None:
    """Raise PlantError if plant height is below 5 cm."""
    if height < 5:
        raise PlantError()


def raise_water_error(level: int) -> None:
    """Raise WaterError if water level is below 5."""
    if level < 5:
        raise WaterError()


def test_custom_errors() -> None:
    """Demonstrate custom exception creation, raising, and inheritance."""
    print("=== Custom Garden Errors Demo ===\n")

    try:
        print("Testing PlantError...")
        raise_plant_error(3)
    except PlantError as e:
        print("Caught PlantError:", e)

    try:
        print("\nTesting WaterError...")
        raise_water_error(3)
    except WaterError as e:
        print("Caught WaterError:", e)

    print("\nTesting catching all garden errors...")
    try:
        raise_plant_error(3)
    except GardenError as e:
        print("Caught a garden error:", e)

    try:
        raise_water_error(3)
    except GardenError as e:
        print("Caught a garden error:", e)

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
