# Вывести на экран числа от -N до N
import os
os.system("cls")

N = abs(int(input()))
for i in range(-N, N + 1):
    print(i, end = ' ')
