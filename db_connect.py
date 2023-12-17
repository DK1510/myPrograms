import sqlite3
connection = sqlite3.connect(r'C:\Users\dines\Downloads\Ex_Files_SQL_EssT\Ex_Files_SQL_EssT\Exercise Files\db\world.db')
c = connection.cursor() #midware
l = list(c.execute('SELECT DISTINCT CountryCode FROM city;'))
print(l)
print(l[0][0])
for CC in l:
    print(CC[0])
    q = 'DROP TABLE IF EXISTS "'+CC[0]+'";'
    c.execute(q)
    q = 'CREATE TABLE IF NOT EXISTS "'+CC[0]+'" (ID INTEGER PRIMARY KEY,name TEXT,District TEXT,Population INTEGER);'
    c.execute(q)
    q = 'SELECT ID,Name,District,Population FROM City WHERE CountryCode="'+CC[0]+'";'
    print(q)
    records = list(c.execute(q))
    for record in records:
        q = 'INSERT INTO "'+CC[0]+'" (ID,Name,District,Population) VALUES '+str(record)+';'
        c.execute(q)
        print(q)

    #print(records)
connection.commit()
connection.close()








































# c.execute('CREATE TABLE IF NOT EXISTS emp (ID INTEGER PRIMARY KEY NOT NULL,name TEXT,salary INTEGER DEFAULT 5000);')
# c.execute('INSERT INTO emp VALUES(100,"kumar",10000);')
# c.execute('INSERT INTO emp VALUES(101,"sam",10000);')
# c.execute('INSERT INTO emp VALUES(102,"dinesh",9000);')