class Plant:
    """Represent a plant created by the factory."""

    def __init__(self, name: str, starting_height: int,
                 starting_age: int) -> None:
        """Initialize a plant with name, height and age."""
        self.name = name
        self.starting_height = starting_height
        self.starting_age = starting_age

    def display(self) -> None:
        """Display plant details."""
        print(f"{self.name} ({self.starting_height}cm,"
              f" {self.starting_age} days)")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    names = ["Rose", "Oak", "Cactus", "Sunflower", "Fern"]
    height = [25, 200, 5, 80, 15]
    age = [30, 365, 90, 45, 120]
    i = 0
    count = 0
    for i in range(5):
        p1 = Plant(names[i], height[i], age[i])
        print("Created: ", end="")
        p1.display()
    print("\nTotal plants created: ", i + 1)


# __new__ builds the object
# __init__ initializes the attributes
