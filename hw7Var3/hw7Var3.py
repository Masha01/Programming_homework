def open_text(): 
     with open('Austen_Jane.txt', 'r', encoding = 'utf - 8') as f: 
               text = f.read() 
               text = text.lower() 
               arr = text.split() 
               for i, w in enumerate(arr): 
                   arr[i] = arr[i].strip(',.”"?!-:;') 
     return arr  

def words():
     arr = open_text()
     arr1 = []
     for i,w in enumerate(arr):
          if arr[i][-4:] == 'hood':
               arr1.append(arr[i])
     return arr1

def number_of_words():
     arr1 = words()
     return len(arr1)

def the_minimum_frequency():
     arr = open_text()
     arr1 = words()
     y = 1
     n = 0
     for i,w in enumerate(arr1):
          y = min(y, arr1.count(arr1[i]))
          for i,w in enumerate(arr1):
              if y == arr1.count(arr1[i]):
                  n = i
     return arr1[n]

def base():
     arr1 = words()
     arr2 = []
     for i,w in enumerate(arr1):
          x = arr1[i].rfind('h')
          arr2.append(arr1[i][:x])
     return arr2

print(number_of_words())
print(the_minimum_frequency())
print(' '.join(map(str,(base()))))
