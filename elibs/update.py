import sqlite3
con = sqlite3.connect("elibs.db")
cursor = con.cursor()

# cursor.execute("UPDATE book SET qty = 25 WHERE rowid=1")
cursor.execute("UPDATE books set qty = 25 where title = 1")

# UPDATE bank_accs SET amount = ? WHERE rowid = 1
# DELETE FROM book WHERE ROWID=2

# Commit your changes in the database
con.commit()

# # Closing the connection
# con.close()