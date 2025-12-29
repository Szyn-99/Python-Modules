class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        print(
            f"""{self.name} (Flower): {self.height}cm, 
            {self.age}days, {self.color} color"""
        )

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        print(
            f"""{self.name} (Tree): {self.height}cm, 
            {self.age}days, {self.trunk_diameter} diameter"""
        )

    def produce_shade(self):
        print(
            f"""{self.name} provides {self.trunk_diameter} 
              square meters of shade"""
        )


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        print(
            f"""{self.name} (Vegetable): {self.height}cm, 
            {self.age}days, {self.harvest_season} season"""
        )
        print(f"""{self.name} is rich in {self.nutritional_value}""")
