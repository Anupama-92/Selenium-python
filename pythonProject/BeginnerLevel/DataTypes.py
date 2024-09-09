# list is a datatype that allows multiple values and can be different data types. Use square bracket.
values=[1,2,"Anu",4,5]
print(values[0])  # 1
print(values[-1]) # 5
print(values[1:3]) # 2,"Anu"
values.insert(3, "Saranu")
print(values)
values.append("End")  # Adding value at the end of list
print(values)
values[2]='Saranu'  # Updating the value
del values[2]  # Deleting the value


# Tuple - Same as LIST datatype but immutable.We cannot update the value and use ()

val = (1, 3, "Anu", 9, 10)
mylist = list(val)
print(mylist)
mylist[2] = "demo"
print(mylist)
print(val[0])  # It will display based on index value

# Dictionary is key value pair form.

dic = {"a": 2, 4: "bcd", "c": "Hello world"}
print(dic[4])   # It will display based on key value

# Creating dictionary at run time

dic = {}

dic["Firstname"] = "Anupama"
dic["lastname"] = "Saranu"
print(dic)

# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

thisset = {"apple", "banana", "cherry"}

print(len(thisset))
set1 = {"abc", 34, True, 40, "male"}


print("Enter your name:")
x = input()
print("Hello, " + x)




