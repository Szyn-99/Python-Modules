class Plant:
    """a class that will work as a blueprint for plant objects"""

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.agee = age

    """this method will increment the height
    and age of the plant by 1 cm each time it is called"""

    def grow(self) -> None:
        self.height += 1

    """this method will increment the age of the
    plant by 1 day each time it is called"""

    def age(self) -> None:
        self.agee += 1

    """this method will print the plant information"""

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.agee} days old")


if __name__ == "__main__":
    """main entry of the program, executing only
    when the script is run directly"""
    print("=== Day 1 ===")
    plants = [
        Plant("Rose", 25, 30),
        Plant("Lotus", 10, 15),
        Plant("Lily", 12, 20)
    ]
    for plant in plants:
        plant.get_info()
    print()
    growth = 0
    for day in range(6):
        for plant in plants:
            plant.grow()
            plant.age()
        growth += 1
    print("=== Day 7 ===")
    for plant in plants:
        plant.get_info()

    print(f"Growth this week: +{growth}cm")
