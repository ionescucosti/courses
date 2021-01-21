# 838 Sqlite
# Importul de date dintr-un fisier .csv
# PF 12.01.2017 Cluj

import csv
import sqlite3

con = sqlite3.connect('info.db')
cur = con.cursor()

with open('c:/wt/medici.txt','r') as fisier: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fisier) # comma is default delimiter
    print(dr.fieldnames)
    to_db = [(i['Nume'], i['Prenume'], i['Tip'], i['Specialitate']) for i in dr]

cur.execute('create table if not exists medici(nume text, prenume text, tip text, specialitate text)')

cur.executemany("INSERT INTO medici VALUES (?, ?, ?, ?);", to_db)

# adaugare cu insert lista de tupluri
medici_noi = [('Ciobanu','Vasile', 'primar', 'ecografie'),
         ('Popescu','Mitica', 'specialist', 'parapsihologie'),
         ('Grigore','Diana', 'primar', 'cardiologie')]

cur.executemany(''' INSERT INTO medici VALUES(?,?,?,?)''', medici_noi)

con.commit()
con.close()

