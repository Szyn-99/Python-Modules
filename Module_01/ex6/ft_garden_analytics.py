""" Classes act like blueprints for objects """
class Plant:
    """ this is a built in method (dunder method) it initialize attributes for instances"""
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.type = "regular"
    """this is an object method, each call grow a plant by 1cm"""
    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")
        return 1
    """same as the type of the previous method, but this one gives basic info"""
    def get_info(self):
        return f"- {self.name}: {self.height}cm"
    """object method, as the name suggest, it returns the height of the plant as a score"""
    def score(self):
        return self.height

"""this class gets the same structure of the class (Plant), we call this inheritance"""
class FloweringPlant(Plant):
    def __init__(self, name, height, color, blooming):
        """super() is a method that calls another method from the base class with similar behaviour"""
        super().__init__(name, height)
        self.color = color
        if(blooming == "blooming"):
            self.blooming = "blooming"
        else:
            self.blooming = "not blooming"
        self.type = "flowering"
    """you may ask how can we use the same function name twice ?, it is possible thanks to polymorphism"""
    def get_info(self):
        return f"{super().get_info()}, {self.color} flowers ({self.blooming})"

"""like the previous class, this one inherit both of the previous classes (Plant) and (Flowering Plant)"""
class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, blooming, points):
        super().__init__(name, height, color, blooming)
        self.points = points
        self.type = "prize"

    def get_info(self):
        return f"{super().get_info()}, Prize points: {self.points}"
    """score calculating for this class is quite different, since we get it's height and value"""
    def score(self):
        return self.height + self.points

"""a class that handles comple"""
class GardenManager:

    all_gardens = []
    gardens_counter = 0
    """nested class, contains a dunder method to initialize extra attributes, that might be used"""
    class GardenStats:
        def __init__(self):
            self.owner_plants = 0
            self.t_growth = 0
            self.types_count = {"regular": 0, "flowering": 0, "prize": 0}
    """ """
    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        self.stats = self.GardenStats()
        GardenManager.all_gardens += [self]
        GardenManager.gardens_counter += 1

    def add_plant(self, plant):
        """Instance Method: Adds a plant and updates stats[cite: 184]."""
        self.plants += [plant]
        """"""
        self.stats.owner_plants += 1
        self.stats.types_count[plant.type] += 1
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_garden(self):
        """Instance Method: Processes growth for all plants."""
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            self.stats.t_growth += plant.grow()

    # Requirement: Static Method
    @staticmethod
    def validate_height(height):
        if height <= 0:
            print("Height validation test: False")
        else:
            print("Height validation test: True")


    # Requirement: Class Method for dynamic networking [cite: 184]
    @classmethod
    def create_garden_network(cls):
        """Processes all gardens in the class registry dynamically[cite: 183]."""
        score_strings = ""
        counter = GardenManager.gardens_counter
        for garden in cls.all_gardens:
            total_score = 0
            # Instead of sum(), we use a standard loop
            for plant in garden.plants:
                # Polymorphism: Each plant knows its own value
                total_score += plant.score()
            if (counter - 1 > 0):
                score_strings += f"{garden.owner}: {total_score}, "
            else:
                score_strings += f"{garden.owner}: {total_score}"
            counter -= 1

        print(f"Garden scores - {score_strings}")

    def generate_report(self):
        """Instance Method: Uses nested helper to show analytics[cite: 184]."""
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(plant.get_info())
        print(
            f"Plants added: {self.stats.owner_plants}, Total growth: {self.stats.t_growth}cm"
        )
        print(
            f"Plant types: {self.stats.types_count['regular']} regular, "
            f"{self.stats.types_count['flowering']} flowering, "
            f"{self.stats.types_count['prize']} prize flowers"
        )
    @classmethod
    def gardens_managed(self):
        """Instance Method: Returns the number of gardens managed."""
        print(f"Total gardens managed: {GardenManager.gardens_counter}")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")

    alice = GardenManager("Alice")
    alice.add_plant(Plant("Oak Tree", 100))
    alice.add_plant(FloweringPlant("Rose", 25, "red", "blooming"))
    alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", "blooming", 10))
    bob = GardenManager("Bob")
    bob.add_plant(Plant("Small Bush", 92))
    szyn = GardenManager("Szyn")
    szyn.add_plant(PrizeFlower("Exotic Orchid", 30, "purple", "not blooming", 20))
    alice.grow_garden()
    alice.generate_report()
    GardenManager.validate_height(101)
    GardenManager.create_garden_network()
    GardenManager.gardens_managed()
