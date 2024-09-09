def employee(data):
    print('')
    for a,b in data.items():
        print(a,':',b)



employeedata = {}
c = 1
while c != '0':
    userkey = input("Enter userkey :")
    uservalue = input("Enter uservalue :")
    employeedata[userkey] = uservalue
    c = input("Enter 0 to exit or press any key to contine...")


employee(employeedata)




