def puzzle():
    phrase = {'незванный':'гость','розовый':'слон','вишнёвый':'сад', 'сиреневый':'туман', 'кленовый':'лист'}
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

