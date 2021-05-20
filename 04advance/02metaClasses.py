'''
Every thing in python is actually an object even a class itself is an object of class 'type'
A metaclass in Python is a class of a class that defines how a class behaves. 
A class is itself an instance of a metaclass.(by default 'type')
'''
class Animal():
    pass
# this class is a object of class type 
print(type(Animal))
print(type(Animal()))

