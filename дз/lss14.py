# Напишите функцию вычисления (), которая может принимать две переменные и 
# вычислять сложение и вычитание. Результат функции должен возвращаться в одном
# обратном вызове. 
# def summ(a, b):
#     return a + b, a - b


# a, b = map(int, input("Enter two numbers in one line: ").split())
# print(summ(a, b))



# # Напишите программу, которая создает функцию для списка всех четных чисел от 4 до 
# # 30. 
# def sp():
#     tt=[]
#     for i in range(4, 31):
#         tt.append(i)
        
        
# Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, 
# x2, y2), вычисляющая расстояние между точкой (x1,y1) и (x2,y2). Считайте четыре 
# действительных числа и выведите результат работы этой функции. Используйте теорему 
# Пифагора.
# from math import sqrt
# x1=float(input())
# x2=float(input())
# y1=float(input())
# y2=float(input())
# def pif(x1, y1, x2, y2):
#     return sqrt((x1 - x2)**2 + (y1 - y2)**2)


# print(pif(x1, y1, x2, y2))


# Дано действительное положительное число a и целое число n. Вычислите a n . Решение 
# оформите в виде функции power(a, n). Стандартной функцией возведения в степень 
# пользоваться нельзя.
# a=float(input())
# n=float(input())
# def power(a, n):
#     res=1
#     for i in range(abs(n)):
#         res*=a
#     return res


# print(power(a, n))


# Напишите программу кошелек. 
# Программа будет иметь несколько функций, основные добавление баланса и 
# уменьшение баланса кошелька. В теле основной программы, вызовите эти функции, 
# организуя диалог с пользователем. У пользователя может быть более двух валют в кошельке.
print("*********My purse*********")
def op():
    ff=int(input("Do you want withdraw or deposit money?\n1-Withdraw    2-Deposit\n"))
    def main(ff):
        bal_d=750
        bal_e=1250
        if ff==1:
            am=int(input("Enter an amount: "))
            print("Withdraw successful")
            ch=input("Do you want to check your balance?\t").lower()
            if ch=="yes":
                vl=input("Choose a valute:\t").lower()
                if vl=="dollar":
                    bal_d-=am
                    print("Your balance is ", bal_d)
                elif vl=="euro":
                    bal_e-=am
                    print("Your balance is ", bal_e)
                else:
                    print("You dont have this valute")
        if ff==2:
            dam=int(input("Enter an amount: "))
            print("Deposit successful")
            dch=input("Do you want to check your balance?\t").lower()
            if dch=="yes":
                dvl=input("Choose a valute:\t").lower()
                if dvl=="dollar":
                    bal_d+=dam
                    print("Your balance is ", bal_d)
                elif dvl=="euro":
                    bal_e+=dam
                    print("Your balance is ", bal_e)
                else:
                    print("You dont have this valute")
    main(ff)
op()
            

