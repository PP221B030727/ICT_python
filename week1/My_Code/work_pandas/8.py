import pandas as pd
df = pd.read_csv(r"C:\Users\user\Desktop\ICT\week1\Lecture_Materials\Apple_price_csv.csv")
# print(df)
df['2 times open'] = 2 * df['Open']
print(df)