#1
import math
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
def fact(f):
    return math.factorial(f)
def power(p):
    return lambda o: p**o
def trig(x):
    inchs=input("Выберите:\n1-Синус угла\t2-Косинус угла\t3-Тангенс угла\t4-Котангенс угла")
    if inchs=="1":
        return print(f'Синус угла {x} = {math.sin(x)}')
    elif inchs=="2":
        return print(f'Косинус угла {x} = {math.cos(x)}')
    elif inchs=="3":
        return print(f'Тангенс угла {x} = {math.tan(x)}')
    elif inchs=="4":
        return print(f'Котангенс угла {x} = {1/math.tan(x)}')
    


print("*"*10, "Инжинерный калькулятор", "*"*10, "\n\t\tEnter to exit")
chs=input("Выберите операцию:\n1-Ряд Фибоначчи\t2-Факториал\t3-Степень числа\t4-Тригонометрия\n")
while chs!="":
    if chs=="1":
        print(f'Ряд {fibonacci(int(input("Введите число: ")))}')
    elif chs=="2":
        print(f'Факториал числа равен {fact(int(input("Введите число: ")))}')
    elif chs=="3":
        lam = power(int(input("Введите число: ")))
        print(f'Число в степени равно {lam(int(input("Введите степень: ")))}')
    elif chs=="4":
        trig(int(input("Угол в градусах: ")))
    else:
        print("Неверный ввод, повторите попытку")
    


#2
def main(sset):         #основной процесс игры
    score = 0
    win = False
    while not win:
        setdraw(sset)
        if score % 2 == 0:
           setdraw("X")
        else:
           inp("O")
        score += 1
        if score > 4:
           t = res(sset)
           if t:
              print(t, "wins!")
              win = True
              break
        if score == 9:
            print("Draw")
            break
    setdraw(sset)
def setdraw(sset):          #рисуем поле
   print("-" * 13)
   for i in range(3):
      print("|", sset[0+i*3], "|", sset[1+i*3], "|", sset[2+i*3], "|")
      print("-" * 13)
def res(sset):      #собираем результаты
   victory = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for c in victory:
       if sset[c[0]] == sset[c[1]] == sset[c[2]]:
          return sset[c[0]]
   return False
def inp(choose):        #ввод ходов
   is1 = False
   while not is1:
      pchoose = input(f"Куда поставим {choose} ? ")
      try:
         pchoose = int(pchoose)
      except:
         print("Повторите попытку")
         continue
      if pchoose >= 1 and pchoose <= 9:
         if(str(sset[pchoose-1]) not in "XO"):
            sset[pchoose-1] = choose
            is1 = True
         else:
            print("Занята!")
      else:
        print("Повторите попытку, введите числа 1-9")



print("*"*10, " Игра Крестики-нолики для двух игроков ", "*"*10)
sset = list(range(1,10))
main(sset)
input("Enter to exit")