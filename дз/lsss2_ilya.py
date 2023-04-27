# Написать лямбду-функцию, которая: 
# 1. добавляет 15 к заданному числу, переданному в качестве аргумента; 
# Input: 10 Output:25 
# 2. умножает аргумент x на аргумент y, выведите результат; 
# Input: 12 4 Output:48 
# 3. фильтрует список целых чисел, заданных пользователем; 
# Список целых чисел: 
# [78, 2, 13, 46, 5, 61, 74, 81, 94, 10] 
# Список четных чисел: 
# [78, 2, 46, 74, 94, 10] 
# Список нечетных чисел: 
# [13, 5, 61, 81] 
# 4.выводит год, месяц, дату и время. 
# При решении используйте модуль datetime. Output: 
# 2022-07-19 07:58:31.246609 
# 2022 
# 7 
# 19 
# 07:58:31.246609 
# import datetime
# #1
# sum=lambda a: a+15
# sum(int(input("input: ")))

# #2
# multi=lambda x, y: x*y
# multi(int(input("input: ")), int(input("input: ")))

# #3
# l=[78, 2, 13, 46, 5, 61, 74, 81, 94, 10]
# nonc = list(filter(lambda x: x%2!=0, l))
# ch = list(filter(lambda x: x%2==0, l))
# print(ch, nonc)

# #4
# now = datetime.datetime.now()
# print(now)
# year = lambda x: x.year
# month = lambda x: x.month
# day = lambda x: x.day
# t = lambda x: x.time()
# print(year(now))
# print(month(now))
# print(day(now))
# print(t(now))


# Задание №2.
# Напишите функцию, которая принимает один аргумент для лямбды функции и этот 
# аргумент будет умножен на неизвестное заданное число.
from random import randint
def umult(p):
    return lambda o: p*o
lam = umult(int(input()))
print(lam(int(input())))


# Задание №3.
# Hапишите программу, используя лямбда-функции для подсчета четных и нечетных чисел 
# в списке целых чисел.
l=[147, 241, 39, 5, 778, 18, 0, 10]
spic=list(map(lambda n:n%2==0, l))
spinc=list(map(lambda n:n%2!=0, l))
print('Количество четных: ',spic.count(True))
print('Количество нечетных: ',spinc.count(True))


