import pymysql


# Credentiale conectare
host = "localhost"
passwd = "paul"
port = 3306  # normal portul e 3306. Daca e diferit trebuie mentionat acela
user = "root"
dbname = "world"

# Creare obiect conectare
db = pymysql.connect ( host=host, port=port, user=user, passwd=passwd, db=dbname )

# Creare cursor
cursor = db.cursor ( )

sd = 'select * from paul.people1 where numele = "john"'

# Executare cursor
cursor.execute ( sd )

# rezultatul instructiunii
results = cursor.fetchall ( )

print(results)
print (list(list(results)[1])[5])

info = ['numele', 'prenumele', 'datan', 'inaltime', 'greutate', 'an_nastere', 'id']
for row in results:
    indx = 0
    for i in row:
        print (info[indx], ':', i)
        indx +=1
    print ('---------------')


sx = 'select numele, prenumele, an_nast from paul.people1 where numele = "john"'

# Executare cursor
cursor.execute ( sx )

# rezultatul instructiunii
resultsx = cursor.fetchall ( )

print (resultsx)

infox = ['numele', 'prenumele', 'an_nastere']
for row in resultsx:
    indx = 0
    for i in row:
        print (infox[indx], ':', i)
        indx +=1
    print ('---------------')