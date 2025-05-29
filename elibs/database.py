import sqlite3
con = sqlite3.connect("elibs.db")
cursor = con.cursor()
# cursor.execute("CREATE TABLE book(name, qty)")


cursor.execute("CREATE TABLE books(title TEXT  PRIMARY KEY NOT NULL,qty INT NOT NULL )")