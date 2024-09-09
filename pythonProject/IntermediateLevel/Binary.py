f = open("Binary", mode="rb")
data = f.read(3)
print(type(data))
print(data)
f.close()

file=open("array","wb")
num=[3,6,9,12,18]
array=bytearray(num)
file.write(array)
file.close()


file=open("array","rb")
number=list(file.read(3))
print (number)
file.close()
