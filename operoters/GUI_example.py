from tkinter import *
root = Tk()
root.title('GUI Calculator')
root.geometry('400x400')


def calc():
    n1 = num1v.get()
    n2 = num2v.get()
    op = operationv.get()
    if op == '+':
        print(n1+n2)
    elif op == '-':
        print(n1-n2)
    elif op == '*':
        print(n1*n2)
    elif op == '/':
        print(n1/n2)
    else:
        print('not available')


Label(root, text="num1").grid(row=0, column=0)
num1v = IntVar()
num1v.set('')
Entry(root, textvariable=num1v).grid(row=0, column=1)
Label(root, text="num2").grid(row=1, column=0)
num2v = IntVar()
num2v.set('')
Entry(root, textvariable=num2v).grid(row=1, column=1)
Label(root, text="operation").grid(row=2, column=0)
operationv = StringVar()
Entry(root, textvariable=operationv).grid(row=2, column=1)
Button(root, text="submit", command=calc).grid(row=3, column=1)

root.mainloop()