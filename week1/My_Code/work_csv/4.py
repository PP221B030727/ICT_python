import csv
with open(r'C:\Users\user\Desktop\ICT\week1\Lecture_Materials\Apple_price_csv.csv','r') as csvfile:
    spam = csv.reader(csvfile,delimiter=',')
    cnt_for_data = 0
    just_cnt = 0
    
    for row in spam:
        if(row[1]>"50"):
            cnt_for_data+=1
        just_cnt+=1
    print(cnt_for_data/just_cnt*100,'%')
