from openpyxl import workbook,load_workbook
import csv
import os
from logging import getLevelName


def write_csv(filename):
    dats=[
        {'name':'shreya','age':22}
    ]
    coulmnnames=['name','age']
    with open(filename,'w',newline='\n')  as file:
        writer=csv.DictWriter(Ffil,fileldname=coulmnname)
        writer.writeheader()
        writer.writer(data)

def delete_csv(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f'{filename} deleted successfully')
    else:
        print(f'{filename} not deleted')


filename='myfile.csv'
write_csv(filename)
print('Data read from csv :')
read_csv(filename)
delete_csv(filename)
