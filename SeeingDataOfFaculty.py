import sqlite3
conn = sqlite3.connect("results.db")
db = conn.cursor()

db.execute("SELECT * FROM ryerson_faculty;")
print(db.fetchall())

conn.commit()
conn.close()