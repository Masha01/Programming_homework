import random

def noun_f():
    file = open ('Существительные_ж.txt' , 'r', encoding = 'utf-8')
    for line in file:
        noun = line.split()
        file.close()
        return random.choice(noun)

def noun_m():
    file = open ('Существительные_м.txt' , 'r', encoding = 'utf-8')
    for line in file:
        nouns = line.split()
        file.close()
        return random.choice(nouns)

def noun_number_of():
    file = open ('Существительные_множественные.txt' , 'r', encoding = 'utf-8')
    for line in file:
        nouns = line.split()
        file.close()
        return random.choice(nouns)

def adjective_m(word):
    file = open ('Прилагательные_м.txt' , 'r', encoding = 'utf-8')
    for line in file:
        adjectives = line.split()
        file.close()
        return random.choice(adjectives) + ' ' + word

def adverb():
    file = open ('Наречия.txt' , 'r', encoding = 'utf-8')
    for line in file:
        adverbs = line.split()
        file.close()
        return random.choice(adverbs) 

def verb_f(subj):
    file = open ('Глаголы_ж.txt' , 'r', encoding = 'utf-8')
    for line in file:
        verbs = line.split()
        file.close() 
        return random.choice(verbs) + ' ' + subj
    
def verb_m(adv,n):
    file = open ('Глаголы_м.txt' , 'r', encoding = 'utf-8')
    for line in file:
        verbs = line.split()
        file.close()
        return adv + ' ' + n+ random.choice(verbs)+ ' '

def verb_inf():
    file = open ('Глаголы_инф.txt' , 'r', encoding = 'utf-8')
    for line in file:
        verbs = line.split()
        file.close() 
        return random.choice(verbs)


def verb_transitive(obj):
    file = open ('Глаголы_переход.txt' , 'r', encoding = 'utf-8')
    for line in file:
        verbs = line.split()
        file.close()
        return ', который ' + random.choice(verbs) + ' ' + obj

def verb_imp():
    file = open ('Глаголы_пов.txt' , 'r', encoding = 'utf-8')
    for line in file:
        verbs = line.split()
        file.close()
        return random.choice(verbs)

def time():
    file = open ('Время.txt' , 'r', encoding = 'utf-8')
    for line in file:
        time = line.split()
        file.close()
        return random.choice(time)

def pronoun():
    file = open ('Местоимения.txt' , 'r', encoding = 'utf-8')
    for line in file:
        pronouns = line.split()
        file.close()
        return random.choice(pronouns)

def no():
    no = [ 'не ', '']
    return random.choice(no)

def random_sentence1():
    sentence = 'Иди и ' + verb_imp() + ' мне ' + noun_m()+'а' + '!'
    return sentence

def random_sentence2():
    sentence = adjective_m(noun_m()) + verb_transitive(noun_number_of())+ ',' +\
               verb_m(adverb(), no()) + verb_inf()  + '.'
    return sentence

def random_sentence3():
    sentence = 'Где ' + time() + ' ' + verb_f(noun_f()) + '?' 
    return sentence

def random_sentence4():
    sentence = 'Если б ' + pronoun() + ' был ' + noun_m()+ ', то ' +\
               verb_m(adverb(), no())+ ' бы ' + verb_inf()  + '.'
    return sentence

def random_text():
    sentences = [random_sentence1(), random_sentence2(), random_sentence3(), random_sentence4()]
    return random.choice(sentences)

print("---- FASCINATING MASTERPIECE STARTS HERE ----")
num_of_sents = 5
for i in range(num_of_sents): 
    sentence = random_text()
    sentence = sentence.capitalize()
    print(sentence, end=' ') 
print("\n---------AND ENDS HERE ---------")


