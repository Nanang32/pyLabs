import sqlite3
con = sqlite3.connect("elibs.db")
cursor = con.cursor()

#delete data
cursor.execute("DELETE FROM books WHERE id=1")
con.commit()