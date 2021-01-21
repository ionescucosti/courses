
'''

https://docs.python.org/2/library/sqlite3.html  - documentatia oficiala - sqlite3

Intr-o bd :
    - atribut   <=>     coloana
    - tuplu     <=>     rand
    - relatie   <=>     tabela

In Sqlite identificatorii (numele de coloane, tabele, etc) sunt case sensitive
''' #

import sqlite3

connect = sqlite3.connect('info.db')    # [,timeout def 5 ,other optional arguments
                                        # Ex: ":memory:"]

cursor = connect.cursor()       # poate primi parametrul cursorClass

cursor.execute("CREATE TABLE if not exists test (DenProd text, Cant real, Pret real)")

cursor.execute("INSERT INTO test VALUES ('Paine', 100, 0.95), ('Branza', 25, 17), ('Cioco', 60, 5)")


# cursor.execute("insert into people values (?, ?)", (who, age)) - placeholdere
# cursor.executescript(sql_script)

connect.commit()

cursor.execute("SELECT * FROM test")

result = cursor.fetchall()

print(result)

# connection.rollback()

# connection.close()

# cursor.fetchone()

# cursor.fetchmany([size=cursor.arraysize])

# cursor.fetchall()

#   !  *  !  *  !  *  !

def select(baza_de_date, select_var):
    '''Functia select primeste ca parametri:
        - baza de date
        - instructiunea select
    si returneaza result set-ul corespunzator''' #
    import sqlite3
    connect = sqlite3.connect(baza_de_date)
    cur = connect.cursor()
    cur.execute(select_var)
    res = cur.fetchall()
    cur.close()
    return res

def delete(baza_de_date, delete_var):
    '''Functia delete primeste ca parametri:
        - baza de date
        - instructiunea deleet
    si sterge...''' #
    import sqlite3
    connect = sqlite3.connect(baza_de_date)
    cur = connect.cursor()
    cur.execute(delete_var)
    connect.commit()
    cur.close()

def insert(baza_de_date, insert_var):
    '''Functia delete primeste ca parametri:
        - baza de date
        - instructiunea insert
    ...''' #
    import sqlite3
    connect = sqlite3.connect(baza_de_date)
    cur = connect.cursor()
    cur.execute(insert_var)
    connect.commit()
    cur.close()

def update(baza_de_date, update_var):
    '''Functia delete primeste ca parametri:
        - baza de date
        - instructiunea insert
    ...''' #
    import sqlite3
    connect = sqlite3.connect(baza_de_date)
    cur = connect.cursor()
    cur.execute(update_var)
    connect.commit()
    cur.close()

x = select('CCR.db', 'select * from cities where field2="202"')

row = 0
for i in x:
    print(i)
    row += 1
print ('Sunt ' + str(row) + ' randuri')


select('info.db', 'select * from medici')

select('info.db', 'select * from medici where nume = "Ciublea"')
delete('info.db', 'delete from medici where nume = "Ciublea"')

insert('info.db', "insert into medici values('Ciublea','Gabriel', 'specialist', 'pneumologie')")

update('info.db', 'update medici set prenume = "Vasile" where nume = "Ciublea"')