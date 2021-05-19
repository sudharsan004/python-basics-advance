from collections import Counter

counter = Counter(a=4,b=3,c=2)
print(counter)

name = Counter('sudharsan')
print(name)

new_counter =Counter(a=2,b=3)
counter.subtract(new_counter)
print(counter)

counter.update(a=4,b=1)
print(counter)