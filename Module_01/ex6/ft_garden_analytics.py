class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 1

    def age_cm(self):
        self.age += 1

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


class FloweringPlant(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(self, name, height, age)
        self.color = color
    def 







class GardenManager:
    gardens_total = 0
    gardens_owners = []
    gardens_owners_stats = []
    def add_plant(self, owner):
        pass
    class GardenStats:
        pass
        