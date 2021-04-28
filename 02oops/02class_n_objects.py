class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sayName(self):
        print('my name is ',self.name)
    def changeAge(self,age):
        self.age = age
sam = Person('sam',5)
james = Person('james',15)
print(type(Person))
print(type(sam))
sam.sayName()
print(james.age)
james.changeAge(20)
print(james.age)