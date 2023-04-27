# Количество дней в месяце варьируется от 28 до 31. Очередная ваша программа
# должна запрашивать у пользователя название месяца и отображать количество
# дней в нем. Поскольку годы мы не учитываем, для февраля можно вывести 
# сообщение о том, что этот месяц может состоять как из 28, так и из 29 дней, 
# чтобы учесть фактор високосного года.
month=int(input("Choose month:\n 1-January 2-February 3-March 4-April 5-May 6-June\n7-July 8-August 9-September 10-October 11-November 12-December\n"))
if month==2:print("28 days or 29 if it's a leap year")
elif month==4 or month==6 or month==9 or month==11:print("30 days in this month")
elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:print("31 days in this month")
else:print("this mouth is not exist")
#самое радикальное решение)))

    