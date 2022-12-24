import pandas as pd
df = pd.read_json(r"C:\Users\user\Desktop\ICT\week1\Lecture_Materials\Example_json_data.json")
print(df)
#print all dataframe in string
print(df.to_string()) 