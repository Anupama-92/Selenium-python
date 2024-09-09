# The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.
# This function is defined in “functools” module.

# importing functools for reduce()
import functools

# initializing list
lis = [1, 3, 5, 6, 2]

# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a + b, lis))

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))    # Output is The sum of the list elements is : 17 & The maximum element of the list is : 6

# reduce() can also be combined with operator functions to achieve the similar functionality as with lambda functions and makes the code more readable.
# using operator functions

# importing functools for reduce()
import functools

# importing operator for operator functions
import operator

# initializing list
lis = [1, 3, 5, 6, 2]

# using reduce to compute sum of list
# using operator functions
print("The sum of the list elements is : ", end="")
print(functools.reduce(operator.add, lis))

# using reduce to compute product
# using operator functions
print("The product of list elements is : ", end="")
print(functools.reduce(operator.mul, lis))

# using reduce to concatenate string
print("The concatenated product is : ", end="")
print(functools.reduce(operator.add, ["Selenium", "With", "Python"]))

# Output
# The sum of the list elements is : 17
# The product of list elements is : 180
# The concatenated product is : SeleniumWithPython

# Difference between reduce() and accumulate()
#      Reduce()                                                Accumulate()
# 1. Functools module                                       1. Itertools module
# 2. stores the intermediate result and                     2. Returns a iterator containing the intermediate results.
#   only returns the final summation value.                    The last number of the iterator returned is summation
#                                                               value of the list.
# 3. It takes function as 1st and sequence                  3. It takes sequence as 1st argument and
# as 2nd argument.                                                function as 2nd argument.

# using reduce() and accumulate()

# importing itertools for accumulate()
import itertools

# importing functools for reduce()
import functools

# initializing list
lis = [1, 3, 4, 10, 4]

# printing summation using accumulate()
print("The summation of list using accumulate is :", end="")
print(list(itertools.accumulate(lis, lambda x, y: x + y)))

# printing summation using reduce()
print("The summation of list using reduce is :", end="")
print(functools.reduce(lambda x, y: x + y, lis))

# Output is The summation of list using accumulate is :[1, 4, 8, 18, 22]
# The summation of list using reduce is :22

# reduce() function with three parameters


def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value

# Note that the initializer, when not None, is used as the first value instead of the first value from iterable , and after the whole iterable.
tup = (2, 1, 0, 2, 2, 0, 0, 2)
print(reduce(lambda x, y: x + y, tup, 6))    # Output is 15

# Sum of numbers in a list:
from functools import reduce
numbers = [1, 2, 3, 4, 5]
# Using reduce with lambda to calculate the sum of numbers
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # Output: 15


# Find the maximum number in a list:
numbers = [5, 8, 3, 10, 1]
# Using reduce with lambda to find the maximum number
max_number = reduce(lambda x, y: x if x > y else y, numbers)
print(max_number)  # Output: 10


# Concatenate strings in a list:
words = ["hello", "world", "this", "is", "reduce"]
# Using reduce with lambda to concatenate strings
concatenated_string = reduce(lambda x, y: x + y, words)
print(concatenated_string)  # Output: helloworldthisisreduce


# Multiply all numbers in a list:
numbers = [1, 2, 3, 4, 5]
# Using reduce with lambda to multiply all numbers
product_of_numbers = reduce(lambda x, y: x * y, numbers)
print(product_of_numbers)  # Output: 120




