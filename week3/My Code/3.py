import csv
import pandas as pd
brand = ['Coca','Nice','Hello']
taste = [6,9,8]
sugar_content = ['high','high','low']



df = pd.DataFrame([brand,taste,sugar_content])
print(df)