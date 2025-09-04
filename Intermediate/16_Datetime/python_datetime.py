from datetime import datetime
from datetime import timedelta
from datetime import date
from datetime import time

# to know the available functions in a certain module

print(dir(datetime))

# now

now = datetime.now()
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()

print(day, month, year, hour)

#  number that represent how seconds passed since 10/01/1970 00:00:00 UTC
print(timestamp)

print(f"{day}/{month}/{year}, {hour}:{minute}")
# ...

# formatting date output using sfrtime

from datetime import datetime

new_year= datetime(2020, 1, 1)
print(new_year) # 2020-01-01 00:00:00
day = new_year.day
month = new_year.month
year = new_year.year
minute = new_year.minute
# ...

print(f"{day}/{month}/{year}")

# Formatting date time using sfrtime method 
from datetime import datetime
# current date and time
now = datetime.now()
t = now.strftime("%H:%M:S")
print("time:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("time two:", time_two)

# String to time using strptime

from datetime import datetime
date_Strnig = "5 December, 2019"
print("date_string=", date_Strnig)
date_object = datetime.strptime(date_Strnig, "%d %B, %Y")
print("date_object = ", date_object)

# using date from datetime

from datetime import date

d = date(2020, 1, 1)
print(d)
print("Current date: ", d.today())
# date object of todays date
today = date.today()
print("Current year:", today.year)
print("Current month:", today.month)

# Time objcets to represent time

from datetime import time

a = time()
print("a =", a)
# time(hour, minute, second)
b = time(10, 30, 50)
print("b= ", b)
c = time(hour=10, minute=30, second=50)
print("c = ", c)
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 20555)
print("d =", d)

# Difference between two points in time using

today = date(year=2019, month=12, day=5)
new_year = date(year = 2020, month = 1, day = 1)
time_lew_for_newyear = new_year - today

print("Time left for new year: ", time_lew_for_newyear)

t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print("diff: ", diff)

# difference between two point in time using timedelta

from datetime import timedelta

t1 = timedelta(weeks = 12, days = 10, hours = 4, seconds = 20)
t2 = timedelta(days = 7, hours = 5, minutes = 3, seconds = 30)
t3 = t1- t2
print("t3: ", t3)
