# for loop

# for identifier in iterator:
#     do something

for number in range(0,100,2):
    print(number)

# while loop

# while condition == True:
#     do something

condition = True
while condition:
    user_input=input('Enter something:')
    print(user_input)
    if user_input=='stop':
        break