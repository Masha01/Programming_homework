import re 


def open_s():
    with open ('Динозавры — Википедия.html','r', encoding = 'utf - 8')as f:
        text = f.read()
        return text

def find_dino():
    text = open_s()
    reg = r'\b[Дд]инозавр[а-я]{0,5}'
    m = re.findall(reg, text)
    return m
print (find_dino())

def no_html():
    text = open_s()
    m = re.sub(u'<.*?>', u'', text, flags = re.DOTALL)
    return m
print (no_html())

def cat_dino():
    m = no_html()
    n = re.sub(r'\bдинозавр',r'\bкот',m,flags = re.DOTALL)
    n1 = re.sub(r'\bДинозавр',r'\bКот',n, flags = re.DOTALL)
    return n1
print(cat_dino())



