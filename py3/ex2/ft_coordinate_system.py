"""Exercise 2: Position Tracker.

Demonstrates tuple operations with 3D coordinates.
"""
from sys import argv
import math


def main() -> None:
    """Parse 3D coordinates and demonstrate tuple unpacking."""
    store = []
    index = 1
    ac = len(argv)
    if ac == 1:
        print("=== Game Coordinate System ===\n")
        print(
            "No coordinates provided. "
            "Usage: python3 ft_coordinate_system.py <x,y,z>"
        )
        return
    print("=== Game Coordinate System ===\n")
    while (index < ac):
        elements = argv[index].split(',')
        for i in elements:
            try:
                i = float(i)
                store.append(float(i))
            except ValueError as e:
                print(f"Error parsing coordinates: {e}")
                return
        index += 1
    if len(store) != 3:
        print("Error: exactly 3 coordinates (x,y,z) are required")
        return
    initial_coordinate = tuple(store)
    x1, y1, z1 = initial_coordinate
    target_coordinate = (0, 0, 0)
    x2, y2, z2 = target_coordinate
    distance = math.sqrt(
        (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2
    )
    if ac == 2:
        print(f'Parsing coordinates: "{argv[1]}"')
        print(f"Parsed position: {initial_coordinate}")
    else:
        print("Position created: ", initial_coordinate)
    print(
        f"Distance between {target_coordinate}"
        f" and {initial_coordinate} : {distance:.2f}"
    )
    print("\n")
    print("Unpacking demonstration:")
    print(f"Player at x={x1}, y={y1}, z={z1}")
    print(f"Coordinates: X={x1}, Y={y1}, Z={z1}")


if __name__ == "__main__":
    main()
