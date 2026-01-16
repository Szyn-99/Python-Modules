class SecurePlant:
    """a class that represents a plant with
    private attributes for height and age"""

    def __init__(self, name, height: int, age: int):
        self.name = name
        self.__height = height
        self.__age = age
        print(f"Plant created: {self.name}")

    """getter method for height"""

    def get_height(self) -> int:
        return self.__height

    """setter method for height with security check"""

    def set_height(self, n_height: int) -> None:
        if n_height < 0:
            print("Invalid operation attempted: "
                  f"height {n_height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = n_height
            print(f"Height updated: {n_height}cm [OK]")

    """getter method for age"""

    def get_age(self) -> int:
        return self.__age

    """setter method for age with security check"""

    def set_age(self, n_age: int) -> None:
        if n_age < 0:
            print("Invalid operation attempted: "
                  f"age {n_age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = n_age
            print(f"Age updated: {n_age} days [OK]")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    """main entry of the program, executing
    only when the script is run directly"""
    plant = SecurePlant("Rose", 0, 0)
    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-5)
    print(
        f"\nCurrent plant: {plant.name} "
        f"({plant.get_height()}cm, {plant.get_age()} days)"
    )
