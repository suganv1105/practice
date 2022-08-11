import sqlite3
from tkinter import *
con=sqlite3.connect(r'student.db')
cur=con.cursor()
root = Tk()
root.title('STUDENT FORM')
root.geometry('400x400')


def S():
    print([IDv.get(), NAMEv.get(), M1v.get(),M2v.get(),M3v.get()])
    if M1v.get() >= 35 and M2v.get() >= 35 and M3v.get() >= 35:
            sql = f"insert into Passtable ({IDv.get()},'{NAMEv.get()}',{M1v.get()},{M2v.get()},{M3v.get()})"
            print(sql)
            cur.execute(sql)
            cur.close()
            conn.commit()

    else:
            sql = f"insert into Failtable ({IDv.get()},'{NAMEv.get()}',{M1v.get()},{M2v.get()},{M3v.get()})"
            print(sql)
            cur.execute(sql)
            cur.close()
            conn.commit()

    root.destroy()

Label(root, text="ID").grid(row=0, column=0)
IDv = IntVar()
IDv.set('')
Entry(root, textvariable=IDv).grid(row=0, column=1)

Label(root,text='NAME').grid(row=1,column=0)
NAMEv=StringVar()
Entry(root,textvariable=NAMEv).grid(row=1,column=1)

Label(root, text="M1").grid(row=2, column=0)
M1v = IntVar()
M1v.set('')
Entry(root, textvariable=M1v).grid(row=2, column=1)

Label(root, text="M2").grid(row=3, column=0)
M2v = IntVar()
M2v.set('')
Entry(root, textvariable=M2v).grid(row=3, column=1)

Label(root, text="M3").grid(row=4, column=0)
M3v = IntVar()
M3v.set('')
Entry(root, textvariable=M3v).grid(row=4, column=1)

Button(root,text='SUBMIT',command=S).grid(row=5,column=1)


root.mainloop()
