from ast import parse
import csv 
import pandas as pd
df = pd.read_csv(r'C:\Users\user\Desktop\ICT\week1\Lecture_Materials\Apple_price_csv.csv',parse_dates=['Date'])
# print(type(df['Date'][0]))
df.columns = ['Date','Open_price','High_price','Low_price','Close_price','Adj Close','Volume']
# print(df)
df = df.rename(columns={'Date':'Date_and_time'})
print(df)


df = df.sort_values('Open_price')
print(df)





df = df.reset_index(drop = True)
print(df)


df = df.set_index(['Date_and_time'])
print(df)


# df = df.set_index(['Date_and_time', 'Open'])
# print(df)