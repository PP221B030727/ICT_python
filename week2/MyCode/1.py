import csv 
# with open(r'C:\Users\user\Desktop\ICT\week1\Lecture_Materials\Apple_price_csv.csv','r') as csv_file:
#     for i in csv_file:
#         print(i)

# Другой варик 

with open(r'C:\Users\user\Desktop\ICT\week1\Lecture_Materials\Apple_price_csv.csv','r') as file :
    csv_file = csv.reader(file)
    csv_file.__next__()
    for row in csv_file:
        print(row)
        break
    for i in csv_file:
        print(i)
        break