import json

# Open json file

json_data = open(r'C:\Users\user\Desktop\ICT\week1\Lecture_Materials\Example_json_data.json','r')
jsonfile=json_data.read()
data = json.loads(jsonfile)
# print(data)
for item in data:
    print(item)
    # for i in item:
    #     print(i)
json_data.close()