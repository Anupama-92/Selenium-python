str = "AmazonOnline.com"
str1 = "OnlineShopping Site"
str3 = "AmazonOnline"
print(str[1])    # m
print(str[0:6])   # If we want substring in python
print(str+str1)  # Concatenation
print(str3 in str)   # Substring check

var = str.split(".")  # Split the string
print(var)
print(var[0])

str2 = " products "   # Strip or trim the string
print(str2.strip())
print(str2.lstrip())   # trim the string at left side
print(str2.rstrip())   # trim the string at right side


#Program to reverse a string
gfg = "Anupama"
print(gfg[::-1])


# Delete/update from a string
String1 = "Hello, I'm a Anupama"
print("Initial String: ")
print(String1)

# 1
list1 = list(String1)
list1[2] = 'p'
String2 = ''.join(list1)
print("\nUpdating character at 2nd Index: ")
print(String2)

# 2
String3 = String1[0:2] + 'p' + String1[3:]
print(String3)

# Deleteing the character
String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)

String2 = String1[0:2] + String1[3:]
print("\nDeleting character at 2nd Index: ")
print(String2)