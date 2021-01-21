import pymysql as mdb

# Credentiale conectare
host = "localhost"
passwd = "paul"
port = 3306  # normal portul e 3306. Daca e diferit trebuie mentionat acela
user = "root"
dbname = "world"

try:
    con = mdb.connect(host, user, passwd, dbname, port)
    cur = con.cursor()
    cur.execute("select database()")
    output = cur.fetchall()

    print ("Output : {0}".format(output))

except mdb.Error as e:

    print ("Error {0}: {1}".format(e.args[0], e.args[1]))

finally:
    if con:
        con.close()
