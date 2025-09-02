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