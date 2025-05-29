import sqlite3
con = sqlite3.connect("elibs.db")
cursor = con.cursor()

cursor.execute("SELECT * FROM books")
for row in cursor.fetchall():
    print(row)

con.close()