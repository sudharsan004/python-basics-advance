# Global vs local variables

# Global variable
age = 20
print(age)

def sayAge():
    # local varibale
    age =21
    print(age)

sayAge()
print(age)


# changing an global variable inside an function (global keyword)

time = 10

def changeTime():
    # declaring a variable global syntax: global variable_name
    global time
    time =20
    print(time)

changeTime()
print(time)
