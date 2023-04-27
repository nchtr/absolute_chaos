#ошибся знаками в полупериметре
import math
def circle():
    r=float(input("Введите радиус:"))
    print("Площадь комнаты",3.14*(r**2))
def par():
    a=float(input("Сторона 1: "))
    b=float(input("Сторона 2: "))
    print("Площадь комнаты=",a*b)
def tri():
    a=float(input("Сторона 1: "))
    b=float(input("Сторона 2: "))
    c=float(input("Сторона 3: "))
    hp=(a+b+c)/2
    s=math.sqrt(hp*(hp-a)*(hp-b)*(hp-c))
    print("Площадь комнаты=",s)
type=int(input("Введите форму комнаты: \n1-круг, 2-прямоугольная, 3-треугольная\n"))
if type==1:
    circle()
elif type==2:
    par()
elif type==3:
    tri()
else:
    print("Out of range")