# 22.	Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
#  стоящих на нечётной позиции.
# Пример:
# •	[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
import os
os.system("cls")

spisok =[]
a = int(input("Введите длину списка :"))
for i in range(a):
      spisok.append(random.randint(1,10))
print(f"Создан новый список: \n {spisok}")
sum = 0
for i in range(a):
      if i % 2 > 0: sum += spisok[i]
print(f"Сумма чисел списка стоящих в нечетных позициях = {sum}")


