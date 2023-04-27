import datetime as dt
from datetime import timedelta
from datetime import date
#1
wek=dt.datetime.today().isocalendar()[1]
print(wek)

#2
rr=dt.date(2015, 1, 1)+dt.timedelta(weeks=50)
ff=rr
rr-=dt.timedelta(days=rr.weekday())
print(rr)

#3
def all_sundays(year):
    dt = date(year, 1, 1)
    dt += timedelta(days = 6 - dt.weekday())  
    while dt.year == year:
        yield dt
        dt += timedelta(days = 7)
  
for s in all_sundays(2020):
    print(s)

#4
def addYears(y, l):
    try:
       
        return y.replace(year = y.year + l)
    except ValueError:
  
        return y + (date(y.year + l, 1, 1) - date(y.year, 1, 1))
print(addYears(dt.date (2015,1,1), -1))
print(addYears(dt.date (2015,1,1), 0))
print(addYears(dt.date (2015,1,1), 2))
print(addYears(dt.date (2000,2,29), 1))