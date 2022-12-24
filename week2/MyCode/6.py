import datetime 
import csv
listDataobject = []
with open(r'C:\Users\user\Desktop\ICT\week1\Lecture_Materials\Apple_price_csv.csv','r') as file:
    csv_file = csv.reader(file)
    # for row in csv_file:
        # print(row)
        # listDataobject.append(datetime.datetime.strptime(row[0],"%Y-%m-%d"))
    # dateObject = 
    # print(csv_file)
    # listDataobject.append(datetime.datetime.strptime(csv_file[1:],"%d-%m-%Y"))
        
    # print(listDataobject)      
date = "2025-02-01"
dateObject = datetime.datetime.strptime(date,"%d/%m/%Y")
print(dateObject.weekday()) 
# print(dateObject.date())
# print(dateObject.ctime())

