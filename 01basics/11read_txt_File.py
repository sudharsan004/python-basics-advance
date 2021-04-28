import os

file = open(r'c:\Users\ADMIN\Desktop\PYTHON-TUROTIALS\code\01basics\input.txt','r')
all_lines=file.readlines()

for line in all_lines:
    if line[-1]=='\n':
        print(line)
    else:
        print('this line does not have next line',line)
file.close()