class Plant:
    """Represent a plant with name, height and age."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a plant."""
        self.name = name
        self.height = height
        self.age = age

    def print_info(self) -> None:
        """Print plant information."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    rose.print_info()
    sunflower.print_info()
    cactus.print_info()
