# 816
# csv
# PF - 12.06.2017

import csv

dir(csv)

help(csv)

# csv.reader(csvfile, dialect='excel', **fmtparams)

import csv

with open('c:/wt/medici.csv', newline='', encoding='utf8') as csvfile:
    medici_reader = csv.reader(csvfile, delimiter=',', quotechar=None)
    for row in medici_reader:
        print(', '.join(row))       # listeaza fiecare rand

with open('c:/wt/medici.csv', newline='', encoding='utf8') as csvfile:
    medici_reader = csv.reader(csvfile, delimiter=',', quotechar=None)
    for row in medici_reader:
        print(row)       # listeaza liste cu fiecare rand

with open('c:/wt/medici.csv', newline='', encoding='utf8') as csvfile:
    medici_reader = csv.reader(csvfile, delimiter=',', quotechar=None)
    for row in medici_reader:
        print('***********************')
        print('Nume: '.ljust(14), row[0])
        print('Prenume: '.ljust(14), row[1])
        print('Tip: '.ljust(14), row[2])
        print('Specialitate: '.ljust(14), row[3])
        # print('***********************')          # Extrage informatiile pentru fiecare rand