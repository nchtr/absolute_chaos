# tux`ы
n=int(input())
for i in range(n):
    print("   _~_   ", end="")
print()
for i in range(n):
    print("  (o o)  ", end="")
print()
for i in range(n):
    print(" /  V  \ ", end="")
print()
for i in range(n):
    print("/(  _  )\ ", end="")
print()
for i in range(n):
    print("  ^^ ^^  ", end="")
print()



# C.E.S.A.R
alfavit = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
move = int(input('Шаг шифровки: '))    #Создаем переменную с шагом шифровки
msg = input("Сообщение для шифровки: ").upper()    #создаем переменнную, куда запишем наше сообщение
result = ''
for i in msg:
    m = alfavit.find(i)
    new = m + move
    if i in alfavit:
        result += alfavit[new]  # Задаем значения в итог
    else:
        result += i
print (result)


#табличка
s1=10
for i in range(1, s1+1):
     for j in range(i, i*s1+1, i):
         print(j, end='\t')
     print()