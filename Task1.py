# 1.По двум заданным числам проверить является ли одно квадратом второго 
import os
os.system("cls")

a = int(input('a ='))
b = int(input('b ='))
if a / b == b or b / a == a:
    print("является")
else :
    print("не являеться")