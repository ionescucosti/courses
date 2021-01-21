

import pymysql as mdb

# Credentiale conectare
host = "localhost"
passwd = "paul"
port = 3306  # normal portul e 3306. Daca e diferit trebuie mentionat acela
user = "root"
dbname = "test"

con = mdb.connect(host, user, passwd, dbname)

cur = con.cursor()

con2 = mdb.connect(host, user, passwd, 'localitati')

curs2 = con2.cursor()

curs2.execute( """CREATE OR REPLACE VIEW Productii AS SELECT jud, loc,  ua,
	PS.cant_t as Sfecla_tone, po.cant_miib as Oua_miibuc
	FROM judete
    left join localitati on judete.idj = localitati.idj
    left join unita on localitati.idua = unita.idua
    left join ps on ps.idl = localitati.idl
    left join po on localitati.idl = po.idl;""")



curs2.execute('select * from Productii')

rezultat2 = curs2.fetchall()

x = curs2.execute('select * from Productii')

'''Printare stil tabel'''

print('{:<20}'.format('Judetul'),
        '{0}'.format('Localitatea').ljust(20),
        '{0}'.format('Unit Admin').ljust(12),
        '{0}'.format('Sfecla').rjust(10),
        '{0}'.format('Oua').rjust(10))
print('*----------------------------------------------------------------------*')
for row in rezultat2:
    j = row[0]
    l = row[1]
    u = row[2]
    s = row[3]
    o = row[4]
    print('{:<20}'.format(j),
        '{0}'.format(l).ljust(20),
        '{0}'.format(u).ljust(12),
        '{:.2f}'.format(s).rjust(10),
        '{:.2f}'.format(o).rjust(10))
print('*----------------------------------------------------------------------*')
print('{:<20}'.format('Judetul'),
        '{0}'.format('Localitatea').ljust(20),
        '{0}'.format('Unit Admin').ljust(12),
        '{0}'.format('Sfecla').rjust(10),
        '{0}'.format('Oua').rjust(10))
print('*----------------------------------------------------------------------*')
print('Au fost returnate {0} inregistrari'.format(x))


'''Printare desfasurata, pe localitate'''

lista_1 = ['Jud', 'Loc', 'UnitAdm', 'ProdSfecla', 'ProdOua']

for row in rezultat2:
   for i in lista_1:
        j = row[0]
        l = row[1]
        u = row[2]
        s = row[3]
        o = row[4]
        print('\n', lista_1[0],j,'\n', lista_1[1], l, '\n', lista_1[2], u, '\n', lista_1[3], s, '\n', lista_1[4], o)
        print('*---------------------*')

cheie = 1
dictionar = dict()
for row in rezultat2:
    Nume = row[0]
    Expl = row[1]
    dictionar[Nume] = Expl


