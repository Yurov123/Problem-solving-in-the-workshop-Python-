# Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

import os
os.system("cls")

day = ['Понедельник','Вторник','Среда','Четверг','Пятница','Суббота','Воскресенье']
count = int(input("Введите число дня недели:"))
while count > 7 or count < 1:
    count = int(print(f'Ошибка\n'))
else:
    print(f'Это', day[count-1], end=' - ')    
if 1 <= count <= 5:
    print('рабочий день!\n')
else:
    print('выходной день!\n')




