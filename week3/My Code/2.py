import csv
import pandas as pd
with open(r'C:\Users\user\Desktop\ICT\week1\Lecture_Materials\Apple_price_csv.csv','r') as file:
    dict = csv.DictReader(file)
    df = pd.DataFrame(dict) 
print(df)   





