import openpyxl as xl


wb = xl.load_workbook('transactions.xlsx')
#In wb['Sheet'] sheet is case sensitive an needs an uppercase letter at the start
sheet = wb['Sheet1']
cell = sheet.cell(1, 1)
#print(cell.value)
#max_row = sheet.max_row
for row in range(1, sheet.max_row):
    print(row)
