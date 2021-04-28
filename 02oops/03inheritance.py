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


raja = Student('Raja','18','12',500)
ram = Staff('Ram','35',50000)
raja.sayDetails()
ram.sayDetails()