import sqlite3

conn=sqlite3.connect('student.db')
cur=conn.cursor()
cur.execute("create table Passtable (Id int, NAME Text, M1 int, M2 int, M3 int)")
cur.execute("create table Failtable (Id int, NAME Text, M1 int, M2 int, M3 int)")
print("table created successfully")
conn.commit()
cur.close()