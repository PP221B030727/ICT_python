# Открываем файл CSV
import csv
file = open(r'C:\Users\user\Desktop\ICT\week1\Lecture_Materials\Apple_price_csv.csv','r')
csv_file = csv.reader(file)
for row in csv_file:
    print(row)
file.close()
#

