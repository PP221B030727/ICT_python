import pandas as pd
import csv
import xlrd
df = pd.read_csv(r'C:\Users\user\Desktop\ICT\week1\Lecture_Materials\Apple_price_csv.csv')
writer = pd.ExcelWriter(r'C:\Users\user\Desktop\ICT\week3\My Code\df.xlsx')
# df['Date'][1:].to_excel(writer,'DataFrame')
df.to_excel(writer,'DataFrame')
writer.save()

# print(df['Date'][:])