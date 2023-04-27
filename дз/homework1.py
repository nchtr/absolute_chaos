# # 1. Пользователь вводит с клавиатуры три числа. Необходимо найти сумму чисел,
# # произведение чисел. Результат вычислений вывести на экран.
# a=float(input("Введите число: "))
# b=float(input("Введите число: "))
# c=float(input("Введите число: "))
# print("Сумма чисел = ", a+b)
# print("Произведение чисел = ", a*b)


# # 2. Пользователь вводит с клавиатуры три числа. Первое число — зарплата за месяц,
# # второе число — сумма месячного платежа по кредиту в банке, третье число — задолженность
# # за коммунальные услуги. Необходимо вывести на экран сумму, которая останется у
# # пользователя после всех выплат.
# zp=float(input("Введите зарплату: "))
# kr=float(input("Введите счет за кредит: "))
# zd=float(input("Введите задолжность за ком.услуги: "))
# print("После необходимых выплат у вас оставнется: ", zp-(kr+zd))


# # 3. Напишите программу, вычисляющую площадь ромба. Пользователь с клавиатуры
# # вводит длину двух его диагоналей.
# d1=float(input("Первая диагональ ромба = "))
# d2=float(input("Вторая диагональ ромба = "))
# print("Площадь ромба = ", (d1+d2)/2)


# # 4. Выведите на экран надпись To be or not to be на разных строках. Пример вывода: To
# # be or not to be.
# print("To \nbe \nor \nnot \nto \nbe")


# # 5. Выведите на экран надпись «Life is what happens when you're busy making other plans»
# # John Lennon на разных строках. Пример вывода:
# # “Life is what happens
# #   when
# #       you’re busy making other plans”
# #                                    John Lennon
# print('“Life is what happens \n\twhen \n\t\tyou’re busy making other plans” \n\t\t\t\t\t\tJohn Lennon')







# Напишите программу, которая считывает с клавиатуры последовательно три строки:
# название фильма, название кинотеатра и время, после чего выводит на экран «Билет на» [название фильма] " в " [название кинотеатра] " на [время] забронирован.».
# film=input("Название фильма:")
# kt=input("Кинотеатр:")
# t=input("Удобное время:")
# print(f'Билет на "{film}" в "{kt}" на {t} забронирован')





#no2
# name=input("Имя:")
# gg=int(input("Год рождения:"))
# mm=int(input("Месяц рождения:"))
# dd=int(input("День рождения:"))
# em=input("Ваш email:")
# print(f'Имя: {name}')
# print(f'{gg}{mm}{dd}'.sep==".")
# print(f'email: {em}'.end=="@gmail.com")


#no3
# from datetime import datetime

# print(datetime.today())



#no4

# from datetime import datetime
# now=datetime.now()
# a=now.strftime("%d/%m/%y")
# b=now.strftime("%H/%M/%S")
# print(f'Date: {a} time: {b}')



a, b, c=map(int(input().split()))
print(a,b,c)