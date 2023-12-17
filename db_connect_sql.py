import sqlite3
db = sqlite3.connect('test100.db')
c= db.cursor()
c.execute('CREATE TABLE school (name TEXT, age INTEGER);')
c.execute('INSERT INTO school (name,age) VALUES ("bala",19)')
db.commit()
db.close()