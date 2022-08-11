from tkinter import *
import os.path
import csv
fileexit=os.path.isfile('output123.csv')
print(fileexit)
root=Tk()
root.title('STUDENT DETAILS')
root.geometry('400x400')
var=IntVar()
cv= IntVar()
cv1= IntVar()
cv2= IntVar()
cv3= IntVar()
ivd=IntVar()
ivd.set("")

def sel():
    selection=str(var.get())
    print(selection)

def s():
    print([NAMEv.get(), Locationv.get(), Salaryv.get(), departmentv.get(),var.get()])
    cvv = cv.get()
    cp = cv1.get()
    jv = cv2.get()
    pv = cv3.get()
    strv = ""-
    l = []
    if cvv == 1:
        l.append("C")
    if cp == 1:
        l.append("C++")
    if jv == 1:
        l.append("Java")
    if pv == 1:
        l.append("Python")
    for i in range(len(l)):
        if i == 0:
            v = ""
            v = l[i]
            strv += v
        else:
            v = ","
            v = v + l[i]
            strv += v
    print(strv)
    if fileexit:
        with open('output12345.csv', 'w') as file:
            w = csv.writer(file)
            w.writerow([NAMEv.get(), Locationv.get(), Salaryv.get(), departmentv.get(),var.get(),strv])
    else:
        with open('output12345.csv', 'w') as file:
            w = csv.writer(file)
            w.writerow(['name', 'Location', 'Salary','department'])
            w.writerow([NAMEv.get(), Locationv.get(), Salaryv.get(), departmentv.get(),var.get(),strv])
    root.destroy()

Label(root,text='NAME').grid(row=0,column=0)
NAMEv=StringVar()
Entry(root,textvariable=NAMEv).grid(row=0,column=1)

Label(root,text='LOCATION').grid(row=1,column=0)
Locationv=StringVar()
Entry(root,textvariable=Locationv).grid(row=1,column=1)

Label(root,text='SALARY').grid(row=2,column=0)
Salaryv=StringVar()
Entry(root,textvariable=Salaryv).grid(row=2,column=1)

Label(root,text='DEPARTMENT').grid(row=3,column=0)
departmentv=StringVar()
Entry(root,textvariable=departmentv).grid(row=3,column=1)

Label(root,text='STUDENT ID : ').grid(row=5,column=0)
Entry(root,textvariable=ivd).grid(row=5,column=1)

Radiobutton(root,text="INDIA",variable=var,value=1,command=sel).grid(row=7,column=0)
Radiobutton(root,text="USA",variable=var,value=2,command=sel).grid(row=7,column=1)
Radiobutton(root,text="US",variable=var,value=3,command=sel).grid(row=7,column=2)
Radiobutton(root,text="UKRAINE",variable=var,value=4,command=sel).grid(row=7,column=3)
Label(root,text='INTERESTED IN : ').grid(row=8,column=0)

Checkbutton(root,text="C",variable= cv).grid(row=9,column=0)
Checkbutton(root,text="C++",variable= cv1).grid(row=9,column=1)
Checkbutton(root,text="Java",variable = cv2).grid(row=9,column=2)
Checkbutton(root,text="Python",variable = cv3).grid(row=9,column=3)

Button(root,text='SUBMIT',command=s).grid(row=10,column=1)

root.mainloop()








