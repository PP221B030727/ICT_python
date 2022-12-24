import csv 
import pandas as pd
df = pd.read_csv(r'C:\Users\user\Desktop\ICT\week1\Lecture_Materials\Apple_price_csv.csv')
print(df)




print(type(df['Date'][0]))