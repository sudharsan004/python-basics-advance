'''
Decorators allow us to wrap another function in order to extend the behavior of the wrapped function,
without permanently modifying it
'''
import time
def timer(function):
    def wrapper(*args,**kwargs):
        startTime = time.time()
        result=function(*args,**kwargs)
        endTime = time.time()
        timeTaken = (endTime-startTime)
        return (timeTaken,result)
    return wrapper

def addNumbers(start,end):
    sum=0
    for num in range(start,end):
        sum += num
        # dealy some time to see the result
        time.sleep(0.01)
    return sum

addNumbers = timer(addNumbers)
result=addNumbers(1,100)
print(result)

# This can also be achived by decorators
@timer
def addNumbers(start,end):
    sum=0
    for num in range(start,end+1):
        sum += num
        # dealy some time to see the result
        time.sleep(0.01)
    return sum

@timer
def multiply(start,end):
    mul=1
    for num in range(start,end):
        mul *= num
    return mul

result=addNumbers(1,100)
print(result)

multiply_result = multiply(1,10)
print(multiply_result)