# !/usr/bin/python3
from tkinter import *
#creating the application main window.
top = Tk()
#Entering the event main loop
top.mainloop()

# python application to create a simple button

from tkinter import *
top = Tk()
top.geometry("250x100")
b = Button(top, text="Simplebutton")
b.pack()
top.mainloop()

from tkinter import *
from tkinter import messagebox
top = Tk()
top.geometry("200x100")
def redfun():
    messagebox.showinfo("Hello", "Red Button clicked")
def bluefun():
    messagebox.showinfo("Hello", "blue Button clicked")
def greenfun():
    messagebox.showinfo("Hello", "Green Button clicked")
def yellowfun():
    messagebox.showinfo("Hello", "Yellow Button clicked")

b1 = Button(top, text="Red", command=redfun, activeforeground="red", activebackground="pink", pady=10)
b2 = Button(top, text="Blue", command=bluefun,activeforeground="blue", activebackground="pink", pady=10)
b3 = Button(top, text="Green", command=greenfun,activeforeground="green", activebackground="pink", pady=10)
b4 = Button(top, text="Yellow", command=yellowfun,activeforeground="yellow", activebackground="pink", pady=10)
b1.pack(side=LEFT)
b2.pack(side=RIGHT)
b3.pack(side=TOP)
b4.pack(side=BOTTOM)
top.mainloop()

from tkinter import *
top = Tk()
top.geometry("200x200")
# creating a simple canvas
c = Canvas(top, bg="pink", height="200")
c.pack()
top.mainloop()

from tkinter import *
top = Tk()
top.geometry("200x200")
# creating a simple canvas
c = Canvas(top, bg="pink", height="200", width=200)
arc = c.create_arc((5, 10, 150, 200), start=0, extent=150, fill="white")
c.pack()
top.mainloop()

from tkinter import *
top = Tk()
top.geometry("200x200")
checkvar1 = IntVar()
checkvar2 = IntVar()
checkvar3 = IntVar()
chkbtn1 = Checkbutton(top, text="POSTGRES", variable=checkvar1, onvalue=1, offvalue=0, height=2, width=10)
chkbtn2 = Checkbutton(top, text="MONGODB", variable=checkvar2, onvalue=1, offvalue=0, height=2, width=10)
chkbtn3 = Checkbutton(top, text="SQLLITE", variable=checkvar3, onvalue=1, offvalue=0, height=2, width=10)
chkbtn1.pack()
chkbtn2.pack()
chkbtn3.pack()
top.mainloop()

from tkinter import *
top = Tk()
top.geometry("400x250")
name = Label(top, text="Name").place(x=30, y=50)
email = Label(top, text="Email").place(x=30, y=90)
password = Label(top, text="Password").place(x=30, y=130)
sbmitbtn = Button(top, text="Submit", activebackground="pink", activeforeground="blue").place(x=30, y=170)
e1 = Entry(top).place(x=80, y=50)
e2 = Entry(top).place(x=80, y=90)
e3 = Entry(top).place(x=95, y=130)
top.mainloop()

import tkinter as tk
from functools import partial
def call_result(label_result, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1) + int(num2)
    label_result.config(text="Result = %d" % result)
    return
root = tk.Tk()
root.geometry('400x200+100+200')
root.title('Calculator')
number1 = tk.StringVar()
number2 = tk.StringVar()
labelNum1 = tk.Label(root, text="A").grid(row=1, column=0)
labelNum2 = tk.Label(root, text="B").grid(row=2, column=0)
labelResult = tk.Label(root)
labelResult.grid(row=7, column=2)
entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)
entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)
call_result = partial(call_result, labelResult, number1, number2)
buttonCal = tk.Button(root, text="Calculate", command=call_result).grid(row=3, column=0)
root.mainloop()

from tkinter import *

top = Tk()
top.geometry("140x100")
frame = Frame(top)
frame.pack()
leftframe = Frame(top)
leftframe.pack(side=LEFT)
rightframe = Frame(top)
rightframe.pack(side=RIGHT)
btn1 = Button(frame, text="Submit", fg="red", activebackground="red")
btn1.pack(side=LEFT)
btn2 = Button(frame, text="Remove", fg="brown", activebackground="brown")
btn2.pack(side=RIGHT)
btn3 = Button(rightframe, text="Add", fg="blue", activebackground="blue")
btn3.pack(side=LEFT)
btn4 = Button(leftframe, text="Modify", fg="black", activebackground="white")
btn4.pack(side=RIGHT)
top.mainloop()

from tkinter import *
top = Tk()
top.geometry("400x250")
# creating label
uname = Label(top, text="Username").place(x=30, y=50)
# creating label
password = Label(top, text="Password").place(x=30, y=90)
sbmitbtn = Button(top, text="Submit", activebackground="pink", activeforeground="blue").place(x=30, y=120)
e1 = Entry(top, width=20).place(x=100, y=50)
e2 = Entry(top, width=20).place(x=100, y=90)
top.mainloop()