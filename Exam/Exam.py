import os
import re

def text():
    for root, dirs, files in os.walk('.'):
        for f in files:
            if f.endswith('.xhtml'):
                with open( f, 'r') as text:
                    text = text.read()
                    reg = re.findall(r'<se>', text)
                    with open('Exam.txt', 'w', encoding = 'utf-8') as f2:
                        f2.write(f +'\t'+str(len(reg))+ '\n')
    return
text()

def table():
    for f in os.listdir('.'):
        with open( f, 'r') as text:
            text = text.read()
            reg1 = re.findall(r' <title>([А-Яа-яёЁ]*)\.', text)
            reg2 = re.findall(r'([0-9]*)</title>', text)
            for i in reg1 and j in reg2:
                with open ('Результат.csv', 'w', encoding = 'utf - 8')as file:
                    file.write( f + ',' + i + ',' + j+ ','+ '\n')
    return
table()

                            



                        
