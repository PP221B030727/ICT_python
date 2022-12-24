import pandas as pd
df = pd.read_csv(r'C:\Users\user\Desktop\ICT\week1\Lecture_Materials\Apple_price_csv.csv')



# for index,item in df.iterrows():
    # print(item['Date'],index)


df = pd.concat([df,df])
print(df)