word = input('Введите слово')
for i in range(len(word)):
    print(word[i::] + word [:i])
    
