import sqlite3

conn=sqlite3.connect('mathop.db')
cur=conn.cursor()
cur.execute("create table if not exists addition(num1 int, num2 int, result text)")
cur.execute("create table if not exists sub(num1 int, num2 int, result text)")
cur.execute("create table if not exists mul(num1 int, num2 int, result text)")
cur.execute("create table if not exists div(num1 int, num2 int, result text)")
conn.commit()
cur.close()
