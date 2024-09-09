class Computer:

    def __init__(self):
        self.name='Anu'
        self.age=28


# Inheritance allows a class (subclass) to inherit attributes and methods from another class (superclass)
class Vehicle:
    def __init__(self,brand):
        self.brand = brand

    def display_info(self):
        print("Brand:",self.brand)


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display_model(self):
        print("model:", self.model)


# Creating an object of the Car class
car = Car("Toyota", "Corolla")

# Accessing inherited and subclass-specific methods
car.display_info()
car.display_model()
