import pandas as pd
dictio = {'name' : ['Brad', 'Angelina', 'Robert'], 'surname' : ['Pitt', 'Joly', 'wilson'], 'age' : [50, 40, 60]}
df = pd.DataFrame(dictio)
df.index = ['' for i in range(len(df))]
print(df.index)