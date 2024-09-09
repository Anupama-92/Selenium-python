print("hello")

# here are the comments
a = 10
print(a)

Str = "Hello world"
print(str)

b, c, d = 6, 11.5, "Demo"

# Concatenating in python

print("{} {}".format("value is", b))

print(type(b))

# we can get the data typeof a variable with the type() function.
x = 5
y = "John"
print(type(x))
print(type(y))

# If you want to specify the data typeof a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# Variable names are case-sensitive.
a = 4
A = "Sally"
# A will not overwrite 'a'

# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

myVariableName = "John"  # Camel case
MyVariableName = "John"  # Pascal Case
my_variable_name = "John"  # Snake Case

# Many values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# If we have a collection of values in a list, tuple etc. Python allows us to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output Variables
x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# We can also use the + operator to output multiple variables
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# When I tried to combine number & string with + operator, it will throw error
x = 5
y = "John"
print(x + y)

# To overcome the above error, use ',' instead of '+' operator
x = 5
y = "John"
print(x, y)


# Global Variables - Global variables can be used by everyone, both inside of functions and outside.
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


