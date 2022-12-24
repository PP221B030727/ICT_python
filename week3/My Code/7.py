import csv
import pandas as pd

with open(r'C:\Users\user\Desktop\ICT\week1\Lecture_Materials\Apple_price_csv.csv','r') as file:
    csvfile = csv.reader(file)
    column_names = csvfile.__next__()
    df = pd.DataFrame(csvfile,columns = column_names)
print(df)