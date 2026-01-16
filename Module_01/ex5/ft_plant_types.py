"""a class that will work
 as a blueprint for objects or as a base class for other classes"""


class Plant:
    """this is the construcor method, where we
    initialize attributes of the instances"""

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    """this method gives basic infos about the current plant"""

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"


class Flower(Plant):
    """this class inherit methods and variables
    of the base class {Plant}, we call it derived or child class"""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """the super() method will call the constructor of
        this class parent, thus initializing and reducing code lines"""
        super().__init__(name, height, age)
        self.color = color

    def get_info(self) -> str:
        return (
            f"{super().get_info()}, "f"{self.color} flowers"
        )

    def bloom(self) -> None:
        """this method print a string, when calling it"""
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """once again, this is a a child
    class that inherits the characteristics of {Plant}"""

    def __init__(self, name: str, height:
                 int, age: int, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def get_info(self) -> str:
        return (
            f"{super().get_info()}, "
            f"{self.trunk_diameter}cm diameter"
        )

    def produce_shade(self) -> None:
        height_m = self.height / 100
        shade = 3.14 * height_m**2
        print(f"{self.name} provides {shade:.0f} square meters of shade")


class Vegetable(Plant):
    """same as the last two previous classes, a
    child class that inherits from parent class"""

    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self) -> str:
        return (
            f"{super().get_info()}, {self.harvest_season} harvest"
        )

    def vegetable_value(self) -> str:
        return f"{self.name} is rich in {self.nutritional_value}"


"""a testing method"""


def test() -> None:
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 25, 30, "red")
    print(rose.get_info())
    rose.bloom()
    lotus = Flower("Lotus", 15, 20, "pink")
    print(lotus.get_info())
    lotus.bloom()
    print()

    sapling = Tree("Sapling", 100, 365, 10)
    print(sapling.get_info())
    sapling.produce_shade()
    oak = Tree("Oak", 500, 1825, 50)
    print(oak.get_info())
    oak.produce_shade()
    print()

    potato = Vegetable("Potato", 60, 120, "autumn", "carbohydrates")
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")

    print(potato.get_info())
    print(potato.vegetable_value())

    print(tomato.get_info())
    print(tomato.vegetable_value())


"""again, this pattern ensures that the test() function
runs only when the script is executed directly"""
if __name__ == "__main__":
    test()
