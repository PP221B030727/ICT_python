import datetime
import requests
origin_date = datetime.datetime(year=1970,month=1,day=1)
begin_date = datetime.datetime(year = 2022,month=10,day=4)
begin_seconds = begin_date-origin_date
end_date = datetime.datetime(year = 2022, month = 10, day = 4)
end_seconds = end_date-origin_date




parameters = {'period1' : str(int(begin_seconds.total_seconds())), 'period2' : str(int(end_seconds.total_seconds())), 'interval' : '1d', 'events': 'history',
              'includeAdjustedClose': 'true'}
# print(parameters)
headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}


resp = requests.get('https://query1.finance.yahoo.com/v7/finance/download/MSFT', params = parameters ,
                    headers = headers)
print(resp.content)





