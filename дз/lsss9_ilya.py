#1
from datetime import datetime, timedelta
def last_day(n):
    b=f.replace(days=28) + timedelta(days=4)
inp=input()
f='%Y %b'
last_da=datetime.datetime.strftime(inp, f)
print(last_da.strftime('%A'))
#2
dnow=datetime.datetime.now()
fday=datetime.datetime()