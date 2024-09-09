# Arrays are used to store multiple values in one single variable
cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)
# Modify the value
cars[0] = "Toyota"
x = len(cars)
print(x)
# Looping the array elements
for x in cars:
  print(x)
# Adding array elements
cars.append("Honda")
# Removing array elements
cars.pop(1)
print(cars)
# Accessing the elements in the array
import array as arr
a = arr.array('i', [1, 2, 3, 4, 5, 6])
print("Access element is: ", a[0])
print("Access element is: ", a[3])
b = arr.array('d', [2.5, 3.2, 3.3])
print("Access element is: ", b[1])
print("Access element is: ", b[2])
# Adding elements to the array
a = arr.array('i', [1, 2, 3])
print("Array before insertion : ", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")
print()
a.insert(1, 4)
print("Array after insertion : ", end=" ")
for i in (a):
    print(i, end=" ")
print()
b = arr.array('d', [2.5, 3.2, 3.3])
print("Array before insertion : ", end=" ")
for i in range(0, 3):
    print(b[i], end=" ")
print()
b.append(4.4)
print("Array after insertion : ", end=" ")
for i in (b):
    print(i, end=" ")
print()
# Counting elements in the array
my_array = arr.array('i', [1, 2, 3, 4, 2, 5, 2])
count = my_array.count(2)
print("Number of occurrences of 2:", count)
# Reversing the elements in the array
my_array = arr.array('i', [1, 2, 3, 4, 5])
print("Original array:", *my_array)
my_array.reverse()
print("Reversed array:", *my_array)

from array import *
vals = array('i',[2,5,9,8,6])
print(vals.buffer_info())
newvalarray = array(vals.typecode,(a for a in vals))

for e in newvalarray:
    print(e)

arr = array('i',[])
n = int(input("Enter the length of array"))
for i in range(n):
    x = int(input("Enter the next value"))
    arr.append(x)

print(arr)
val = int(input("Enter the value for search"))

#Manually
k = 0
for j in arr:
    if j == val:
        print(k)
        break

    k+=1

print(arr.index(val))


# Creating an empty array
my_array1 = []

# Creating an array with initial values
my_array2 = [1, 2, 3, 4, 5]

# Slicing Arrays
subset = my_array2[1:4]
print(subset)

# Modifying elements
my_array2[2] = 10
print(my_array2)

# Adding elements to end of the array
my_array2.append(6)

my_array2.insert(2,7)

# Removing elements by value
my_array2.remove(3)  # removes the first occurrence of value 3
print(my_array)

# Removing elements by index
del my_array2[0]  # removes the element at index 0
print(my_array)

# Removing elements from the end
popped_element = my_array2.pop()  # removes and returns the last element
print(popped_element)

# Iterating over elements in the array
for element in my_array2:
    print(element)

# Finding the index of an element
index = my_array2.index(4)  # returns the index of value 4
print(index)

# Checking if an element exists in the array
print(10 in my_array2)  # prints False since 10 is not in the array


