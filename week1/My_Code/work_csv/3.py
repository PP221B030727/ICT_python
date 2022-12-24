import csv
with open(r'C:\Users\user\Desktop\ICT\week1\Lecture_Materials\Test_csv_writer.csv','w') as csvfile:
    spamwrite = csv.writer(csvfile,delimiter = ',')
    spamwrite.writerow(['1','2','3'])
    spamwrite.writerow(['4','5','6'])
    spamwrite.writerow(['7','8','9'])

#Пример как писать в CSV файл


