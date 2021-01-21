import pymysql


# Credentiale conectare
host = "localhost"
passwd = "paul"
port = 3306  # normal portul e 3306. Daca e diferit trebuie mentionat acela
user = "root"
dbname = "world"

# Creare obiect conectare
db = pymysql.connect ( host='127.0.0.1', port=3306, user=user, passwd=passwd, db=dbname )

# Creare cursor
cursor = db.cursor ( )

# Executare cursor
cursor.execute ( "select code, name, continent, surfacearea, population  from country " )

# rezultatul instructiunii va fi incarcat in variabila results
results = cursor.fetchall ( )

# prelucrare informatiilor

info = ['code', 'name', 'continent', 'surfacearea', 'population']
for row in results:
    indx = 0
    for i in row:
        if indx >= 0:
            if indx == 3:
                break
            print (info[indx], ':', i)
            indx +=1
    print ('-' * 40)
