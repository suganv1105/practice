from tkinter import *
root=Tk()
root.title('checkbutton')
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

def savd():
    iv=ivd.get()
    cvv=cv.get()
    cp=cv1.get()
    jv=cv2.get()
    pv=cv3.get()
    strv=""
    l=[]
    if cvv==1:
        l.append("C")
    if cp==1:
        l.append("C++")
    if jv==1:
        l.append("Java")
    if pv==1:
        l.append("Python")
    for i in range(len(l)):
        if i==0:
            v=""
            v=l[i]
            strv+=v
        else:
            v=","
            v=v+l[i]
            strv+=v
    print(strv)
    root.destroy()



Label(root,text='Student ID : ').grid(row=0,column=0)
Entry(root,textvariable=id).grid(row=0,column=1)

Radiobutton(root,text="INDIA",variable=var,value=1,command=sel).grid(row=1,column=0)
Radiobutton(root,text="CHENNAI",variable=var,value=2,command=sel).grid(row=1,column=1)
Radiobutton(root,text="SALEM",variable=var,value=3,command=sel).grid(row=1,column=2)
Radiobutton(root,text="KARNATKA",variable=var,value=4,command=sel).grid(row=1,column=3)
Label(root,text='Interested in : ').grid(row=2,column=0)
Checkbutton(root,text="C",variable= cv).grid(row=3,column=0)
Checkbutton(root,text="C++",variable= cv1).grid(row=3,column=1)
Checkbutton(root,text="Java",variable = cv2).grid(row=3,column=2)
Checkbutton(root,text="Python",variable = cv3).grid(row=3,column=3)
Button(root,text="submit",command=savd).grid(row=4,column=1)
root.mainloop()