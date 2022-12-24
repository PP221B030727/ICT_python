# import csv


# lists = [[] for i in range(7)]
# # print(lists)

# with open(r'C:\Users\user\Desktop\ICT\week1\Lecture_Materials\Apple_price_csv.csv','r') as file:
#     csv_file = csv.reader(file)
#     for row in csv_file:
#         for i in range(7):
#             lists[i].append(row[i])
#     # print(lists)

# print(lists[0][:10])
# print(lists[1][:10])
# # Фича






















import csv 
lists = [[] for i in range(7)]
# print(lists)
with open(r'C:\Users\user\Desktop\ICT\week1\Lecture_Materials\Apple_price_csv.csv','r') as file:
    csv_file = csv.reader(file)
    for row in csv_file:
        for i in range(7):
            lists[i].append(row[i])
    print(lists[0][0:5])
    print(lists[1][0:5])
    print(lists[2][0:5])
    print(lists[3][0:5])
    print(lists[4][0:5])
    print(lists[5][0:5])
    print(lists[6][0:5])




