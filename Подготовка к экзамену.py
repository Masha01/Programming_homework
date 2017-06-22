import re
import os

def text_read():
    for root, dirs, files in os.walk('.'):
        for f in files:
            if f.endswith('.xml'):
                with open( f, 'r', encoding = 'utf - 8') as text:
                    text = text.read()
                    return text
def count():
    text = text_read()
    reg1 = re.findall(r'<ana', text)
    reg2 = re.findall(r'<w>.*</w>', text)
    num = len(reg1)/len(reg2)
    return num
print(count())

def part_of_speech():
    text = text_read()
    dic = {}
    reg = re.findall(r'gr="([A-Z]*)', text)
    for i in reg:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i]+=1
    return dic
print(part_of_speech())

def write_in():
    with open('Test1.txt', 'w', encoding = 'utf-8') as f:
        d = part_of_speech()
        template = '{}{:>10}'
        for key in sorted(d):
            f.write((template.format(key, d[key]))+ '\n')
        return
#write_in() 

def write():
    with open('Test1.txt', 'w', encoding = 'utf-8') as f:
        d = part_of_speech()
        for key in sorted(d):
            f.write(key+'\t'+str(d[key])+ '\n')
        return
write()
