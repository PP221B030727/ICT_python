import csv
import pandas 
df = pandas.read_csv(r'C:\Users\user\Desktop\ICT\week1\Lecture_Materials\Apple_price_csv.csv')
print(df)
df['name'] = ['Chardon' for i in range(0,1763)]
df['Surname'] = 'Hello World'
print(df)