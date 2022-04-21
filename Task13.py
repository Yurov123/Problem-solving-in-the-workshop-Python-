# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

count = 0
for i in range(len(str1) - len(str2)):
    if str2 in str1[i:i+len(str2)]:
        count += 1
print(f"Вторая строка входит в первуюф {count} раз(а).")

exid()

from itertools import count
import os
os.system('cls')

str1 = '''Один из наиболее известных русских писателей и мыслителей, 
            один из величайших писателей-романистов мира. Участник обороны Севастополя. 
            Просветитель, публицист, религиозный мыслитель, его авторитетное мнение 
            послужило причиной возникновения нового религиозно-нравственного течения - толстовства. 
            За свои взгляды был отлучён от РПЦ. Член-корреспондент Императорской Академии наук, 
            почётный академик по разряду изящной словесности. Был номинирован на 
            Нобелевскую премию по литературе. Впоследствии отказался от дальнейших номинаций. 
            Классик мировой литературы.'''
str2 = 'из'


print('Количество вхождений второй строки в первую: ',
      str1.count(str2), '\n')

exid()

str1 = input("Введите первую строку для проверки:")
str2 = input("Введите вторую строку для поиска в первой строке:")

# первый способ
print(f"Вторая строка входит в первую {str1.count(str2)} раз(а).")

# второй способ
count = 0
for i in range(len(str1) - len(str2)):
    if str2 in str1[i:i+len(str2)]:
        count += 1
print(f"Вторая строка входит в первую {count} раз(а).")

exid()

def text_find(a,b):
    """
    Function will find occurence of word in the text
    """
    count = 0
    i = 0
    while i <= len(a):
        if b in a[i: i+len(b)]:
            #print("Найдено повторение номер", count+1)
            count += 1
            i += len(b)
        else:
            i += 1
    return count

exid()

# str1= input('First string: ')
# str2= input('Second string: ')

str1 = 'Python free 777 $$$ python free python python python $$$ python'
str2 = 'python free new $$$'

str_list = str1.lower().split()
substr_list = str2.lower().split()

# print('String: ' + str1)
# print('Substrings: ' + str2)
# print()
#
# for i in substr_list:
#     count = 0
#     for j in str_list:
#         count = str_list.count(i)
#     print(f'{i} found {count} times.')

