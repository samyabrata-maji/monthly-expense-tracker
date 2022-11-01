import os
import csv
import openpyxl
from datetime import date

filename = date.today().strftime('%b_%d_%y')
parent_dir = f'{os.getcwd()}\\data\\'
filepath_excel = f'{parent_dir}{filename}.xlsx'
filepath_csv = f'{parent_dir}{filename}.csv'

print(filepath_excel)
print(filepath_csv)


def import_from_csv(worksheet, workbook):
    with open(filepath_csv) as csv_file:
        reader = csv.reader(csv_file, delimiter=':')
        for row in reader:
            worksheet.append(row)
    workbook.save('file.xlsx')


if not os.path.exists(filepath_excel):
    wb = openpyxl.Workbook()
    ws = wb.create_sheet()
    wb.save(filename=filepath_excel)
    print(f'File {filename}.xlsx created successfully')
else:
    print('File already created')
    wb = openpyxl.load_workbook(filename=filepath_excel)
    ws = wb.active

if input('Import CSV data? (y/n)') == 'y':
    print('importing...')
    import_from_csv(workbook=wb, worksheet=ws)

wb.close()
