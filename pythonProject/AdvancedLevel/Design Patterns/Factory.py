class Dog:
    def __init__(self, name):
        self._name = name
    def speak(self):
        return "Woof!"


class Cat:
        def __init__(self, name):
            self._name = name

        def speak(self):
            return "Meow!"


def get_pet(pet="dog"):
    """The Factory Method"""
    pets = dict(dog=Dog("Hope"),cat = Cat("Peace"))
    return pets[pet]


d=get_pet("dog")
print(d.speak())
c = get_pet("cat")
print(c.speak())

from abc import ABC, abstractmethod


# Example 2:
class creator(ABC):
    def factory_method(self):
        pass

    def some_operation(self):
        product = self.factory_method()
        result = f"Creator: The same creator's code has just worked with {product.operation()}"

        return result


class ConcreteCreator1(creator):
    def factory_method(self):
        return ConcreteProduct1()


class ConcreteCreator2(creator):
    def factory_method(self):
        return ConcreteProduct2()


class Product(ABC):
    def operation(self):
        pass


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"


def client_code(creator: creator) -> None:
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())



