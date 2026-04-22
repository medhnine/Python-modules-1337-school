class Plant:
    """Represent a plant that can grow and age."""

    def __init__(self, name: str, height: int, plant_age: int) -> None:
        """Initialize a plant."""
        self.name = name
        self.height = height
        self.plant_age = plant_age

    def grow(self) -> None:
        """Increase the plant height by 1cm."""
        self.height += 1

    def age(self) -> None:
        """Increase the plant age by 1 day."""
        self.plant_age += 1

    def get_info(self) -> None:
        """Print plant information."""
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")

    def growth_over_time(self, days: int) -> None:
        """Simulate plant growth over a number of days."""
        for i in range(1, days + 1):
            if i != 1:
                self.grow()
                self.age()
            print(f"=== Day {i} ===")
            self.get_info()


if __name__ == "__main__":
    days = 7
    rose = Plant("Rose", 25, 30)
    old_height = rose.height
    rose.growth_over_time(days)
    print(f"Growth this week: +{(rose.height - old_height)}cm")
