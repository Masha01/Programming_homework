def open_text():
    with open('text.txt', 'r', encoding = 'utf - 8') as f:
              text = f.read()
              text = text.lower()
              arr = text.split()
              for i, w in enumerate(arr):
                  arr[i] = arr[i].strip(',.?!-')
    return arr
#print (open_text())


def first_letter(letter):
    arr = open_text()
    for i in arr:
        if letter == i[0]:
            print (i)
        else:
            pass
    return i

letter = input('Введите букву')
    
