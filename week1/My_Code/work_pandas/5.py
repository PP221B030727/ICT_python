import pandas as pd
df = pd.DataFrame()
#Add Series to the dataframe (index are kept)
dictionary = {"day1" : 1000, "day2": 1100, "day3": 0}
my_serie = pd.Series(dictionary)
df["My numbers"] = my_serie
# print(df)
dictionary = {"day1" : 3265, "day2": 6354, "day3": 6463}
my_serie = pd.Series(dictionary)
df["My numbers 2"] = my_serie
print(df)