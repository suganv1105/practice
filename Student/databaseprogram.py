import sqlite3

conn=sqlite3.connect('std.db')
cur=conn.cursor()
cur.execute("create table StudentDetails (Id int, Name Text, M1 int, M2 int, M3 int,Total int,Average float )")
print("table created successfully")
conn.commit()
cur.close()



