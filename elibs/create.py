import sqlite3
con = sqlite3.connect("elibs.db")
cursor = con.cursor()



cursor.execute("INSERT INTO books (title, qty) VALUES (?, ?)", ("Fisika", 21))

con.commit()