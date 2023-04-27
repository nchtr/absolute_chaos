# Написать рекурсивную функцию, которая по заданному целому числу возвращает n-e
# число Фибоначчи. Ряд Фибоначчи 0, 1, 1, 2, 3, 5, 8, 13,……
def fib(n,c=0,p=1):
    if n==0:
        return c
    else:
        return fib(n-1,c+p,c)

n=int(input("Enter n number: "))
for i in range(1, n+1):
    print(f'the fibonacci number {i} = {fib(i)}')
    n-=1



# Напишите функцию, которая проверяет является ли число степенью двойки. Если 
# истинно выведите True, иначе False.
def sqroftwo(a):                    #а так как не указано какая должна быть функция, решение будет таким :)
    while a!=1 and a/2!=1:
        a=a-(a/2)
        if a==int(a):
            continue
        elif a!=int(a):
            print('False')
            break
    if a/2==1 or a==1:
            print('True')
print(sqroftwo(int(input())))