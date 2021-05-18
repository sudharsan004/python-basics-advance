vegetables =['ladies finger','potato','beans', 'brinjal']

def containsI(str):
    if 'i' in str:
        return str

def strRev(str):
    return str[::-1]
result = list(filter(containsI,vegetables))
print(result)
# using filter and map togeather
result = tuple(map(strRev,filter(containsI,vegetables)))
print(result)
