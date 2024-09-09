# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# Syntax - lambda arguments : expression

# Add 10 to argument a, and return the result:
x = lambda a : a + 10
print(x(5))  # output is 15

# Lambda functions can take any number of arguments:
# Multiply argument a with argument b and return the result:
x = lambda a, b : a * b
print(x(5, 6))  # output is 30.


x = lambda a, b, c : a + b + c
print(x(5, 6, 2))  # output is 13

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))    # For double the number
print(mytripler(11))    # For triple the number


# Using Strings
str1 = 'GeeksforGeeks'

upper = lambda string: string.upper()
print(upper(str1))                       # output is GEEKSFORGEEKS


def cube(y):
  return y * y * y


lambda_cube = lambda y: y * y * y
print("Using function defined with `def` keyword, cube:", cube(5))
print("Using lambda function, cube:", lambda_cube(5))


# Python Lambda Function with List Comprehension

is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
for item in is_even_list:
    print(item())

# Python Lambda Function with if-else

Max = lambda a, b : a if(a > b) else b
print(Max(1, 2))

# Python Lambda with Multiple Statements


List = [[2, 3, 4], [1, 4, 16, 64], [3, 6, 9, 12]]

sortList = lambda x: (sorted(i) for i in x)
secondLargest = lambda x, f: [y[len(y) - 2] for y in f(x)]
res = secondLargest(List, sortList)             # Output is [3, 16, 9]

print(res)

# Lambda functions can be used along with built-in functions like filter(), map() and reduce().
# Filter() - This offers an elegant way to filter out all the elements of a sequence “sequence”, for which the function returns True.
# Map() -The function is called with a lambda function and a list and a new list is returned which contains all the lambda-modified items returned by that function for each item
# Reduce() - The function is called with a lambda function and an iterable and a new reduced result is returned. This performs a repetitive operation over the pairs of the iterable. The reduce() function belongs to the functools module.
# Filter out all odd numbers using filter() and lambda function
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(filter(lambda x: (x % 2 != 0), li))
print(final_list)      # output is [5, 7, 97, 77, 23, 73, 61]


# Filter all people having age more than 18, using lambda and filter() function

ages = [13, 90, 17, 59, 21, 60, 5]
adults = list(filter(lambda age: age > 18, ages))

print(adults)        # output is [90, 59, 21, 60]

# Using lambda() Function with map()
# Multiply all elements of a list by 2 using lambda and map() function
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(map(lambda x: x * 2, li))
print(final_list)         # Output is [10, 14, 44, 194, 108, 124, 154, 46, 146, 122]

# Transform all elements of a list to upper case using lambda and map() function
animals = ['dog', 'cat', 'parrot', 'rabbit']
uppered_animals = list(map(lambda animal: animal.upper(), animals))

print(uppered_animals)           # Output is ['DOG', 'CAT', 'PARROT', 'RABBIT']

# Using lambda() Function with reduce()
# A sum of all elements in a list using lambda and reduce() function
from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print(sum)          # Output is 193

# Find the maximum element in a list using lambda and reduce() function
import functools
lis = [1, 3, 5, 6, 2, ]
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))    # Output is The maximum element of the list is : 6