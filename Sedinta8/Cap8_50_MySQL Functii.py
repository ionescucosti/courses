# 850 MySQL
# Functii utile pentru diferite operatiuni
# PF - 12/10/2017 - v3

"""
Contine urmatoarele functii pentru manipularea datelor:
 - select;
 - delete;
 - insert;
 - update.
Functiile primesc ca parametri baza de date de accesat si instructiunea
specifica. Se conecteaza automat la baza de date, creaza cursorul si efectueaza 
operatiunea, iar in final valideaza operatiunea si inschide conexiunea


"""#

def select(baza_de_date, select_var):
    '''Functia select primeste ca parametri:
        - baza de date
        - instructiunea select
    si returneaza result set-ul corespunzator''' #
    import pymysql as mydb
    connect = mydb.connect(passwd='paul', user='root', host='localhost', port=3306)
    cursor = connect.cursor()
    cursor.execute('Use ' + baza_de_date)
    cursor.execute(select_var)
    result = cursor.fetchall()
    cursor.close()
    return result

def delete(baza_de_date, delete_var):
    '''Functia delete primeste ca parametri:
        - baza de date
        - instructiunea deleet
    si sterge...''' #
    import pymysql as mydb
    connect = mydb.connect(passwd = 'paul', user='root', host='localhost', port=3306)
    cursor = connect.cursor()
    cursor.execute('Use ' + baza_de_date)
    cursor.execute(delete_var)
    connect.commit()
    cursor.close()

def insert(baza_de_date, insert_var):
    '''Functia delete primeste ca parametri:
        - baza de date
        - instructiunea insert
    ...''' #
    import pymysql as mydb
    connect = mydb.connect(passwd='paul', user='root', host='localhost', port=3306)
    cursor = connect.cursor()
    cursor.execute('Use ' + baza_de_date)
    cursor.execute(insert_var)
    connect.commit()
    cursor.close()

def update(baza_de_date, update_var):
    '''Functia delete primeste ca parametri:
        - baza de date
        - instructiunea insert
    ...''' #
    import pymysql as mydb
    connect = mydb.connect(passwd='paul', user='root', host='localhost', port=3306)
    cursor = connect.cursor()
    cursor.execute('Use ' + baza_de_date)
    cursor.execute(update_var)
    connect.commit()
    cursor.close()


select('world', 'describe world.country')

lista_coloane = []
for i in select('world', 'describe country.field'):
    lista_coloane += [i[0]]
print(lista_coloane)    # extrage numele coloanelor pentru tabela noastra

select('world', "select column_name from information_schema.COLUMNS where TABLE_NAME = 'country'\
        AND table_schema = 'world'")    # extrage numele coloanelor pentru tabela noastra
select('world', 'select * from country where code = "rom"')

select('world', "select column_name from information_schema.COLUMNS where TABLE_NAME = 'country'\
    AND table_schema = 'world' \
    UNION \
    select * from country where code = 'rom'")

select('world', 'select * from autor' )

delete('world', 'delete from autor where id = 4')

insert('world', 'insert into autor(name) values("Tudor Arghezi")')

update('world', 'update autor set id = 4  where name = "Tudor Arghezi"')

