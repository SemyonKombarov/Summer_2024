import openpyxl
from openpyxl import Workbook

f_in = open("spisok.txt", encoding="utf-8")
lst = []
for i in f_in:
    lst.append(i.strip().split(","))
f_in.close()
print(lst)
def sort_lst(x):
    return x[3],x[1],x[2]
lst_sort = sorted(lst, key= lambda x: sort_lst(x))

wb = Workbook()
wb.save("excel.xlsx")
print(wb.sheetnames)
ws = wb.active
k = 1
for i in lst_sort:
    ws.append(i)
wb.save("excel.xlsx")


