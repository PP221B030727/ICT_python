import pandas as pd
df = pd.DataFrame({"Company" : ['Apple', 'Tesla', 'Microsoft'], "Creation" : [1976, 2003, 1975]}, 
                  index = ['favorite', 'so-so', 'Maybe'])
print(df)