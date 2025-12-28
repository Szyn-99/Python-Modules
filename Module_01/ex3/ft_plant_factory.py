class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self._height = height
        self._age = age

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, n_height):
        if n_height <= 0:
            print("Height can not be negative")
        else:
            self._height = n_height

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, n_age):
        if n_age <= 0:
            print("age can not be negative")
        else:
            self._age = n_age
