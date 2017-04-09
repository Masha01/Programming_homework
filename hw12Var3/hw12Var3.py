import re
def open_text():
    with open('Гоголь.txt', 'r', encoding = 'utf - 8') as f:
        text = f.read()
        text = re.sub(r'\n',' ', text)
        arr = re.split('\.|\?|\! ', text)
        for i, s in enumerate(arr):
            arr[i] = re.sub(r'[:;,.?!— -]',' ', arr[i])
        return arr 

def words_5():
    arr = open_text()
    for i in range(len(arr)):
        arr1 = arr[i].split()
        template = '{}_{}'
        length ={print(template.format(arr1[i],len(arr1[i]))) for i,w in enumerate(arr1)}
    return 
words_5()
