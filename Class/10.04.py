import os
def task_0():
    print(os.listdir('.'))
task_0()


def task_1():
    sent = input('Введите предложение:')
    arr = sent.split()
    path = '\\'.join([str(i) for i in arr])
    os.makedirs(path)
task_1()

def task_2():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(i)
    path = '\\'.join([str(i) for i in arr])
    os.makedirs(path)

task_2()


 
