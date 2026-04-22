from typing import List, Optional


def water_plants(plant_list: List[Optional[str]]) -> None:
    """Water each plant in the list, using finally to guarantee cleanup."""
    success = True
    try:
        print("Opening watering system")
        for i in plant_list:
            if i is None:
                success = False
                raise ValueError("Cannot water None - invalid plant!")
            print("Watering", i)
    except ValueError as e:
        print("Error:", e)
    finally:
        print("Closing watering system (cleanup)")
        if success:
            print("Watering completed successfully!\n")


def test_watering_system() -> None:
    """Test the watering system with normal and error scenarios."""
    print("=== Garden Watering System ===\n")
    plants = ["tomato", "lettuce", "carrots"]
    print("Testing normal watering...")
    water_plants(plants)

    plants = ["tomato", None]
    print("Testing with error...")
    water_plants(plants)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
