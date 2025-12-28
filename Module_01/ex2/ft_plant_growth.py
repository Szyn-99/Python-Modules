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


lotus = Plant("Lotus", 19, 89)

for i in range(7):
    lotus.grow()
    lotus.age_cm()
    lotus.get_info()

