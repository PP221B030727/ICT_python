import pandas as pd
csv_file = pd.read_csv(r'C:\Users\user\Desktop\ICT\week1\Lecture_Materials\Apple_price_csv.csv')
# print(csv_file)
# print(csv_file.head(1))
# print(csv_file.tail(10))
del csv_file['Volume']
del csv_file['Adj Close']
print(csv_file)