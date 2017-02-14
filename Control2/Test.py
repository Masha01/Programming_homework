import re
def count_line():
    with open('Test.xml', 'r', encoding = 'utf-8') as f:
        s = 1
        for line in f:
            if line != '  </teiHeader>\n':
                s += 1
            else:
                break
        return s

def write_in():
    with open('Test.txt', 'w', encoding = 'utf-8') as f:
        num = count_line()
        f.write(str(num))
        return
write_in()

def open_text():
    with open('Test.xml', 'r', encoding = 'utf-8') as f:
        text = f.read()
        return text

def phrase():
    text = open_text()  
    d = {}
    reg = re.findall(r'<w lemma=".*?" type="(.*?)">.*?</w>',text)
    for i in range(len(reg)):
        if reg[i] not in d:
            d[reg[i]] = 1
        else:
            d[reg[i]] +=1
    return d

def write_phrase():
    with open('Test1.txt', 'w', encoding = 'utf-8') as f:
        d = phrase()
        for key in d:
            f.write(key + ',' + str(d[key])+ '\n')
        return
write_phrase()

def n():
    text = open_text()  
    reg = re.findall(r'<w lemma=".*?" type="f\wh\w*">(.*?)</w>',text)
    return reg
print(n())

    
                
                
                
