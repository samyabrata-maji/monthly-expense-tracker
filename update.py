import csv
import os
from csv import writer
from datetime import date

input_prompt = 'FORMAT: \"tag\",\"expense\" e.g, food,40\nType \'x\' to exit.\n >>> '

# uses date as file name
# e.g. Nov_02_2022.xlsx for entries on Nov 2nd
filename = date.today().strftime('%b_%d_%y')
parent_dir = fr"{os.getcwd()}\data"
filepath_excel = fr'{parent_dir}\{filename}.xlsx'
filepath_csv = fr'{parent_dir}\{filename}.csv'

# imports csv data in a @param rows
# eg, csv -> food,40
# ---------> travel,50
# then, row[][] = [["food",40], ["travel",50]
# and, rows_dict = {"food": 40, "travel": 50}
if os.path.exists(filepath_csv):
    with open(filepath_csv, 'r') as csv_file:
        rows = list(csv.reader(csv_file))
        rows_fields = set(dict(csv.DictReader(csv_file)).keys())  # fieldnames
else:
    rows = []
    rows_fields = set()

isXPressed = False  # <-- TODO: see if there is a better way to do this
if input('Do you wish to create entries? (y/n) >>> ') == 'y':
    while not isXPressed:
        entry = input(input_prompt).strip('\n')

        # when 'x' is pressed, loop terminates
        # TODO: see if there is a better way to do this
        if entry == 'x':
            isXPressed = True
            break

        # if input does not match the format,
        # process does not get finished with exit code 0
        try:
            tag = entry.split(',')[0]
            expense = int(entry.split(',')[1])
        except ValueError and IndexError:
            print('WRONG INPUT')
            continue
        else:
            rows.append([tag, expense])
            rows_fields.add(tag)

    with open(filepath_csv, 'a') as csv_file:
        writer_obj = csv.writer(csv_file, lineterminator='\n')
        writer_obj.writerows(rows)
