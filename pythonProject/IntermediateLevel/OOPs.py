# Classes are user defined blueprint or prototype
# Sum, multiplication, addition, constant
# Methods, Class variables, instance variables, constructor etc
class Calculator:
    num = 100    # Class variables
# Using same function syntax inside of class, then we called it as methods.
# # Constructor is one method which is automatically called when you create object for any class
# "init" is a keyword to declare the constructor in python
# Constructor name should not be a class name. It should be init.
# Variables which are defined inside of constructor called instance variables.
# Self keyword is mandatory for calling variable names into method.
# new keyword is not required when you create object.

    def __init__(self, a, b):
        self.a = a       # Instance variables
        self.b = b       # Instance variables
        print("I am called automatically when object is created")

    def getData(self):
        print(" Methods in classes")

    def Summation(self):
        return self.a + self.b


obj = Calculator(2, 3)    # Syntax to create the objects in Python
obj.getData()
print(obj.Summation())


