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

from collections import namedtuple

# a tuple in which we can access the values via the name(specific argument like name)
book=namedtuple('Book','name author price')
book=namedtuple('Book',['name', 'author', 'price'])
book1 = book('origin of species','charles drawin', 500)
print(book1)
print(book1.name)
print(book1.price)
print(book1._fields)

# collections deque
from collections import deque

d = deque('hello world')
print(d)
d.append('!')
d.extend(['!','!','.'])
d.appendleft('0')
print(d)
d.popleft()
print(d)
# it shifts n digits
d.rotate(2)
print(d)