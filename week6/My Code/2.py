import pandas as pd
import io
import requests

headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}
resp = requests.get('https://query1.finance.yahoo.com/v7/finance/download/MSFT?period1=1633828168&period2=1665364168&interval=1d&events=history&includeAdjustedClose=true', 
                    headers = headers)


df = pd.read_csv(io.StringIO(resp.content.decode('utf-8')))
print(df)

