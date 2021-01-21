import pymysql as mdb

# Credentiale conectare
host = "localhost"
passwd = "paul"
port = 3306  # normal portul e 3306. Daca e diferit trebuie mentionat acela
user = "root"
dbname = "test"

con = mdb.connect(host, user, passwd, dbname)

cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS Autor")
cur.execute("CREATE TABLE Autor(Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(25))")
cur.execute("INSERT INTO Autor(Name) VALUES('Marin Sorescu'),('Nichita Stanescu')")
cur.execute("INSERT INTO Autor(Name) VALUES('Lucian Blaga')")
cur.execute("INSERT INTO Autor(Name) VALUES('George Toparceanu')")
x = "INSERT INTO Autor(Name) VALUES({0})".format('"Mihai Eminescu"')
cur.execute(x)

cur.execute ( "UPDATE Autor SET Name = %s WHERE Id = %s",("Tudor Arghezi", '4') )

autor = 'select * from autor'

cur.execute(autor)

rezultat = cur.fetchall ( )

print (rezultat)

print ('\n')

for row in rezultat:
    print (row)

print ('\n')

for row in rezultat:
    print (row[0], row[1])

con.commit()

cur.close()

