import csv
# open with dictionnary 

with open(r'C:\Users\user\Desktop\ICT\week1\Lecture_Materials\Apple_price_csv.csv','r') as file:
    csv_dict = csv.DictReader(file)
    csv_dict.__next__()
    cnt = 0
    for i in csv_dict:
        print(i)
        cnt+=1
        if(cnt == 2):
            break
    cnt = 0
    for i in csv_dict:
        print(i)
        cnt+=1
        if(cnt == 3):
            break






