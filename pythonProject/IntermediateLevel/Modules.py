# Python modules may contain several classes, function and variables etc.
# A file containing a set of functions you want to include in your application.
# Creating module - mymodulename.py
# Use a module - By using import statement.
# Re-naming a module - by using as keyword
import mymodulename as mn
mn.greeting("Anupama")
# Variables in Module-mymodulename.py
a = mn.person1["age"]
print(a)

# Built-in modules
import platform
x= platform.system()
print(x)

# dir() function - list all the function names (or variable names) in a module
y=dir(platform)
print(y)

# To import only parts from a module-using from keyword
from mymodulename import person1
print(person1["age"])
