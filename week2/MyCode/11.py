import pandas as pd
import datetime
df = pd.read_csv(r'C:\Users\user\Desktop\ICT\week1\Lecture_Materials\Apple_price_csv.csv',header=0,names=['Date', 'Open price', 'High price', 'Low price', 'Close price', 'Adjusted close price', 'Volume exchanged'],parse_dates = ['Date'])
# print(df)
# print(type(df['Date'][0]))
# print(df['Date'][0])



# print(df.loc[0,:])
# print(df.iloc[0,:])
# print(df.loc[[1,2,3],:])
# print(df.iloc[[1,2,3], 2])
# print(df.loc[[1,2], ['High price']])


# print(df.loc[range(0,10), ['Date', 'High price']])


# print(df['Open price'] > 100)
# print(df[ df['Open price'] > 100 ])
begining_date = datetime.datetime(year = 2020, month = 1, day = 1)
ending_date = datetime.datetime(year = 2021, month = 1, day = 1)
df_begin = df['Date'] > begining_date
df_end = df['Date'] < ending_date
# print(df_begin)

# print(df[(df['Date'] > begining_date) & (df['Date'] < ending_date) & (df['Open price'] <75)])
print(df.sort_values(['Low price']))




