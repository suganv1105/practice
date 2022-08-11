from tkinter import *
import sqlite3
def login():
    usernamevalue=sandy.get()
    passwordvalue=pradeepa.get()
    conn=sqlite3.connect('pythongui/login.db')
    cur=conn.cursor()
    cur.execute('insert into officelogin values(?,?)',[usernamevalue,passwordvalue])
    print(usernamevalue,passwordvalue)
    conn.commit()
    cur.close()

formtk=Tk()
formtk.geometry('600x200')
formtk.title('latha')
sandy=StringVar()
pradeepa=StringVar()
Label(formtk,text="username").grid(row=0,column=1)
Entry(formtk,textvariable=sandy).grid(row=0,column=2)
Label(formtk,text="password").grid(row=1,column=1)
Entry(formtk,textvariable=pradeepa).grid(row=1,column=2)
Button(formtk,text="submit",command=login).grid(row=3,column=2)
Checkbutton(formtk,text="some").grid(row=2,column=1)
formtk.mainloop()