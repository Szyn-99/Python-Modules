class Plant:
    def __init__(self, name, heigth, age):
        self.name = name
        self.heigth = heigth
        self.age = age


lotus = Plant("Lotus", 25, 30)
rose = Plant("rose", 80, 45)
Sunflower = Plant("apah", 24, 80)

print(f"{lotus.name}: {lotus.heigth}cm, {lotus.age} days old")
print(f"{rose.name}: {rose.heigth}cm, {rose.age} days old")
print(f"{Sunflower.name}: {Sunflower.heigth}cm, {Sunflower.age} days old")
