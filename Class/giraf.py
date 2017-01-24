import re

def open_text(): 
     with open('Жирафики.txt', 'r', encoding = 'utf - 8') as f: 
               text = f.read()
               text = text.lower() 
               arr = text.split() 
               for i, w in enumerate(arr): 
                   arr[i] = arr[i].strip(',.?!-') 
     return arr 


def giraf():
    s = input('Введите что-нибудь ')
    regex = 'жираф(а(ми?|х)?|у|е|о[мв]|ами|ы)?'
    m = re.search(regex,s)
    if m != None:
        return 'Я нашёл'
print(giraf())


def giraf_in_text():
    arr = open_text()
    regex = r'\bжираф(а(ми?|х)?|у|е|о[мв]|ами|ы)?\b'
    m = re.search(regex,i[arr])
    s = 0
    for  i[arr] in arr:
        if m != None:
            s += 1
    return s
print(giraf_in_text())

