# Пользователь вводит с клавиатуры два числа, выполните следующие операции:
# 1. Нужно показать все числа в указанном диапазоне.
# 2. Нужно показать все нечетные числа в указанном диапазоне.
# 3. Нужно показать все четные числа в указанном диапазоне.
# 4. Нужно показать все числа в указанном диапазоне в порядке убывания.
a=int(input())
b=int(input())
for i in range (a, b+1):
    print(i)
for i in range (a, b+1):
    if i%2!=0:
        print(i)
for i in range (a, b+1):
    if i%2==0:
        print(i)
for i in range (b, a-1, -1):
    print(i)



# Когда Павел учился в школе, он запоминал таблицу умножения прямоугольными
# блоками. Для тренировок ему бы очень пригодилась программа, которая показывала бы блок
# таблицы умножения.
# Напишите программу, на вход которой даются четыре числа a, b, c и d, каждое в своей
# строке. Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [a;
# b] на все числа отрезка [c;d].
a =int (input("Число 1: "))
b =int (input("Число 2: "))
c =int (input("Число 3: "))
d =int (input("Число 4: "))
print("Таблица: ", end='\n')
for k in range (c, d+1):
    print('\t'+str(k), end="")
print(end='\n')
for i in range (a, b+1):
    print(str(i)+'\t', end="")
    for j in range (c, d+1):
        print(str(i*j), end='\t')
    print(end='\n')