from xml.etree import ElementTree as ET
tree = ET.parse(r'C:\Users\user\Desktop\ICT\week1\Lecture_Materials\Example_xml_data.xml')
root = tree.getroot()
# for item in root:
#     # print(item)
#     for i in item:
#         print(i)
#         print(i.text)
# print(root)

price_of_ginger = root[4][4]
print(price_of_ginger.text)
price_of_ginger.text = "$10.00"
# Открытия и спуск данные ХML