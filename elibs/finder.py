import sqlite3
con = sqlite3.connect("elibs.db")
cursor = con.cursor()


# cur.execute("SELECT * FROM list WHERE InstitutionName=?", (Variable,))
# cursor.execute("SELECT * FROM books")

name_to_search = "pascal"
cursor.execute("SELECT * FROM books WHERE title = ?", (name_to_search,))
results = cursor.fetchall()

for row in results:
    print(row)



con.close()