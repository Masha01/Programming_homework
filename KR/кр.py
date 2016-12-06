n = 0
f = open( "Цитаты.txt", "r", encoding = "utf-8")
for line in f:
    arr = line.split ('—')
    arr2 = arr[0].split()
    if len(arr2) < 10:
         print (arr[0])
arr3 = line.split()
for i in arr3:
    if i == 'разум':
        n += 1
print (n)
f.close()
