import pandas as pd
dict = {'name':['Nurs','Ars'],'soname':['Asd','hfg'],'age':[23,412]}
df = pd.DataFrame(dict)
# print(df)
# print(df.head())
print(df['name'],'\n')
print(df['name'][1],'\n')