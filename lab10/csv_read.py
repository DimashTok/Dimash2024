import csv

filename = 'C:/Users/Dimash/Desktop/Dimash2024PP2/lab10/phone.csv'

with open(filename, "r") as file:
    csvreader = csv.reader(file, delimiter=',')
    for row in csvreader:
        name, surname, pn = row
        print(name,pn)