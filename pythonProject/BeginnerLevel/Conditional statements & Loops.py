name = " Anupama Saranu"
a=10

if a > 2:
    print("condition matches")
else:
    print("condition not matches")

print("if else condition code is completed")

# elif loop

person_age = 21

if person_age >= 18:
    print("Eligible for voting")
elif person_age < 10:
    print("Not eligible for voting")
elif person_age == 10:
    print("Minor")
else:
    print("Invalid Age")

# For loop

obj=[2,3,4,5]
for i in obj:
    print(i*2)

# Sum of first natural numbers 1+2+3+4+5
# range(i,j) - > i,j-1
summation = 0
for j in range(1,6):
    summation = summation + j
print(summation)

print("***************************")
# Jumping 2 iterations(Passing index)
for k in range(1,10,2):
    print(k)

print("***************")
# Skipping the first index
for m in range(10):
    print(m)

matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

flatten_matrix = []

for sublist in matrix:
    for val in sublist:
        flatten_matrix.append(val)

print(flatten_matrix)



for b in range(5):
    if b == 3:
        break
    print(b)

# program to find first 5 multiples of 6

c = 1

while c <= 10:
    print('6 * ', (c), '=', 6 * c)

    if c >= 5:
        break

    c = c + 1

for d in range(5):
    if d == 3:
        continue
    print(d)


from itertools import chain

# Concatenate ranges
new_range = chain(range(5), range(5, 10))
for num in new_range:
    print(num, end=' ')
# Output 0 1 2 3 4 5 6 7 8 9

# slicing
for i in range(10)[3:8]:
    print(i, end=' ')
# output 3 4 5 6 7