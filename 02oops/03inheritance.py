# inheritance and overeride
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sayDetails(self):
        print(f'My name is {self.name} and I am {self.age} years old')

# inheritance
class Student(Person):
    def __init__(self,name,age,std, marks):
        super().__init__(name,age)
        self.std= std
        self.marks= marks
    
    # override method
    def sayDetails(self):
        print(f'I"m {self.name}, {self.age} years old and studying at {self.std}')

class Staff(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary = salary
    
    # override method
    def sayDetails(self):
        print(f'I"m {self.name}, {self.age} years old and my salary is {self.salary}')

chiti = Person('Chiti Robot',0)
chiti.sayDetails()
raja = Student('Raja','18','12',500)
ram = Staff('Ram','35',50000)
raja.sayDetails()
ram.sayDetails()

class animal(object):
    def __init__(self,name,age):
        self.age=age
        self.name=name
    
    def speak():
        print('animals make sounds')

    def sayName(self):
        print('My name is '+self.name)

class Dog(animal):
    def __init__(self, name, age,favFood):
        super().__init__(name, age)
        self.favFood = favFood
    
    def sayDetails(self):
        print(f'My name is {self.name}, I am {self.age} years old and my fav food is {self.favFood}')

    def speak(self):
        print('Dog barks.')

class Cat(animal):
    def __init__(self, name, age, catColor):
        super().__init__(name, age)
        self.color = catColor
    def sayDetails(self):
        print(f'My name is {self.name}, I am {self.age} years old and my color is {self.color}')

    def speak(self):
        print('Cat meows.')

    
dog1= Dog('tim',5,'pedegri')
dog1.sayDetails()
dog1.speak()
dog1.sayName()

cat1= Cat('tom',10,'grey')
cat1.sayDetails()
cat1.speak()
cat1.sayName()
