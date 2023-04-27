# Напишите программу, определяющую вид фигуры по количеству ее сторон. Запросите у 
# пользователя количество сторон и выведите сообщение с  указанием вида фигуры.
#  Программа должна корректно обрабатывать и выводить названия для фигур с количеством
#   сторон от трех до десяти включительно. Если введенное пользователем значение 
#   находится за границами этого диапазона, уведомите его об этом.
print("count of sides of the figure:")
c=int(input())
def cofs():
    if c==10:
        print("This is a dexagon")
    elif c==9:
        print("This is a nonagon")
    elif c==8:
        print("This is a octagon")
    elif c==7:
        print("This is a heptagon")
    elif c==6:
        print("This is a hexagon")
    elif c==5:
        print("This is a pentagon")
    elif c==4:
        print("This is a square")
    elif c==3:
        print("This is a triangle")
    elif c>3 or c<10:
        print("No such figure exists")
cofs()