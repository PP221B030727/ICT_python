import pandas as pd
dictionary = {"day1" : 1000, "day2": 1100, "day3": 0}
my_serie = pd.Series(dictionary, index = ["day1", "day2"])
print(my_serie)