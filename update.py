import csv
import os
from datetime import date

# uses date as file name
# e.g. Nov_02_2022.xlsx for entries on Nov 2nd
filename = date.today().strftime('%b_%d_%y')
parent_dir = fr"{os.getcwd()}\data"
filepath_excel = fr'{parent_dir}\{filename}.xlsx'
filepath_csv = fr'{parent_dir}\{filename}.csv'

isXPressed = False
if input('Do you wish to create entries? (y/n) >>> ') == 'y':
    while not isXPressed:
        entry = input('Format: \"tag\",\"expense\"\n e.g, food,40\nType \'x\' to exit.\n >>> ')
        if entry == 'x':
            isXPressed = True
            break

        try:
            tag = entry.split(',')[0]
            expense = int(entry.split(',')[1])
        except ValueError and IndexError:
            print('WRONG INPUT\nFormat: \"tag\",\"expense\"\n e.g, food,40\nType \'x\' to exit.\n >>> ')
            continue

        with open(filepath_csv, 'a+') as csv_file:
            reader = csv.reader(csv_file=csv_file)

