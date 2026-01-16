"""a class that will work
 as a blueprint for objects or as a base class for other classes"""


class Plant:
    """this is the construcor method, where we
    initialize attributes of the instances"""

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    """this method gives basic infos about the current plant"""

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


class Flower(Plant):
    """this class inherit methods and variables
    of the base class {Plant}, we call it derived or child class"""

    def __init__(self, name, height, age, color):
        """the super() method will call the constructor of
        this class parent, thus initializing and reducing code lines"""
        super().__init__(name, height, age)
        self.color = color
        print(
            f"{self.name} (Flower): "
            f"{self.height}cm, {self.age} days, {self.color} color"
        )

    def bloom(self):
        """this method print a string, when calling it"""
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """once again, this is a a child
    class that inherits the characteristics of {Plant}"""

    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        print(
            f"{self.name} (Tree): "
            f"{self.height}cm, {self.age} days, "
            f"{self.trunk_diameter}cm diameter"
        )

    def produce_shade(self):
        height_m = self.height / 100
        shade = 3.14 * height_m**2
        print(f"{self.name} provides {shade:.0f} square meters of shade")


class Vegetable(Plant):
    """same as the last two previous classes, a
    child class that inherits from parent class"""

    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        print(
            f"{self.name} (Vegetable): "
            f"{self.height}cm, {self.age} days, {self.harvest_season} harvest"
        )
        print(f"{self.name} is rich in {self.nutritional_value}")


"""a testing method"""


def test():
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 25, 30, "red")
    rose.bloom()
    oak = Tree("Oak", 500, 1825, 50)
    oak.produce_shade()
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    tomato.get_info()


"""again, this pattern ensures that the test() function
runs only when the script is executed directly"""
if __name__ == "__main__":
    test()
