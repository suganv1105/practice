from tkinter import *
import  sqlite3
root = Tk()
root.title('Student')
root.geometry('200x200')

conn= sqlite3.connect(r'C:\sqlite3\training.db')
cur=conn.cursor()

def s():
    print(IDv.get(),NAMEv.get(),M1v.get(),M2v.get(),M3v.get())
    sql = f"insert into student values ({IDv.get()},'{NAMEv.get()}',{M1v.get()},{M2v.get()},{M3v.get()})"

    cur.execute(sql)
    cur.close()
    conn.commit()
    root.destroy()

Label(root,text='ID').grid(row=0,column=0)
IDv=IntVar()
IDv.set('')
Entry(root,textvariable=IDv).grid(row=0,column=1)

Label(root,text='NAME').grid(row=1,column=0)
NAMEv=StringVar()
Entry(root,textvariable=NAMEv).grid(row=1,column=1)

Label(root,text='M1').grid(row=2,column=0)
M1v=IntVar()
M1v.set('')
Entry(root,textvariable=M1v).grid(row=2,column=1)

Label(root,text='M2').grid(row=3,column=0)
M2v=IntVar()
M2v.set('')
Entry(root,textvariable=M2v).grid(row=3,column=1)

Label(root,text='M3').grid(row=4,column=0)
M3v=IntVar()
M3v.set('')
Entry(root,textvariable=M3v).grid(row=4,column=1)

Button(root,text='SUBMIT',command=s).grid(row=5,column=1)


root.mainloop()

