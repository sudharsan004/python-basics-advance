'''
Decorators allow us to wrap another function in order to extend the behavior of the wrapped function,
without permanently modifying it
'''
import time
def timer(function,*args,**kwargs):
    startTime = time.time()
    result=function(*args,**kwargs)
    endTime = time.time()
    timeTaken = (endTime-startTime)
    return timeTaken

def addNumbers(start,end):
    sum=0
    for num in range(start,end):
        sum += num
        # dealy some time to see the result
        time.sleep(0.01)
    return sum

timeTaken = timer(addNumbers,5,100)
print(timeTaken)

# This can also be achived by decorators
@timer
def addNumbers(start,end):
    sum=0
    for num in range(start,end):
        sum += num
        # dealy some time to see the result
        time.sleep(0.01)
    return sum
    
addNumbers(1,100)