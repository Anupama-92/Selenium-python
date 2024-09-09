# Polymorphism allows objects of different classes to be treated as objects of a common superclass.
# It enables a single interface to be used for different types of objects.
# In Python, polymorphism is achieved through method overriding and method overloading.
class Bird:

    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")


class sparrow(Bird):

    def flight(self):
        print("Sparrows can fly.")


class ostrich(Bird):

    def flight(self):
        print("Ostriches cannot fly.")


obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()

# Example2


class Animal:
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Woof!"


class Cat(Animal):
    def sound(self):
        return "Meow!"


# Function to demonstrate polymorphism
def make_sound(animal):
    print(animal.sound())


# Creating objects of different classes
dog = Dog()
cat = Cat()

# Calling the make_sound function with different objects
make_sound(dog)  # Output: Woof!
make_sound(cat)  # Output: Meow!

