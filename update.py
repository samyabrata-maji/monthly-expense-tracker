import os
from csv import writer
from datetime import date

# uses date as file name
# e.g. Nov_02_2022.xlsx for entries on Nov 2nd
filename = date.today().strftime('%b_%d_%y')
parent_dir = fr"{os.getcwd()}\data"
filepath_excel = fr'{parent_dir}\{filename}.xlsx'
filepath_csv = fr'{parent_dir}\{filename}.csv'

rows = []
isXPressed = False
if input('Do you wish to create entries? (y/n) >>> ') == 'y':
    while not isXPressed:
        entry = input('FORMAT: \"tag\",\"expense\" e.g, food,40\nType \'x\' to exit.\n >>> ').strip('\n')

        # when 'x' is pressed, loop terminates
        if entry == 'x':
            isXPressed = True
            break

        # if input does not match the format,
        # no exception is thrown
        try:
            tag = entry.split(',')[0]
            expense = int(entry.split(',')[1])
            print(expense)
        except ValueError and IndexError:
            print('WRONG INPUT')
            continue
        else:
            rows.append([tag, expense])

    with open(filepath_csv, 'a') as csv_file:
        writer_obj = writer(csv_file, lineterminator='\n')
        writer_obj.writerows(rows)
