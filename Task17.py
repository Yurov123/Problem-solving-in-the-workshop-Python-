# Задать список из N элементов, заполненных числами из [-N, N].
#  Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число

import os
import random
os.system("cls")

N = int(input("Введите размер списка: "))
num_list = list(range(-N, N+1)) # задаем список из N элементов, заполняем его
print(num_list)

with open('file.txt', 'w') as data:
    data.write(f'{random.randint(0,N*2)}\n') # добавляем случайное число в файл
    data.write(f'{random.randint(0,N*2)}\n') # добавляем случайное число в файл
    data.write(f'{random.randint(0,N*2)}\n') # добавляем случайное число в файл
    data.write(f'{random.randint(0,N*2)}\n') # добавляем случайное число в файл
 # читает файл в список
def read2list(file):
    # открываем файл в режиме чтения utf-8
    file = open(file, 'r', encoding='utf-8')

    # читаем все строки и удаляем переводы строк
    lines = file.readlines()
    lines = [line.rstrip('\n') for line in lines]

    file.close()

    return lines    
    
lines = read2list('file.txt')
print(lines)

multiply = 1
for i in lines :
    multiply *= int(num_list[int(i)])
print(multiply)     


    













