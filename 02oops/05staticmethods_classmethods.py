class Person(object):
    # this class variables are common to all the instance of this(and also sub classes) objects, can also be called directly from this class itself.
    # class variable
    person_names =[]
    persons =[]
    def __init__(self,name,age):
        self.person_names.append(name)
        self.persons
        self.name= name
        self.age = age
    
    # class method
    @classmethod
    def get_no_persons(obj):
        return len(obj.person_names)


    # static method like a normal fun inside a class
    @staticmethod
    def greet():
        return('hello world')

class Teacher(Person):
    pass

t1= Teacher('teacher','20')
print(t1.person_names)
print(Person.get_no_persons())
print(Person.person_names)
t2= Person('s','20')
print(t2.person_names)
print(t1.person_names)
print(Person.get_no_persons())
print(t2.get_no_persons())
print(Person.greet())

# class methods and class variables can be called directly by the class or by an instance
        