# a single line anonomous function

addTwo = lambda var: var+2

print(addTwo(4))

# multiple paramaters

eqn = lambda x,y,z=3: (x+y)*z

print(eqn(3,4))
seperateVowle=lambda word : [x for x in word.lower() if x in ['a','e','i','o','u']]
print(seperateVowle('apple'))
