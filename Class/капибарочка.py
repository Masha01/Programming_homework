import re

def open_s():
    with open ('Капибара — Википедия.html','r', encoding = 'utf - 8')as f:
        text = f.read()
    reg = r'<a\s+href="(.*?)">(.*?)</a>'
    m = re.findall(reg,text)
    return m

print (open_s())

for link in links [:10]:
    print(link[0]

for link in links[:10]:
          print(link[2],'-->', link[1]
      
