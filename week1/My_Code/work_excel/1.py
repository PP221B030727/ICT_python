import xlrd
#pip install xlrd==1.2.0
book = xlrd.open_workbook(r'C:\Users\user\Desktop\ICT\week1\Lecture_Materials\Price_tesla_and_microsoft.xlsx')
# for sheet in book.sheets():
#     print(sheet.name)



sheet = book.sheet_by_name('Tesla_price')
# #Or just to get the first tab
# sheet = book.sheet_by_index(0)
# print(sheet)



# for i in range(sheet.nrows):
    # print(sheet.row_values(i))
    
# print(sheet.col_values(0))


print(sheet.cell_value(rowx=3, colx = 3))