import sqlite3
con = sqlite3.connect("elibs.db")
cursor = con.cursor()

# cursor.execute("UPDATE book SET qty = 25 WHERE rowid=1")
# cursor.execute("UPDATE books SET qty = 25,WHERE title = Cisco advances ")




cursor.execute("""
    UPDATE books
    SET qty = ?
    WHERE id = ?;
""", (1, 1))



# Commit your changes in the database
con.commit()

# # Closing the connection
con.close()