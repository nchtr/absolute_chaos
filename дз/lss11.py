# Написать программу для вывода узора по образцу, используя вложенный цикл.
z="*"
while True:
    for i in range(1, 6):
            print(z*i)   
    for j in range(5, 0, -1):
            print(z*j)
    break
    

# Напишите программу, которая считывает целые числа с консоли по одному числу в
# строке.
# Для каждого введённого числа проверить:
# ➢ если число меньше 10, то пропускаем это число;
# ➢ если число больше 100, то прекращаем считывать числа;
# ➢ в остальных случаях вывести это число обратно на консоль в отдельной строке.

y=0
while True:
    y=int(input())
    if y>=100:
         break
    elif y<=10:
        continue
    print(y)


# Совершенным числом называется целое положительное число, равное сумме своих
# положительных делителей, исключая само число. Например, 6 имеет делители 1, 2 и 3
# 2
# (исключая само себя), а 1 + 2 + 3 = 6, поэтому 6 — совершенное число.
# Напишите программу, которая выводит все совершенные числа от 1 до 100.
n = 100
for i in range(1, n+1):
   a = 0
   for j in range(1, i):
        if i % j == 0:
          a += j
   if a == i:
      print(i)