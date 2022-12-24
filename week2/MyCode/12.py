import pandas as pd
import datetime
df = pd.read_csv(r"C:\Users\user\Desktop\ICT\week1\Lecture_Materials\Apple_price_csv.csv", 
                 parse_dates = ['Date'])

begining_date = datetime.datetime(year = 2019, month = 1, day = 1)
ending_date = datetime.datetime(year = 2020, month = 1, day = 1)
average = df[(df['Date'] > begining_date) & (df['Date'] < ending_date)].loc[:, ['High']].mean()
print(average[0])


begining_date = datetime.datetime(year = 2021, month = 1, day = 1)
ending_date = datetime.datetime(year = 2022, month = 1, day = 1)

print(df[(df['Date'] > begining_date) & (df['Date'] < ending_date) &   (df['High'] > average[0]) ].loc[:, ['Date', 'Volume', 'High']])