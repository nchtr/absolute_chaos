import datetime as dt
import pytz
import calendar
from time import strftime
import time

#1
print(time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime()))
print(strftime("%a, %d %b %Y %I:%M:%S %p %Z"))

#2
print(dt.date(2014, 7, 11) - dt.date(2014, 7, 2))

#3

def date_diff_in_seconds(dt2, dt1):
  timedelta = dt2 - dt1
  return timedelta.days * 24 * 3600 + timedelta.seconds
def dhms_from_seconds(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	days, hours = divmod(hours, 24)
	return (days, hours, minutes, seconds)

date1 = dt.datetime.strptime('2015-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')

date2 = dt.datetime.now()
print("%d, %d, %d, %d" % dhms_from_seconds(date_diff_in_seconds(date2, date1)))
print()

#4
# htmlcal = calendar.HTMLCalendar(calendar.MONDAY)
# print(htmlcal.formatmonth(2020, 12))
