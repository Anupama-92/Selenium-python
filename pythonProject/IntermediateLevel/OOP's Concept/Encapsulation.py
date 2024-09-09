# Encapsulation refers to restricting access to certain parts of an object and hiding the object's internal state.
# In Python, you can achieve encapsulation using private attributes and methods.

class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"

    # Creating a derived class


class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)

    # Driver code


obj1 = Base()
print(obj1.a)


# Example 2
class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        if radius > 0:
            self.__radius = radius
        else:
            print("Radius must be greater than 0.")


# Creating an object of the Circle class
circle = Circle(5)

# Accessing private attribute using getter method
print("Radius:", circle.get_radius())

# Trying to access private attribute directly (will raise an error)
# print(circle.__radius)

# Trying to set negative radius (will be ignored)
circle.set_radius(-2)
print("Radius after setting:", circle.get_radius())


# Single Underscore (_): Indicates a variable is intended for internal use (convention).
# Double Underscore (__): Triggers name mangling to make the variable more private and avoid name collisions, especially in subclasses.

