import datetime
origin_date = datetime.datetime(year=1970,month=1,day=1)
begin_date = datetime.datetime(year = 2022,month=10,day=4)
difference = begin_date-origin_date
print(difference.total_seconds())