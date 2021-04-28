vegetables =['brinjal','potato','carrot',]
# lists can contain differrent data types like int , str, bool etc
print(vegetables)
vegetables.sort()
print('after sorting',vegetables)

vegetables.append('ladies finger')
print('after adding ladies finger',vegetables)

print(vegetables[1])
vegetables[1] =' beetroot'
print('after changing carrot to beetroot', vegetables)

# tuples - unmutable data type cannot change the value

coordinates =(5,0,2)
color =(23,67,225)
print(type(color))