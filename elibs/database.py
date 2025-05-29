import sqlite3
con = sqlite3.connect("elibs.db")
cursor = con.cursor()
# cursor.execute("CREATE TABLE book(name, qty)")


cursor.execute("CREATE TABLE books(id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT  NOT NULL,qty INTEGER NOT NULL )")

con.commit()
con.close()