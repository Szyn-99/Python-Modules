class Plant:
    """a class that will work as a blueprint for plant objects"""

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.agee = age

    """this method will increment the height and age of the plant by 1 cm each time it is called"""

    def grow(self):
        self.height += 1

    """this method will increment the age of the plant by 1 day each time it is called"""

    def age(self):
        self.agee += 1

    """this method will print the plant information"""

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.agee} days old")


if __name__ == "__main__":
    """main entry of the program, executing only when the script is run directly"""
    print("=== Day 1 ===")
    rose = Plant("Rose", 25, 30)
    rose.get_info()

    heigth = rose.height
    for day in range(6):
        rose.grow()
        rose.age()
    print("=== Day 7 ===")
    rose.get_info()

    growth = rose.height - heigth
    print(f"Growth this week: +{growth}cm")
