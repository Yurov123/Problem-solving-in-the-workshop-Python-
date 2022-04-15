# Найти максимальное из пяти чисел
import os
os.system("cls")

d1, d2, d3, d4, d5 = map(int, input().split())
map = max(d1, d2, d3, d4, d5 )
print(map)

