# Написать рекурсивную функцию нахождения степени числа.
def stpn(a, b):
    if b==1:
        return a
    else:
        return a*stpn(a, b-1)
    
    
a, b=map(int, input().split())
print(stpn(a,b))


# Написать рекурсивную функцию, которая вычисляет сумму всех чисел в диапазоне от a
# до b. Пользователь вводит a и b. Проиллюстрируйте работу функции примером. 
def sumall(x):
    if x == z:
         return x
    return x+sumall(x-1)
    
    
z, x=map(int, input().split())
print(sumall(x))


# Написать рекурсивную функцию, которая выводит N звезд в ряд, число N задает 
# пользователь. Проиллюстрируйте работу функции примером.
def stars(n):
    if n==1:
        return
    stars(n-1)
    print("*", end='')


n=int(input())
print(stars(n))


# Дано действительное положительное число a и целое неотрицательное число n. 
# Вычислите a
# n не используя циклы, возведение в степень через ** и функцию math.pow(), а 
# используя рекуррентное соотношение a
# n=a⋅a
# n-1
# . 
def power(a, n):
    if n==0:
        return 1
    else:
        return a * power(a, n-1)

a=float(input())
n=int(input())
print(power(a, n))
