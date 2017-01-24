def open_text():  
      with open('Книга1.csv', 'r', encoding = 'utf - 8') as f:
          line= f.readline()
          arr = line.split(';')
          for i, w in enumerate(arr):
              arr[i] = arr[i].strip('\n') 
          line = f.readline()
          arr1 = line.split(';')
          phrase = dict(zip(arr,arr1))
      return phrase

def puzzle():
    phrase = open_text()
    for key in phrase:
        for i in range(len(key)):
            print(key + '...')
            w = input('Я загадал слово ')
            if w == phrase[key]:
                return print('Ты выиграл')
            else:
                print ('Ты проиграл')
        return

puzzle()


