class SecurePlant:
    def __init__(self, name, height: int, age: int):
        self.name = name
        self.__height = height
        self.__age = age
        print(f"Plant created: {self.name}")

    def get_height(self):
        return self.__height

    def set_height(self, n_height: int):
        if n_height < 0:
            print(
                f"""Invalid operation attempted: height
                   {n_height}cm [REJECTED]"""
            )
            print("Security: Negative height rejected")
        else:
            self.__height = n_height
            print(f"Height updated: {n_height}cm [OK]")

    def get_age(self):
        return self.__age

    def set_age(self, n_age: int):
        if n_age < 0:
            print(
                f"""Invalid operation attempted:
                   age {n_age} days [REJECTED]"""
            )
            print("Security: Negative age rejected")
        else:
            self.__age = n_age
            print(f"Age updated: {n_age} days [OK]")


print("=== Garden Security System ===")
plant = SecurePlant("Rose", 0, 0)
plant.set_height(25)
plant.set_age(30)
plant.set_height(-5)
print(
    f"""Current plant: {plant.name}
       ({plant.get_height()}cm, {plant.get_age()} days)"""
)
