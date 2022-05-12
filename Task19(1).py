# Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел
# x(n+1) = (a * x(n)+b) % m

import os
os.system("cls")

m = 100
b = 3
a = 2
x = 1
c = 50
list = []
for i in range(c):
    x = (a * x + b) % m
    list.append(x)

print(list)    

