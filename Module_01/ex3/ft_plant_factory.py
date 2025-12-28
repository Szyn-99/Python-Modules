class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.__height = height
        self.__age = age

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, n_height):
        if n_height <= 0:
            print("Height can not be negative")
        else:
            self.__height = n_height

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, n_age):
        if n_age <= 0:
            print("age can not be negative")
        else:
            self.__age = n_age
