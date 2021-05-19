vegetables =['ladies finger','potato','beans', 'brinjal']

def containsI(str):
    if 'i' in str.lower():
        return True

def strRev(str):
    return str[::-1]
result = list(filter(containsI,vegetables))
print(result)
# using filter and map togeather
result = tuple(map(strRev,filter(containsI,vegetables)))
print(result)

reverse_vegetable_list = list(map(strRev,vegetables))
print(reverse_vegetable_list)
# lambda is in next file :)
filter_reverse_vegetables_having_e = list(filter((lambda str: True if ('e' in str.lower()) else False),reverse_vegetable_list))
print(filter_reverse_vegetables_having_e)
undo_reverse = set(map(strRev,filter_reverse_vegetables_having_e))
print('vegetables having e',undo_reverse)