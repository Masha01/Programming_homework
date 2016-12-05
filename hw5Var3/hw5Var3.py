first = 0
second = 0
f = open( "Капибара.txt", "r", encoding = "utf-8")
for line in f:
    arr = line.split()
    for i in arr:
        if len(i) == 3 and i[len(i)-1] != ',' :
           first += 1
        if len(i) == 4 and i[len(i)-1] == ',':
        #Знаю, что для универсальности нужно добавить такие условия для других знаков препинания(и в слове длины 1 тоже),с таким условием программа работает только для моего текста.Но из задания не совсем поняла, должна ли быть программа универсальной.
            first += 1
        if len(i) == 1 and i != '―':
            second += 1
if second == 0:
    print( 'Слов длины один нет')
else:
    num = first/second
print(num)
f.close()

