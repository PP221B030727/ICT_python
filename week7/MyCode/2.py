import pandas as pd
# df = pd.read_csv(r"C:\Users\user\Desktop\ICT\week7\Lecture Materials\Apple_price_to_clean.csv")
# print(df)
# print(df.isnull())






# import pandas as pd

# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }

# myvar = pd.DataFrame(mydataset)

# print(myvar.loc[0])


# #Non standard missing values : na_values in the read_csv function
# #use of unique function to identify them
# na_value = ['na', '--']
# df = pd.read_csv(r"C:\Users\user\Desktop\ICT\week7\Lecture Materials\Apple_price_to_clean.csv", na_values = na_value)
# print(df.isnull())



# With the index argument, you can name your own indexes.

# import pandas as pd

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

# df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

# print(df) 
# import pandas as pd

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

# df = pd.DataFrame(data, index = ["day1", "day2", "day3"])


# # df = pd.DataFrame(data,index =["day4"]); 
# # df = pd.DataFrame(data,index=["day1"])
# # print(df)
# df2 = pd.DataFrame(data)
# df.plot()

# # print(df2.head())
# df.fillna("day1","day2")
# print(df.to_string())





#Unexpected format missing values : check if value can be int for example
import numpy as np
import pandas as pd
df = pd.read_csv(r"C:\Users\user\Desktop\ICT\week7\Lecture Materials\Apple_price_to_clean.csv")


for index, line in df.iterrows():
    try:
        int(line['OWN_OCCUPIED'])
        print(line['OWN_OCCUPIED'])
        df.loc[index, 'OWN_OCCUPIED'] = np.nan
    except:
        pass


df = df.fillna(method = 'ffill')
# print(df)




import numpy as np

arr = np.array([10, 15, 20, 25, 30, 35, 40])
print(arr[1:4])



#delete lines with dropna with subset and inplace aeguments
df.dropna(inplace = True)
print(df)




# Location based replacement with the loc function
print(df)
df = df.loc[6, 'OWN_OCCUPIED'] = 'Y'
# print(df)





#Replacing the missing values with a median 
#(calculate median and then use the replace with a number)
print(df['NUM_BEDROOMS'].mean())
df.fillna(int(df['NUM_BEDROOMS'].mean()), inplace = True)
print(df)





#Read csv with clean data
na_value = ['na', '--']
df = pd.read_csv(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_7\csv_to_clean.csv", na_values = na_value)
print(df)
df.dropna(inplace = True, subset = ['SQ_M'])
print(df)



#With the describe method
print(df.describe())





# With the plot method
df.plot(y = 'SQ_M')


# In[93]:


df = df[df['SQ_M'] < 10000]
df.plot(y = 'SQ_M')


# In[ ]:


#YOUR TURN (10 min)
#Find the outliers in your dataset and remove them
#=> 18:46


