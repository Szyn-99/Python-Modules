class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.plant_type = "regular"

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")
        return 1

    def get_info(self):
        return f"- {self.name}: {self.height}cm"

    def calculate_value(self):
        """Base score is just the height."""
        return self.height


class FloweringPlant(Plant):
    def __init__(self, name, height, color, blooming):
        super().__init__(name, height)
        self.color = color
        self.blooming = "blooming" if blooming == "blooming" else "not blooming"
        self.plant_type = "flowering"

    def get_info(self):
        return f"{super().get_info()}, {self.color} flowers ({self.blooming})"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, points, blooming):
        super().__init__(name, height, color, blooming)
        self.points = points
        self.plant_type = "prize"

    def get_info(self):
        return f"{super().get_info()}, Prize points: {self.points}"

    def calculate_value(self):
        """Override: Height + Prize points."""
        return self.height + self.points


class GardenManager:
    # Requirement: Class-level registry for dynamic networking [cite: 184]
    all_gardens = []

    # Requirement: Nested Helper Class [cite: 184]
    class GardenStats:
        def __init__(self):
            self.plants_added = 0
            self.total_growth = 0
            self.counts = {"regular": 0, "flowering": 0, "prize": 0}

    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        self.stats = self.GardenStats()
        GardenManager.all_gardens.append(self)

    def add_plant(self, plant):
        """Instance Method: Adds a plant and updates stats[cite: 184]."""
        self.plants.append(plant)
        self.stats.plants_added += 1
        self.stats.counts[plant.plant_type] += 1
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_garden(self):
        """Instance Method: Processes growth for all plants."""
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            self.stats.total_growth += plant.grow()

    # Requirement: Static Method 
    @staticmethod
    def validate_height(height):
        """Utility function: Independent of garden data[cite: 184]."""
        return height > 0

    # Requirement: Class Method for dynamic networking [cite: 184]
    @classmethod
    def create_garden_network(cls):
        """Processes all gardens in the class registry dynamically[cite: 183]."""
        score_strings = []
        
        for garden in cls.all_gardens:
            total_score = 0
            # Instead of sum(), we use a standard loop
            for plant in garden.plants:
                # Polymorphism: Each plant knows its own value
                total_score += plant.calculate_value()
            
            score_strings.append(f"{garden.owner}: {total_score}")
            
        print(f"Garden scores - {', '.join(score_strings)}")

    def generate_report(self):
        """Instance Method: Uses nested helper to show analytics[cite: 184]."""
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(plant.get_info())
        print(f"Plants added: {self.stats.plants_added}, Total growth: {self.stats.total_growth}cm")
        print(f"Plant types: {self.stats.counts['regular']} regular, "
              f"{self.stats.counts['flowering']} flowering, "
              f"{self.stats.counts['prize']} prize flowers")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    
    alice = GardenManager("Alice")
    alice.add_plant(Plant("Oak Tree", 100))
    alice.add_plant(FloweringPlant("Rose", 25, "red", "blooming"))
    alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10, "blooming"))
    
    # Adding Bob to demonstrate dynamic network
    bob = GardenManager("Bob")
    bob.add_plant(Plant("Small Bush", 92))

    alice.grow_garden()
    alice.generate_report()

    print(f"Height validation test: {GardenManager.validate_height(101)}")
    
    # Requirement: Dynamic method working on the manager type itself [cite: 184]
    GardenManager.create_garden_network()
    
    print(f"Total gardens managed: {len(GardenManager.all_gardens)}")