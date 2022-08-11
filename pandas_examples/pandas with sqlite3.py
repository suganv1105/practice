import pandas as pd
import sqlite3
conn=sqlite3.connect(r'C:\sqlite3\pandasexample.db')
sql="select * from student"
ta=pd.read_sql(sql,conn)
df=pd.DataFrame(ta)
print(df)

df['total']=df['m1']+df['m2']+df['m3']+df['m4']+df['m5']
df['avg']=df['total']|5
print(df.tail(2))
print(df)