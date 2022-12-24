import csv
lists = [[] for i in range(7)]
with open(r'C:\Users\user\Desktop\ICT\week1\Lecture_Materials\Apple_price_csv.csv','r') as file:
    csv_file = csv.reader(file)
    for row in csv_file:
        for i in range(7):
            lists[i].append(row[i])
    

    for i in range(1,len(lists[1:])):
        lists[i] = [float(j) for j in lists[1:]]
        # print(lists[i])
    # print(lists[1][:10])


    #хз чет не раб
    