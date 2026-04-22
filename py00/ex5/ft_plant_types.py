class Plant:
    """Base class representing a plant."""

    def __init__(self, name: str, height: int,
                 age: int) -> None:
        """Initialize a plant."""
        self.name = name
        self.height = height
        self.age = age

    def plant_info(self) -> None:
        """Print plant information"""
        print(f"{self.name} ({self.__class__.__name__}): {self.height}cm,"
              f" {self.age} days,", end="")


class Flower(Plant):
    """A plant that produces flowers."""

    def __init__(self, name: str, height: int,
                 age: int, color: str) -> None:
        """Initialize a flower with a color."""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """Display bloom message."""
        print(f"{self.name} is blooming beautifully!\n")

    def plant_info(self) -> None:
        super().plant_info()
        print(f" {self.color} color ")


class Tree(Plant):
    """A plant that represents a tree."""

    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int,
                 meters: int) -> None:
        """Initialize a tree with trunk diameter."""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.meters = meters

    def produce_shade(self) -> None:
        """Display shade information."""
        print(f"{self.name} provides {self.meters}"
              f" square meters of shade\n")

    def plant_info(self) -> None:
        super().plant_info()
        print(f" {self.trunk_diameter} diameter")


class Vegetable(Plant):
    """A plant that represents a vegetable."""

    def __init__(self, name: str, height: int,
                 age: int, season: str) -> None:
        """Initialize a vegetable with a season."""
        super().__init__(name, height, age)
        self.season = season

    def harvest_season(self) -> None:
        """Display harvest information."""
        print(f"{self.name} is rich in vitamin C")

    def plant_info(self) -> None:
        super().plant_info()
        print(f" {self.season} harvest")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")

    flower = Flower("Rose", 500, 30, "red")
    flower.plant_info()
    flower.bloom()

    tree = Tree("Oak", 500, 1825, 50, 78)
    tree.plant_info()
    tree.produce_shade()

    vege = Vegetable("Tomato", 80, 90, "summer")
    vege.plant_info()
    vege.harvest_season()
