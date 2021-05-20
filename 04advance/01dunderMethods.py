# dunder stands for double underscore '__' methods
# dunder methods are like defining the basic operations(+,-,*,/,len(),etc..) for all the instances(objects) of this class
class Person(object):
    def __init__(self,name,height):
        self.name=name
        self.height=height
    
    def __add__(self,anotherPerson):
        if isinstance(anotherPerson,Person):
            return f'{self.name} and {anotherPerson.name} are friends'
        else:
            raise Exception(anotherPerson+'is not a object of class Person')
    
    def __call__(self):
        return print(f'Hi, I am {self.name},did you call me?')


ram = Person('Ram','173cm')
ram()

