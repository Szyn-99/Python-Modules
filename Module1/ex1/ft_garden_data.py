class Plant:
    """this class represents a plant with a name,
    height, and age, also a blueprint for plant objects"""

    def __init__(self, name: str, height: int, age: int) -> None:
        """constructor method to initialize plant attributes"""
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    """a pattern to run some code only when the script is executed directly"""
    print("=== Garden Plant Registry ===")
    lotus = Plant("Lotus", 25, 30)
    rose = Plant("Rose", 80, 45)
    sunflower = Plant("Sunflower", 24, 80)

    print(f"{lotus.name}: {lotus.height}cm, {lotus.age} days old")
    print(f"{rose.name}: {rose.height}cm, {rose.age} days old")
    print(f"{sunflower.name}: {sunflower.height}cm, {sunflower.age} days old")
