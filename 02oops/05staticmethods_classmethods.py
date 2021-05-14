class Person(object):
    names =[]
    def __init__(self,name,age):
        self.names.append(self)
        self.name= name
        self.age = age

class Teacher(Person):
    pass

t= Teacher('s','20')
print(t.name)
print(object)
        