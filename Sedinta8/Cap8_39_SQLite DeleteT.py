# 839 Sqlite
# Curatenie in daza de date
# PF 12.01.2017 Cluj

import sqlite3

con = sqlite3.connect('c:/wt/info.db')
cur = con.cursor()

cur.execute('drop table if exists test')
cur.execute('drop table if exists medici')
