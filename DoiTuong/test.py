from datetime import datetime

# dates in string format
str_d1 = '6:00'
str_d2 = '8:30'

# convert string to date object
d1 = datetime.strptime(str_d1, "%H:%M")
d2 = datetime.strptime(str_d2, "%H:%M")

# difference between dates in timedelta
delta = d2 - d1
print(f'{delta.seconds/3600}')