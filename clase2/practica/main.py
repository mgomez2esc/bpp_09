# Miguel Gómez Gómez-Escalonilla
# miguel.gomez.escalonilla@gmail.com
# Practica02

import csv
import pandas as pd

filename = 'persona.csv'

def ingresar_persona(my_name, my_sunrname, my_age, my_email):
    
    with open(filename, 'a', newline='') as csvile:
        fieldnames = ['name', 'surname', 'age', 'email']
        writer = csv.DictWriter(csvile, fieldnames=fieldnames)
        writer.writerow({'name': my_name, 'surname': my_sunrname,
                         'age': my_age, 'email': my_email})

def leer_archivo(generic_value):

    my_list = []

    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            for column in row:
                if (column == generic_value):
                    my_list.append(row)
    
    return my_list

def return_file():

    df = pd.read_csv(filename)

    return df
