# Реализовать алгоритм перемешивания списка.
import os
os.system("cls")
from random import randint, shuffle

N = int(input("Введите размер списка: "))
num_list = list(range(-N, N+1)) # задаем список из N элементов, заполняем его
print(num_list)

shuffle(num_list) # функция перемешивания
print(f'Перемешанный список:  {num_list}') # распечатали перемешанный список


