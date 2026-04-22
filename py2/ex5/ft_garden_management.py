from typing import List, Optional


class GardenManager:
    """Manage a garden with planting, watering, and health checking."""

    def __init__(self, garden: List[str]) -> None:
        """Initialize the garden manager with a list of plants."""
        self.garden = garden
        self.tank = 50

    def add_plants(self, plants: List[Optional[str]]) -> None:
        """Add plants to the garden, raising PlantError for invalid names."""
        print("Adding plants to garden...")
        try:
            for i in plants:
                if not i:
                    raise PlantError("Error adding plant: "
                                     "Plant name cannot be empty!")
                else:
                    self.garden.append(i)
                    print(f"Added {i} successfully")
        except PlantError as e:
            print(e)
        finally:
            print("System recovered and continuing...")

    def water_plants(self, plant_list: List[Optional[str]]) -> None:
        """Water plants using try/finally to guarantee cleanup."""
        print("Watering plants...")
        success = True
        try:
            print("Opening watering system")
            for i in plant_list:
                if not i:
                    success = False
                    raise WaterError("Cannot water None - invalid plant!")
                print("Watering", i)
        except WaterError as e:
            print("Error:", e)
        finally:
            print("Closing watering system (cleanup)")
        if success:
            print("Watering completed successfully!\n")

    def check_plant_health(
        self, plant_name: str, water_level: int, sunlight_hours: int
    ) -> None:
        """Check plant health and raise ValueError for invalid parameters."""
        try:
            if (
                plant_name
                and (1 <= water_level <= 10)
                and (2 <= sunlight_hours <= 12)
            ):
                print(
                    f"{plant_name}: healthy (water: {water_level}, "
                    f"sun: {sunlight_hours})"
                )
            elif not plant_name:
                raise ValueError("Error: Plant name cannot be empty!\n")
            elif water_level < 1 or water_level > 10:
                if water_level > 10:
                    raise ValueError(
                        f"Error checking {plant_name}: "
                        f"Water level {water_level} is too high (max 10)"
                    )
                else:
                    raise ValueError(
                        f"Error checking {plant_name}: "
                        f"Water level {water_level} is too low (min 1)"
                    )
            elif sunlight_hours < 2 or sunlight_hours > 12:
                if sunlight_hours < 2:
                    raise ValueError(
                        f"Error checking {plant_name}: "
                        f"Sunlight hours {sunlight_hours} is too low (min 2)"
                    )
                else:
                    raise ValueError(
                        f"Error checking {plant_name}: "
                        f"Sunlight hours {sunlight_hours} is too high (max 12)"
                    )
        except ValueError as e:
            print(e)


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


def water_error(height: int, garden: List[str]) -> None:
    """Raise WaterError if water height is below 5."""
    if height < 5:
        raise WaterError()


def test_garden_management() -> None:
    """Test the garden management system with various scenarios."""
    print("=== Garden Management System ===\n")
    garden = []
    plants = ["tomato", "lettuce", None]
    a = GardenManager(garden)
    try:
        a.add_plants(plants)
    except PlantError as e:
        print(e)
    print("\n")
    a.water_plants(plants)
    print("\n")
    print("Checking plant health...")
    a.check_plant_health("tomato", 8, 6)
    a.check_plant_health("lettuce", 15, 6)
    print("\n")
    print("Testing error recovery...")
    try:
        water_error(3, garden)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("System recovered and continuing...\n")
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
