import csv 
import pandas as pd
dic = {
    "Brand" : ['Coca', 'pepsi', 'Sprite', 'water'],
    "Taste" : [5, 6, 9, 8],
    "Sugar_content" : ['high', 'high', 'high', 'low']
}

df1 = pd.DataFrame(dic)
df = pd.concat([df1,df1])
print(df)




df = df.drop_duplicates()
print(df) 


