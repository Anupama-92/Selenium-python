# A class is a blueprint for creating objects, and an object is an instance of a class
class Computer:
    def config(self):
        print("15, 16GB, 1TB")


comp1 = Computer()
comp2 = Computer()

comp1.config()
comp2.config()

# Example 2


class Car:
    def __init__(self, brand, model):
        self.Brand = brand
        self.Model = model

    def display_info(self):
        print("Brand:", self.Brand)
        print("Model:", self.Model)


# Creating objects of the Car class
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Accessing object attributes and calling methods
car1.display_info()
car2.display_info()




