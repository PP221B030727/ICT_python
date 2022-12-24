import xlwt



book = xlwt.Workbook(r"C:\Users\user\Desktop\ICT\week1\Lecture_Materials\Test.xlsx")
ws = book.add_sheet('A Test Sheet')
ws = book.add_sheet('A Test Sheet1')
ws = book.add_sheet('A Test Sheet2')
for i in range(5,100):
    ws.write(i, 0, 1)
    ws.write(i, 1, 2)
    
ws.write(5, 2, xlwt.Formula("A6+B6"))
book.save(r"C:\Users\user\Desktop\ICT\week1\Lecture_Materials\Test.xlsx")