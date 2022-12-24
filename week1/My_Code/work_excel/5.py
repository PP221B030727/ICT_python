import pprint#Dictionary print
import csv
date = []
open_list = []
high = []
with open(r"C:\Users\user\Desktop\ICT\week1\Lecture_Materials\Apple_price_csv.csv", 'r') as f:
    csv_file = csv.reader(f)
    for row in csv_file:
        date.append(row[0])
        open_list.append(row[1])
        high.append(row[2])

new_dict = {date[0] : date[1:], open_list[0]: open_list[1:], "High": high[1:]}
pprint.pprint(new_dict)