class Plant:
    """Base class representing a plant in the garden."""

    def __init__(self, name: str, height: int) -> None:
        """Initialize a plant with a name and height."""
        self.name = name
        self.height = height

    def get_info(self) -> None:
        """Print basic plant information."""
        print(f"- {self.name}: {self.height}cm")

    def grow(self, number: int, display: bool) -> None:
        """Grow the plant by a given amount."""
        if (number >= 0):
            self.height += number
            if (display):
                print(f"{self.name}: grew 1cm")
        else:
            print("Security: Negative height rejected")

    @classmethod
    def clone_plant(cls, p: 'Plant') -> 'Plant':
        """Create a clone of the plant."""
        return cls(p.name, p.height)


class FloweringPlant(Plant):
    """A plant that produces flowers."""

    def __init__(self, name: str, height: int, color: str) -> None:
        """Initialize a flowering plant with a color."""
        super().__init__(name, height)
        self.color = color

    def flower_info(self) -> None:
        """Print detailed flower information."""
        print(f"{self.name} {self.__class__.__name__}: {self.height}cm,"
              f" {self.color} color ")

    def get_info(self) -> None:
        """Print flowering plant information."""
        print(f"- {self.name}: {self.height}cm, {self.color} flowers"
              f" (blooming)")

    @classmethod
    def clone_plant(cls, p: 'FloweringPlant') -> 'FloweringPlant':
        """Create a clone of the flowering plant."""
        return cls(p.name, p.height, p.color)


class PrizeFlower(FloweringPlant):
    """A flowering plant that can win prizes."""

    def __init__(self, name: str, height: int,
                 color: str, prize_points: int) -> None:
        """Initialize a prize flower with prize points."""
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def get_info(self) -> None:
        """Print prize flower information."""
        print(f"- {self.name}: {self.height}cm, {self.color} flowers"
              f" (blooming), Prize points: {self.prize_points}")

    @classmethod
    def clone_plant(cls, p: 'PrizeFlower') -> 'PrizeFlower':
        """Create a clone of the prize flower."""
        return cls(p.name, p.height, p.color, p.prize_points)


class GardenManager:
    """Manages multiple gardens and their statistics."""

    class GardenStats:
        """Handles garden statistics and scoring."""

        def __init__(self, obj: list) -> None:
            """Initialize stats with a list of plants."""
            self.obj = obj

        @staticmethod
        def height_validation(height: int) -> None:
            """Validate that a height value is positive."""
            if (height > 0):
                print("Height validation test: True")
            else:
                print("Height validation test: False")

        def score_calculation(self) -> int:
            """Calculate total score based on plant heights."""
            score = 0
            for i in self.obj:
                score += i.height
                if (i.__class__.__name__ == "PrizeFlower"):
                    score += 10
            return score

    def __init__(self, manager_name: str) -> None:
        """Initialize the garden manager."""
        self.manager_name = manager_name
        self.gardens: list = []

    def add_garden(self, garden: 'Garden') -> None:
        """Add a garden to the manager."""
        self.gardens.append(garden)


class Garden:
    """Represents a garden owned by a person."""

    def __init__(self, owner: str) -> None:
        """Initialize a garden with an owner."""
        self.owner: str = owner
        self.plants: list = []
        self.total_grew: int = 0
        self.regular: int = 0
        self.flowering: int = 0
        self.prize: int = 0

    def add_plants(self, plant: Plant, display: bool) -> None:
        """Add a plant to the garden."""
        self.plants.append(plant)
        if (display):
            print(f"Added {plant.name} to {self.owner}'s garden")
        if (type(plant).__name__ == Plant.__name__):
            self.regular += 1
        elif (type(plant).__name__ == FloweringPlant.__name__):
            self.flowering += 1
        elif (type(plant).__name__ == PrizeFlower.__name__):
            self.prize += 1

    def get_plants_info(self) -> None:
        """Print info for all plants in the garden."""
        for plant in self.plants:
            plant.get_info()

    def grow_all(self, display: bool) -> None:
        """Grow all plants in the garden by 1cm."""
        if display is True:
            print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(1, display)
            self.total_grew += 1

    def garden_info(self) -> None:
        """Print garden summary statistics."""
        print(f"Plants added: {len(self.plants)}, Total growth:"
              f" {self.total_grew}cm")
        print(f"Plant types: {self.regular} regular, {self.flowering}"
              f" flowering, {self.prize} prize flowers")


def owner_management(element: list, owner: str,
                     display: bool) -> Garden:
    """Create a garden for an owner with cloned plants."""
    ga = Garden(owner)
    x = 0
    while (x < 3):
        ga.add_plants(element[x].clone_plant(element[x]), display)
        x += 1
    return ga


if __name__ == "__main__":
    number_of_plant = 3
    test_height = False
    names = ["Oak Tree", "Rose", "Sunflower"]
    alice_height = [100, 25, 50]
    bob_height = [50, 23, 66]
    heights = [alice_height, bob_height]
    elements = []
    i = 0
    while (i < 2):
        element = []
        p1 = Plant(names[0], heights[i][0])
        element.append(p1)
        p1 = FloweringPlant(names[1], heights[i][1], "red")
        element.append(p1)
        p1 = PrizeFlower(names[2], heights[i][2], "yellow", 10)
        element.append(p1)
        elements.append(element)
        i += 1
    owner = ["Bob", "Alice"]
    print("=== Garden Management System Demo ===\n")
    x = 0
    garden = []
    for i in owner:
        g1 = owner_management(elements[0], owner[x], test_height)
        garden.append(g1)
        test_height = True
        x += 1
    print("\n")
    growth = False
    for i in garden:
        i.grow_all(growth)
        growth = True

    print("\n")
    print(f"=== {garden[1].owner}'s Garden Report ===")
    print("Plants in garden:")
    for i in garden[1].plants:
        i.get_info()
    print("\n")
    garden[0].garden_info()
    print("\n")
    alice_score = GardenManager.GardenStats(elements[0]).score_calculation()
    bob_score = GardenManager.GardenStats(elements[1]).score_calculation()
    GardenManager.GardenStats.height_validation(10)
    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")
    print(f"Total gardens managed: {len(owner)}")
