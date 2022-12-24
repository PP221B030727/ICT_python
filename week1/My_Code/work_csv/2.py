import csv
with open(r'C:\Users\user\Desktop\ICT\week1\Lecture_Materials\Apple_price_csv.csv','r') as csv_file:
    spamreader = csv.reader(csv_file,delimiter=',')
    for row in spamreader:
        print(', '.join(row))
        # print(row)
#Продвинутый уровень открытия файлов 
