import pandas as pd
values = ['Apple', 'Tesla', 'Microsoft']
values2 = ['Hello','Nursultan','This is a ','pandas','series']
my_series2 = pd.Series(values2)
my_serie = pd.Series(values)
my_series = pd.Series(values, index = ['x', 'y', 'z'])#Можно изменить i... на x,y...
# print(my_serie)
print(my_series['y'])
# print(my_serie)
# print(my_series2)