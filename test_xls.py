import xlrd
book = xlrd.open_workbook('resources/file_example_XLS_10_copy.xls')
print(book.nsheets)
print(book.sheet_names())
sheet = book.sheet_by_index(0)
print(sheet.ncols)
print(sheet.nrows)
print(sheet.cell_value(rowx=9, colx=3))
for rx in range(sheet.nrows):
    sheet.row(rx).insert(1, 'value')