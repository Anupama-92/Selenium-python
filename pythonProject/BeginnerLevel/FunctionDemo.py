# In Python, function is a group of related statements that performs a specific task.
# Function Declaration
def demo(name):
    print("Learning functions" + name)
    # Function Call


def addIntegers(a, b):
    return a+b


demo("Anupama")
print(addIntegers(2,10))

# Fibnonacci Number


def Fibonacci(n):
     if n < 0:
        print("Incorrect input")
     elif n == 0:
        return 0
     elif n == 1 or n == 2:
        return 1
     else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


print(Fibonacci(9))

# Factorial of number
# 5 * 4 * 3 * 2 * 1=120


def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


num = 5
print("Factorial of", num, "is", factorial(num))

import math


def factorial(n):
    return math.factorial(n)


# Driver Code
num = 5
print("Factorial of", num, "is",
      factorial(num))
