from email import header
import requests
import pandas as pd
import io
l = ['TSLA','MSFT','AAPL']
for i in l:
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
    resp = requests.get('https://query1.finance.yahoo.com/v7/finance/download/'+i+'?period1=1633828168&period2=1665364168&interval=1d&events=history&includeAdjustedClose=true',
    headers = headers)
df = pd.read_csv(io.StringIO(resp.content.decode('utf-8')))
print(df)