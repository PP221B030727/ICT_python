#!/usr/bin/env python
# coding: utf-8

# # Work with .csv file

# In[ ]:


#import package csv to read csv files
import csv


# In[ ]:


#Open the file in python with the path of the file in your computer
file = open(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_1\Apple_price_csv.csv", 'r')


# In[ ]:


#open the file with reader function
csv_file = csv.reader(file)


# In[ ]:


#print all rows
for row in csv_file:
    print(row)


# In[ ]:


#read the file as a dict
csv_file = csv.DictReader(file)


# In[ ]:


#print all rows
for row in csv_file:
    print(row)


# In[ ]:


#Advanced reading
with open(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_1\Apple_price_csv.csv", 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        print(', '.join(row))


# In[ ]:


#Writing is also possible
with open(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_1\Test_csv_writer.csv", 'a', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';')
    spamwriter.writerow(['1', '2', '3'])
    spamwriter.writerow(['10', '2', '3'])
    spamwriter.writerow(['11', '2', '3'])


# In[2]:


#YOUR TURN
#What is the percentage of student who knows python?
#Open the file
#do number of yes divide by number of answers
#Print the result
# file on teams in the channel Lecture_wednesday_11_13
#time : 10 min => 12:05

import csv

number_of_yes = 0
total_answers = 0

with open(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_1\Skills assessment .csv\Skills assessment_modified.csv", 'r') as file:
    csv_file = csv.reader(file)
    for row in csv_file:
        total_answers += 1
        if row[1] == "Yes":
            number_of_yes += 1
            
print(number_of_yes/total_answers *100, '%')


# # Work with .json file

# In[3]:


#import json package
import json


# In[4]:


#Open Json file
json_data = open(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_1\example_json_data.json").read()


# In[5]:


#Load json data into python
data = json.loads(json_data)


# In[6]:


#Print the data (dictionnary)
for item in data:
    print(item)


# # Work with XML files

# In[7]:


#Import package
from xml.etree import ElementTree as ET


# In[8]:


#Open the file
tree = ET.parse(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_1\Example_xml_data.xml")


# In[9]:


#Get the root of your file
root = tree.getroot()
print(root)


# In[10]:


#Browse all items
for item in root:
    print(item)


# In[12]:


#Browse categories in each item and print its value
item = root[0]
for cat in item:
    print(cat)
    print(cat.text)


# In[13]:


#Modify XML file with set function
price_of_ginger = root[4][4]
print(price_of_ginger.text)
price_of_ginger.text = "$10.00"

#save file
tree.write(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_1\Example_xml_data_modified.xml")


# # Work with excel files

# ## Read excel files

# In[14]:


#Import xlrd package
import xlrd


# In[15]:


#Open a workbook
book = xlrd.open_workbook(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_1\Price_tesla_and_microsoft.xlsx")


# In[16]:


#List a tabs
for sheet in book.sheets():
    print(sheet.name)


# In[17]:


#Choose the right tab
sheet = book.sheet_by_name('Tesla_price')
#Or just to get the first tab
sheet = book.sheet_by_index(0)
print(sheet)


# In[18]:


#iterate on rows
for i in range(sheet.nrows):
    print(sheet.row_values(i))
    
print(sheet.col_values(0))


# In[19]:


#Print on cell in particular
print(sheet.cell_value(rowx=3, colx = 3))


# ## Write excel files

# In[22]:


#import the package
import xlwt


# In[27]:


#Create workbook
book = xlwt.Workbook(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_1\Price_tesla_and_microsoft.xlsx")


# In[28]:


#Add a sheet
ws = book.add_sheet('A Test Sheet')
ws = book.add_sheet('A Test Sheet1')
ws = book.add_sheet('A Test Sheet2')


# In[29]:


#Write the wanted information
for i in range(5,100):
    ws.write(i, 0, 1)
    ws.write(i, 1, 2)
    
ws.write(5, 2, xlwt.Formula("A6+B6"))


# In[30]:


#Save your file under xls
book.save(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_1\Example_excel_write.xls")


# In[ ]:


#YOUR TURN
#Write first columns of the csv file into a excel file
#Open csv file => get the first column => create excel file => write inside the first column => Save
#Time : 10 min => 12:31
#Using .xls is easier


# In[31]:


import csv

first_column = []
with open(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_1\Skills assessment .csv\Skills assessment_modified.csv", 'r') as csvfile:
    csv_read = csv.reader(csvfile)
    for row in csv_read:
        first_column.append(row[0])
print(first_column)


# In[32]:


import xlwt

book = xlwt.Workbook(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_1\your_turn.xls")
ws = book.add_sheet('result')
for i in range(0,len(first_column)):
    ws.write(i, 0, first_column[i])
book.save(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_1\your_turn.xls")


# # Transform the Data

# In[33]:


#Load data from your files
import csv
with open(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_1\Apple_price_csv.csv", 'r') as f:
    csv_file = csv.reader(f)
    for row in csv_file:
        print(row)


# In[34]:


#Use your data with lists
date = []
open_list = []
high = []
with open(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_1\Apple_price_csv.csv", 'r') as f:
    csv_file = csv.reader(f)
    for row in csv_file:
        date.append(row[0])
        open_list.append(row[1])
        high.append(row[2])
print(date[0:10])
print(open_list[0:10])


# In[35]:


#use Dicitonary
new_dict = {date[0] : date[1:], open_list[0]: open_list[1:], "High": high[1:]}
print(new_dict)


# In[36]:


#Use pprint to improve display
import pprint
pprint.pprint(new_dict)


# # Transform your data

# In[38]:


#load your datas
date = []
open_list = []
high = []
with open(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_1\Apple_price_csv.csv", 'r') as f:
    csv_file = csv.reader(f)
    for row in csv_file:
        date.append(row[0])
        open_list.append(row[1])
        high.append(row[2])
print(open_list[:10])


# In[40]:


#Float function for string to number
print(open_list[:10])
open_list = [float(i) for i in open_list[1:]]
# #OR :
# open_list = []
# for i in range(1,len(open_list)):
#     open_list[i] = float(open_list[i])
print(open_list[:10])


# In[43]:


#Datetime package for string to time
import datetime
print(date[1])
print(type(date[1]))
date_transform = datetime.datetime.strptime(date[1], '%Y-%m-%d')
print(date_transform)


# In[45]:


a = "12-01-2020 02:05"
date_transform = datetime.datetime.strptime(a, '%m-%d-%Y %H:%M')
print(date_transform)


# In[46]:


#do that for all list
date_modified = [datetime.datetime.strptime(i, '%Y-%m-%d') for i in date[1:]]
print(date_modified)


# # PANDAS

# ## Series

# In[47]:


#import package
import pandas as pd


# In[48]:


#Get the value of a column
values = ['Apple', 'Tesla', 'Microsoft']


# In[49]:


#Create a serie
my_serie = pd.Series(values)
print(my_serie)


# In[50]:


#without specification, index are the label
print(my_serie[1])


# In[54]:


#But you can specify them
my_serie = pd.Series(values, index = ['x', 'y', 'z'])
# print(my_serie)
print(my_serie['y'])


# In[55]:


#Label is automatic from a dictionary
dictionary = {"day1" : 1000, "day2": 1100, "day3": 0}
my_serie = pd.Series(dictionary)
print(my_serie)


# In[56]:


#You can choose the one you want to keep
my_serie = pd.Series(dictionary, index = ["day1", "day2"])
print(my_serie)


# ## Create DataFrame

# In[57]:


#You can create a DataFrame from a Serie
#Create an empty dataframe
df = pd.DataFrame()
print(df)


# In[59]:


#Add Series to the dataframe (index are kept)
dictionary = {"day1" : 1000, "day2": 1100, "day3": 0}
my_serie = pd.Series(dictionary)
df["My numbers"] = my_serie
# print(df)
dictionary = {"day1" : 3265, "day2": 6354, "day3": 6463}
my_serie = pd.Series(dictionary)
df["My numbers 2"] = my_serie
print(df)


# In[60]:


#From a dictionary
#Create the dataset you want to analyze
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'numbers': [3, 7, 2]
}


# In[61]:


#Create a Dataframe from the dictionary 
my_df = pd.DataFrame(mydataset)
print(my_df)


# In[62]:


#You can locate a row (return a Serie)
print(my_df.loc[1])


# In[63]:


#Or several row (return a dataframe)
print(my_df.loc[[1,2]])


# ## Modify Indexes

# In[ ]:


#Create dataframe with indexes
df = pd.DataFrame({"Company" : ['Apple', 'Tesla', 'Microsoft'], "Creation" : [1976, 2003, 1975]}, 
                  index = ['favorite', 'so-so', 'Maybe'])
print(df)


# In[ ]:


#Acces to a value with the index
print(df.loc['favorite'])


# # DataFrame for data science

# In[65]:


#Read directly csv file to dataframes
df = pd.read_csv(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_1\Apple_price_csv.csv")
# print(df)
df['2 times open'] = 2 * df['Open']
print(df)


# In[66]:


#Read directly csv file to dataframes
df = pd.read_json(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_1\Example_json_data.json")
print(df)


# ## Display a Dataframe

# In[67]:


#print all dataframe in string
print(df.to_string()) 


# In[68]:


#Print a portion of the dataframe
print(df)


# In[71]:


#change the maximum of displayed rows
print(pd.options.display.max_rows) 
# pd.options.display.max_rows = 2000
# print(df)
pd.options.display.max_rows = 4
print(df)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




