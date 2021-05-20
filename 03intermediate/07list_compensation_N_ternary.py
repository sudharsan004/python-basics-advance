# list compenensation 
# syntax
# newlist = [expression for item in iterable if condition == True]
 
fruits= ['apple','grapes','orange','dates']

reverseFruitsContainingVowle = [fruit[::-1] for fruit in fruits if any(vowle in fruit for vowle in ['a','e','i','o','u'] ) ]
print(reverseFruitsContainingVowle)
fruitsContainingVowle= [fruit[::-1] for fruit in reverseFruitsContainingVowle ]
print(fruitsContainingVowle)

# ternary operator
# syntax: [on_true] if [expression] else [on_false] 

print('hello') if 5<3 else ''