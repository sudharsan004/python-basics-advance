import sys

def gen(n):
    for i in range(n):
        yield i


num_list= [i for i in range(5000)]
for num in num_list:
    # print(num)
    pass

generator= gen(5000)
# print(next(generator))

for num in generator:
    # print(num)
    pass

print(sys.getsizeof(num_list))
print(sys.getsizeof(generator))

