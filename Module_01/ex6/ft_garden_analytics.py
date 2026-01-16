"""Classes act like blueprints for objects"""


class Plant:
    def __init__(self, name: str, height: int) -> None:
        """this is a built in method (dunder method)
         it initialize attributes for instances"""
        self.name = name
        self.height = height
        self.type = "regular"

    def grow(self) -> int:
        """this is an instance method, each call grow a plant by 1cm"""
        self.height += 1
        print(f"{self.name} grew 1cm")
        return 1

    def get_info(self) -> str:
        """same as the type of the previous method,
         but this one gives basic info"""
        return f"- {self.name}: {self.height}cm"

    def score(self) -> int:
        """instance method, as the name suggest,
        it returns the height of the plant as a score"""
        return self.height


class FloweringPlant(Plant):
    """this class gets the same structure
     of the class (Plant), we call this inheritance"""

    def __init__(self, name: str,
                 height: int, color: str, blooming: str) -> None:
        """super() is a method that calls another
         method from the base class with similar behaviour"""
        super().__init__(name, height)
        self.color = color
        if blooming == "blooming":
            self.blooming = "blooming"
        else:
            self.blooming = "not blooming"
        self.type = "flowering"

    def get_info(self) -> str:
        """you may ask how can we use the same function
        name twice ?, it is possible thanks to polymorphism"""
        return f"{super().get_info()}, {self.color} flowers ({self.blooming})"


class PrizeFlower(FloweringPlant):
    """like the previous class, this one inherit both
    of the previous classes (Plant) and (Flowering Plant)"""

    def __init__(self, name: str, height: int,
                 color: str, blooming: str, points: int) -> None:
        super().__init__(name, height, color, blooming)
        self.points = points
        self.type = "prize"

    def get_info(self) -> str:
        return f"{super().get_info()}, Prize points: {self.points}"

    def score(self) -> int:
        """score calculating for this class is quite different,
        since we get it's height and value"""
        return self.height + self.points


class GardenManager:
    """a class that handles comple"""

    all_gardens = []
    gardens_counter = 0

    class GardenStats:
        """nested class, contains a dunder method to
        initialize extra attributes, that might be used"""

        def __init__(self) -> None:
            self.owner_plants = 0
            self.t_growth = 0
            self.types_count = {"regular": 0, "flowering": 0, "prize": 0}

    def __init__(self, owner: str) -> None:
        """initialization of class variables,
        the __init__ is also called constructor"""
        self.owner = owner
        self.plants = []
        self.stats = self.GardenStats()
        GardenManager.all_gardens += [self]
        GardenManager.gardens_counter += 1

    def add_plant(self, plant: Plant) -> None:
        """this method add a plant to the garden of it's owner"""
        self.plants += [plant]
        self.stats.owner_plants += 1
        self.stats.types_count[plant.type] += 1
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_garden(self) -> None:
        """this method grow all plants by iterating
        on all plants of the garden"""
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            self.stats.t_growth += plant.grow()

    def validate_height(height: int) -> None:
        """this method validate a given height"""
        if height <= 0:
            print("Height validation test: False")
        else:
            print("Height validation test: True")

    """here we convert this method to a static method,
    thus not needing an instance to call it"""
    validate_height = staticmethod(validate_height)

    @classmethod
    def create_garden_network(cls) -> None:
        """this method create a network between gardens,
        the idea is showing all scores of each garden and it's owner"""
        score_strings = ""
        counter = GardenManager.gardens_counter
        for garden in cls.all_gardens:
            total_score = 0
            for plant in garden.plants:
                total_score += plant.score()
            if counter - 1 > 0:
                score_strings += f"{garden.owner}: {total_score}, "
            else:
                score_strings += f"{garden.owner}: {total_score}"
            counter -= 1

        print(f"Garden scores - {score_strings}")

    """here we convert this method to a class method,
    avoiding decorators is a must according to the correction sheet"""
    create_garden_network = classmethod(create_garden_network)

    def generate_report(self) -> None:
        """instace method that generates a report for the owner calling it"""
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(plant.get_info())
        print(
            f"Plants added: {self.stats.owner_plants}, "
            f"Total growth: {self.stats.t_growth}cm"
        )
        print(
            f"Plant types: {self.stats.types_count['regular']} regular, "
            f"{self.stats.types_count['flowering']} flowering, "
            f"{self.stats.types_count['prize']} prize flowers"
        )

    def gardens_managed(cls) -> None:
        print(f"Total gardens managed: {GardenManager.gardens_counter}")

    gardens_managed = classmethod(gardens_managed)


def main() -> None:
    """main function meant for testing"""
    print("=== Garden Management System Demo ===")

    alice = GardenManager("Alice")
    alice.add_plant(Plant("Oak Tree", 100))
    alice.add_plant(FloweringPlant("Rose", 25, "red", "blooming"))
    alice.add_plant(
        PrizeFlower("Sunflower", 50, "yellow", "blooming", 10),
    )
    bob = GardenManager("Bob")
    bob.add_plant(Plant("Small Bush", 92))
    alice.grow_garden()
    alice.generate_report()
    GardenManager.validate_height(101)
    GardenManager.create_garden_network()
    GardenManager.gardens_managed()


if __name__ == "__main__":
    """using the pattern {if __name__ == "__main__"} to
    avoid running the program in case of importing it to another module"""
    main()
