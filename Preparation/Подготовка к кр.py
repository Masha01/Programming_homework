import re
def open_text():  
      with open('Leskov.txt', 'r', encoding = 'utf - 8') as f:  
                text = f.read()  
                text = text.lower()  
                arr = text.split()  
                for i, w in enumerate(arr):  
                    arr[i] = arr[i].strip(',.”"?!-:;')  
      return arr

def words():
    arr = open_text()
    return len(arr)
print(words())

def frequency():
    arr = open_text()
    d = {}
    for i in range(len(arr)):
        if arr[i] not in d:
            d[arr[i]] = 1
        else:
            d[arr[i]] +=1
    return d

def result():
    with open ('Результат.csv', 'w', encoding = 'utf - 8')as file: 
        d = frequency() 
        for key in sorted(d):
            file.write(key + ',' + str(d[key])+ '\n')
        return

result()    
 
def phrase():
      with open('Leskov.txt', 'r', encoding = 'utf - 8') as f:  
                text = f.read()  
      with open ('Результат.txt', 'w', encoding = 'utf - 8')as file:
            reg = re.findall(r'\b\w*аго \w*(?:и|а|ы)',text)
            for reg 
            return reg
phrase()
