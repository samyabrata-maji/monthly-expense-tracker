import csv
from csv import DictReader, DictWriter
import os
from datetime import date

# filepath
# uses date as file name
# e.g. Nov_02_2022.xlsx for entries on Nov 2nd
filename = date.today().strftime('%b_%d_%y')
parent_dir = fr"{os.getcwd()}\data"
filepath_excel = fr'{parent_dir}\{filename}.xlsx'
filepath_csv = fr'{parent_dir}\{filename}.csv'

# csv test


