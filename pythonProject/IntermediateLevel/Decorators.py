# Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of a function or class.
# Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it.
# Decorators are functions that modify the behavior of other functions or methods.

# Function Decorator:
def my_decorator(func):
    def wrapper():
        print("Something is happened before function called")
        func()
        print("Something happened after the function called")
    return wrapper


@my_decorator   # say_hello = my_decorator(say_hello)
def say_hello():
    print("Hello")

say_hello()

# Class methods Decorator:


def log_method_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling method: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


class MyClass:
    @log_method_call
    def my_method(self):
        print("Executing my_method")


obj = MyClass()
obj.my_method()

# Decorators with arguments:


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeat(3)
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")


# Decorators are extensively used in frameworks like Flask and Django for creating routes, authentication, logging, etc.,
# making them an essential tool in Python for code organization and reuse.















#  Treating the functions as objects.
def shout(text):
    return text.upper()


print(shout('Hello'))

yell = shout

print(yell('Hello'))

# Passing the function as an argument

def shout(text):
    return text.upper()
def whisper(text):
    return text.lower()
def greet(func):
    # storing the function in a variable
    greeting = func("""Hi, I am created by a function passed as an argument.""")
    print(greeting)


greet(shout)
greet(whisper)

# Returning functions from another function.

def create_adder(x):
    def adder(y):
        return x + y

    return adder


add_15 = create_adder(15)

print(add_15(10))


def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    print(a/b)

divide(2,5)

divide(2,0)