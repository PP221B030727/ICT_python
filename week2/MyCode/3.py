import csv
list1 = []
list2 = []
list3 = []
with open(r'C:\Users\user\Desktop\ICT\week1\Lecture_Materials\Apple_price_csv.csv','r') as file: 
    csv_file = csv.reader(file)
    
    for i in csv_file:
        # print(type(i[1]))
        list1.append(i[0])
        list2.append(i[1])
        list3.append(i[2])
        # list2.append(csv_file[1])
        # list3.append(csv_file[2])
    print(list1[:12])

    