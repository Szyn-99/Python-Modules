class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


Plants = [
    Plant("Rose", 30, 45),
    Plant("Tulip", 25, 30),
    Plant("Sunflower", 80, 60),
    Plant("Daisy", 15, 20),
    Plant("Orchid", 40, 50),
]
for plant in Plants:
    plant.get_info()
