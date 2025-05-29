import sqlite3
con = sqlite3.connect("elibs.db")
cursor = con.cursor()

cursor.execute("""
    INSERT INTO books VALUES
        ('pengantar pascal',5),
        ('Cisco advances',2)
        
""")

con.commit()