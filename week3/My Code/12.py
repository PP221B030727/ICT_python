import csv
import pandas as pd
def foo(x):
    return 8*x

df = pd.read_csv(r'C:\Users\user\Desktop\ICT\week1\Lecture_Materials\Apple_price_csv.csv')
df['Open'] = df['Open'].apply(foo)
print(df)
