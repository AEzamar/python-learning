import openpyxl as xl
from openpyxl.chart import BarChart, Reference


wb = xl.load_workbook('transactions.xlsx')
#In wb['Sheet'] sheet is case sensitive an needs an uppercase letter at the start
sheet = wb['Sheet1']
#cell = sheet.cell(1, 1)
#print(cell.value)
#max_row = sheet.max_row
for row in range(2, sheet.max_row + 1):
    cell = sheet.cell(row, 3)
    corrected_price = cell.value * 0.9
    corrected_price_cell = sheet.cell(row, 4)
    corrected_price_cell.value = corrected_price

Reference(sheet, 
    min_row=2, 
    max_row = sheet.max_row,
    min_col = 4,
    max_col = 4)
wb.save('transactons2.xlsx')
