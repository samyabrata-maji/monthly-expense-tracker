import os
import csv
import openpyxl
from datetime import date

# uses date as file name
# eg Nov_02_2022.xlsx for entries on Nov 2nd
filename = date.today().strftime('%b_%d_%y')
parent_dir = fr"{os.getcwd()}\data"
filepath_excel = fr'{parent_dir}\{filename}.xlsx'
filepath_csv = fr'{parent_dir}\{filename}.csv'
