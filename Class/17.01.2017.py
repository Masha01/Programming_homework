#d = {'Россия': 'Москва','Германия' : 'Берлин','Италия':'Рим', 'Франция': 'Париж', 'Азербайджан': 'Баку'}
#for key in d:
#    print(key, d[key], sep = ' - ')

def c():
    cont = input('Введите страну ')
    d = {'Россия': 'Москва','Германия' : 'Берлин','Италия':'Рим', 'Франция': 'Париж', 'Азербайджан': 'Баку'}
    if cont in d:
        return d[cont]
    else:
        return 'NO'
#print (c())

def change():
    d = {'Россия': 'Москва','Германия' : 'Берлин','Италия':'Рим', 'Франция': 'Париж', 'Азербайджан': 'Баку'}
    d1 = {}
    for key in d:
        city = d[key]
        d1[city] = key
    return d1
#print (change())

def delete_doubles():
    d = { 'Петя': 12345, 'Пётр': 12345, 'Аня': 54321, 'Анна': 54321, 'Сёма': 13579}
    arr = []
    d1 = {}
    for key in d:
        if d[key] in arr:
            pass
        else:
            append
            d1[key] = d[key]
        return d1

print(delete_doubles())
    
