first = 0
second = 0
f = open( "Капибара.txt", "r", encoding = "utf-8")
for line in f:
    arr = line.split()
    for i in arr:
        if len(i) == 3 and i[len(i)-1] != ',' and i[len(i)-1] != '.' and i[len(i)-1] != ':' and i[len(i)-1] != ';' and i[len(i)-1] != '!' and i[len(i)-1] != '?':
            first += 1
        if len(i) == 4 and i[len(i)-1] == ',' for i[len(i)-1] == '.' or i[len(i)-1] == ':' or i[len(i)-1] == ';' or i[len(i)-1] == '!' or i[len(i)-1] == '?':
            first += 1
        if len(i) == 1 and i != '―':
            second += 1
        if len(i) == 2 and i[len(i)-1] == ',' or i[len(i)-1] == '.' or i[len(i)-1] == ':' or i[len(i)-1] == ';' or i[len(i)-1] == '!' or i[len(i)-1] == '?':
            second +=1
if second == 0:
    print( 'Слов длины один нет')
else:
    num = first/second
print(num)
f.close()

