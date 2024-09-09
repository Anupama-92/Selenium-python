from pythonProject.IntermediateLevel.OOPs import Calculator


class ChildImpl(Calculator):
    num2=200

    def __init__(self):
        Calculator.__init__(self, 2, 10)

    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()


obj = ChildImpl()
print(obj.getCompleteData())


# Single Inheritance - A subclass inherits from a single parent class.
class Cat(Animal):
    def speak(self):
        return f"{self.name} meows"

# Multiple Inheritance: A subclass inherits from more than one parent class.
class Animal:
    def __init__(self, name):
        self.name = name

class CanFly:
    def fly(self):
        return f"{self.name} can fly"

class Bird(Animal, CanFly):
    def speak(self):
        return f"{self.name} sings"

# Multilevel Inheritance: A class is derived from another derived class.
class Mammal(Animal):
    def __init__(self, name, has_fur=True):
        super().__init__(name)
        self.has_fur = has_fur

class Dog(Mammal):
    def speak(self):
        return f"{self.name} barks"
# Hierarchical Inheritance: Multiple classes inherit from a single parent class.
class Horse(Animal):
    def speak(self):
        return f"{self.name} neighs"

class Cow(Animal):
    def speak(self):
        return f"{self.name} moos"

