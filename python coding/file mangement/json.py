from fileinput import filename

from openpyxl import workbook,load_workbook
import csv
import os
from logging import getLevelName


def write_json(filename):
    dats={}
        'people':[
        {'name':'shreya','age':22}
        ]
    }

    with open(filename("w") as file:
        json.dump(data,file,indent=4)
    print(f'wrote{filename}sucessfully')

    def read_json(filename):
        with open(filename,'r')as file:
            data=json.load(file)
            for persin in data['people']:
                print(f'Nmae:{person['name']},age:{person}['age'])

    def delete_json(filename):
            if os.path.exists(filename):
                os.remove(filename)
                print(f'print{filename} deleted successfully')
            else:
                print(f'{filename} not deleted')

        

filename='myfile.csv'
write_csv(filename)
print('Data read from :')
read_csv(filename)
delete_csv(filename)
