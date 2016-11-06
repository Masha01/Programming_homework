print ('Введите слово')
word = input()
for letter in word[::-1]:
    if letter not in 'з,я':
        print (letter)
    if letter in 'з,я':
        continue
        print (letter)
        
