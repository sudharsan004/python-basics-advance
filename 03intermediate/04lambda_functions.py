# a single line anonomous function

addTwo = lambda var: var+2

print(addTwo(4))

# multiple paramaters

sum = lambda x,y: x+y

seperateVowle=lambda word : [x for x in word.lower() if x in ['a','e','i','o','u']]
print(seperateVowle('apple'))
