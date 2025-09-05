# Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime
from datetime import date

current_day = datetime.now()

year = current_day.year
month = current_day.month
day = current_day.day
hour = current_day.hour
minute = current_day.minute
seconds = current_day.second
timestamp = current_day.timestamp()

print(f"Date and time: {year}/{month}/{day} {hour}:{minute}:{seconds} timestamp: {timestamp}")

# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")

now = datetime.now()

time = now.strftime("%m/%d/%Y , %H:%M:%S")

print(time)

# Today is 5 December, 2019. Change this time string to time.

date_1 = "5 December, 2019"
str_Date = datetime.strptime(date_1, "%d %B, %Y")
print(str_Date)

# Calculate the time difference between now and new year.

now = datetime.now()
new_year = datetime(2026, 1, 1, 0, 0, 0)

diff = new_year - now
print(diff)

# Calculate the time difference between 1 January 1970 and now.

date_2 = date(1970, 1, 1)
now = date.today()

diff = now - date_2
print(diff)