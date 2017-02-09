import re

def open_s(): 
     with open ('Высшая школа экономики — Википедия.html','r', encoding = 'utf - 8')as f:
         content = f.read()
         links = r'<th(.*?)>Преподаватели</th>\n<td(.*?)>\n<p>(.*?)<sup(.*?)><a(.*?)>(.*?)</a></sup></p>'
         m = re.search(links,content)
         if m != None:
              return m.group(3)

def result():
     with open ('Результат.txt', 'w', encoding = 'utf - 8')as file:
          result = open_s()
          return file.write('Преподаватели:'+ result)
open_s()
result()


