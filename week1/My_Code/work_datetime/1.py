import datetime
a = "12-01-2020 02:05"
date_transform = datetime.datetime.strptime(a, '%m-%d-%Y %H:%M')
print(date_transform)