
import sqlite3

# Creare BD, tabele

conn = sqlite3.connect('test.db')
print ("Opened database successfully")

conn.execute('DROP TABLE IF EXISTS COMPANY')

conn.execute('''CREATE TABLE COMPANY
       (ID            INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')
print ("Table created successfully")

conn.close()


# Insert

conn = sqlite3.connect('test.db')
print ("Opened database successfully")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")

conn.commit()
print ("Records created successfully")
conn.close()

'''
cursor.execute(\'''INSERT INTO users(name, phone, email, password)
                  VALUES(:name,:phone, :email, :password)\''',
                  {'name':name1, 'phone':phone1, 'email':email1, 'password':password1})


users = [(name1,phone1, email1, password1),
         (name2,phone2, email2, password2),
         (name3,phone3, email3, password3)]
cursor.executemany(\''' INSERT INTO users(name, phone, email, password) VALUES(?,?,?,?)\''', users)


id = cursor.lastrowid
print('Last row id: %d' % id)


# Never do this -- insecure!
symbol = 'RHAT'
c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)

'''


# Select

conn = sqlite3.connect('test.db')
print ("Opened database successfully")

cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")

for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")

print ("Operation done successfully")

conn.close()


# Update

conn = sqlite3.connect('c:/wt/test.db')
print ("Opened database successfully")

conn.execute('UNLOOK TABLE COMPANY')
conn.execute("UPDATE COMPANY set SALARY = 25147.00 where ID=1;")
conn.commit
print ("Total number of rows updated :", conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")

print ("Operation done successfully")

conn.close()

'''
cursor.execute(\'''UPDATE users SET phone = ? WHERE id = ? \''', (newphone, userid))
'''


# Delete

conn = sqlite3.connect('test.db')
print ("Opened database successfully")

conn.execute("DELETE from COMPANY where ID=2;")
conn.commit
print ("Total number of rows deleted :", conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")

print ("Operation done successfully")

conn.close()



