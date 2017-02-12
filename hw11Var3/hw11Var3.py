import re

def open_s(): 
     with open ('Лингвистика — Википедия.html','r', encoding = 'utf - 8')as f: 
         text = f.read() 
         return text

def lang_meat():
    m = open_s()
    step = re.sub(r'\bязык(а(ми?|х)?|у|о(м|в)|е|и)?\b',r'\bшашлык\1',m, flags = re.DOTALL)
    step2 = re.sub(r'\bЯзык(а(ми?|х)?|у|о(м|в)|е|и)?\b',r'\bШашлык\1', step, flags = re.DOTALL)
    return step2

def result():
     with open ('Результат.txt', 'w', encoding = 'utf - 8')as file:
         result = lang_meat()
         return file.write(result)
result()

 
