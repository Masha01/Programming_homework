arr = []
word = input('Введите слово')
while word:
   arr.append (word)
   word = input( 'Введите слово')
for w in range(len(arr)):
    print(arr[w][w + 1::])

    
