import re
import os
def folder():
    arr = [f for f in os.listdir('.')if re.search(r'[а-яёЁА-Я]+',f)if os.path.isdir(f)]
    print(len(arr))
    return arr
folder()

def print_result():
    result = []
    for f in os.listdir('.'):
        if os.path.isfile(f):
            f = f[:f.rfind('.')]
            if f not in result:
                result.append(f)
        else:
            if f not in result:
                result.append(f)
    return ' '.join([str(i) for i in result])
print(print_result())
