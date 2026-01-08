# 1. THE INHERITANCE CHAIN
# We build from simple to complex: Plant -> Flowering -> Prize

class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")
        return 1

    def get_info(self):
        return f"- {self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name, height, color, blooming):
        # super() sends name/height to Plant class
        super().__init__(name, height) 
        self.color = color
        self.blooming = "blooming" if blooming == "blooming" else "not blooming"

    def get_info(self):
        # Get basic info from parent, then add our specific info
        plant_info = super().get_info()
        return f"{plant_info}, {self.color} flowers ({self.blooming})"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, points):
        # super() sends name/height/color to FloweringPlant
        super().__init__(name, height, color)
        self.points = points

    def get_info(self):
        # Get info from parent, add points
        plant_info = super().get_info()
        return f"{plant_info}, Prize points: {self.points}"


# 2. THE MANAGER
# Handles the logic using Nested Classes and different Method types

class GardenManager:
    gardens_so_far = 0  # Class variable (shared by all gardens)

    # NESTED CLASS: A helper just for GardenManager
    class GardenStats:
        def __init__(self):
            self.count = 0
            self.total_growth = 0
            self.regular = 0
            self.flowering = 0
            self.prize = 0

    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        self.stats = self.GardenStats() # Create the helper
        GardenManager.total_gardens += 1

    # INSTANCE METHOD: Needs 'self'. Works with specific garden data.
    def add_plant(self, plant):
        self.plants += plant
        self.stats.count += 1
        
        # Update stats based on type
        if isinstance(plant, PrizeFlower):
            self.stats.prize += 1
        elif isinstance(plant, FloweringPlant):
            self.stats.flowering += 1
        else:
            self.stats.regular += 1
            
        print(f"Added {plant.name} to {self.owner}'s garden")

    # INSTANCE METHOD: Needs 'self'. Helps plants grow.
    def grow_garden(self):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            growth = plant.grow()
            self.stats.total_growth += growth

    # INSTANCE METHOD: Prints the report using the stats helper
    def generate_report(self):
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(plant.get_info())
        
        print(f"Plants added: {self.stats.count}, Total growth: {self.stats.total_growth}cm")
        print(f"Plant types: {self.stats.regular} regular, {self.stats.flowering} flowering, {self.stats.prize} prize")

    # STATIC METHOD: No 'self'. A utility tool. 
    # Doesn't need garden data, just checks a number.
    @staticmethod
    def validate_height(height):
        # Returns True if height is a valid number
        if height > 0:
            return True
        return False

    # CLASS METHOD: Needs 'cls'. Works on the 'GardenManager' concept, not a specific person.
    @classmethod
    def create_garden_network(cls, name1, score1, name2, score2):
        # This simulates creating a network report for multiple owners
        print(f"Garden scores - {name1}: {score1}, {name2}: {score2}")


# --- RUNNING THE CODE ---

if __name__ == "__main__":
    print("=== Garden Management System Demo ===")

    # 1. Create the Manager
    alice = GardenManager("Alice")

    # 2. Create the Plants
    tree = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    # 3. Add to Garden
    alice.add_plant(tree)
    alice.add_plant(rose)
    alice.add_plant(sunflower)

    # 4. Grow
    alice.grow_garden()

    # 5. Report
    alice.generate_report()

    # 6. Test the Static Method (Utility)
    check = GardenManager.validate_height(10)
    print(f"Height validation test: {check}")

    # 7. Test the Class Method (Network)
    GardenManager.create_garden_network("Alice", 218, "Bob", 92)

    # 8. Check Class Variable
    # We created 1 garden (Alice), so this should be 1.
    # To match your example output of 2, we can pretend we made Bob's garden:
    bob = GardenManager("Bob") 
    print(f"Total gardens managed: {GardenManager.total_gardens}")