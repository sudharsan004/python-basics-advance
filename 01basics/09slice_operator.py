colors =['green','blue','orange','yellow','red']
my_text ="Sudharsan likes green color"

# slice operator(':') syntax=>list or string[start:stop:steps]
print(colors[:3:2])
print(colors[2:3:])
print(my_text[:10:1])
print(my_text[:10:-1])

print(colors)

colors[0:0]="first"
print(colors)
colors[1:1]="second"
print(colors)

colors.insert(3,'insert_at_3')
print(colors)
