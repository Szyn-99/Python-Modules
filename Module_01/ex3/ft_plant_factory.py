class Plant:
    """a class that will work as a blueprint for plant objects"""

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        """this method will print the plant information"""
        return f"{self.name} ({self.height}cm, {self.age} days old)"


if __name__ == "__main__":
    """main entry of the program, executing
    only when the script is run directly"""
    print("=== Plant Factory Output ===")
    plants = [
        Plant("Rose", 30, 45),
        Plant("Tulip", 25, 30),
        Plant("Sunflower", 80, 60),
        Plant("Daisy", 15, 20),
        Plant("Orchid", 40, 50),
    ]
    plants_count = 0
    for plant in plants:
        print(f"Created: {plant.get_info()}")
        plants_count += 1

    print(f"\nTotal plants created: {plants_count}")
