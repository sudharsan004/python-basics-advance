# *args refers to any number of arguments
# *kwargs refers to any number of keyword arguments
def addNumbers(a,b,*args):
    sum =a+b
    print(args)
    # args is of tuple
    print(type(args))
    map(lambda num:sum+num,args)
    return sum

print(addNumbers(6,9,743,8723))

def path(startingPlace,destination,**kwargs):
    print(type(kwargs))
    print(f"""Travel Details are:
        Starting Place : {startingPlace}.
        Ending Place : {destination}.""",end='')
    for key, value in kwargs.items():
        print(f"""
        {key}: {value}.""",end='')

path('Vellore','Delhi',distance='750kms',check_point='Chennai')
