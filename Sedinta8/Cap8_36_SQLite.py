import csv
import sqlite3
import sys


def main():
    con = sqlite3.connect(sys.argv[1]) # database file input
    cur = con.cursor()
    cur.executescript("""
        DROP TABLE IF EXISTS t;
        CREATE TABLE t (COL1 TEXT, COL2 TEXT);
        """) # checks to see if table exists and makes a fresh table.

    with open(sys.argv[2], "rb") as f: # CSV file input
        reader = csv.reader(f, delimiter=',') # no header information with delimiter
        for row in reader:
            to_db = [unicode(row[0], "utf8"), unicode(row[1], "utf8")] # Appends data from CSV file representing and handling of text
            cur.execute("INSERT INTO neto (COL1, COL2) VALUES(?, ?);", to_db)
            con.commit()
    con.close() # closes connection to database

if __name__=='__main__':
    main()