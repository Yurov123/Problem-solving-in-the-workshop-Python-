# Подсчитать сумму цифр в вещественном числе.
import os
import random
os.system("cls")

a = random.uniform(1, 1001)
print('Задано число:', a)

a = str(a).replace('.', '')     # переводим в строковый тип, убираем точку
print(a)
summa = sum(map(int, a))        # переводим в числовой тип, считаем сумму
print('Сумма цифр данного числа равна:', summa, '\n')

