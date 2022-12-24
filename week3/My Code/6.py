import csv
import pandas as pd
brand = ['Coca','Nice','Hello']
taste = [6,9,8]
sugar_content = ['high','high','low']
df = pd.DataFrame(list(zip(brand,taste,sugar_content)),columns=['brand','taste','sugar'])
print(df)