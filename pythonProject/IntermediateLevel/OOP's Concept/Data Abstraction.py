# Data abstraction is the process of hiding the implementation details and showing only the essential features of an object.
# In Python, data abstraction is typically achieved through encapsulation, where the internal state of an object is hidden from the outside world.

class MyClass:
    # Hidden member of MyClass
    __hiddenVariable = 0

    # A member method that changes
    # __hiddenVariable
    def add(self, increment):
        self.__hiddenVariable += increment
        print(self.__hiddenVariable)

    # Driver code


myObject = MyClass()
myObject.add(2)
myObject.add(5)

# This line causes error
#print(myObject.__hiddenVariable)

# Example 2
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Creating objects of different shapes
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Calling the area method on different objects
print("Area of circle:", circle.area())  # Output: 78.5
print("Area of rectangle:", rectangle.area())  # Output: 24


class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def area(self):
        return self._length * self._width

    def perimeter(self):
        return 2 * (self._length + self._width)


# Example usage
rect = Rectangle(10, 5)
print(rect.area())  # Output: 50
print(rect.perimeter())  # Output: 30
