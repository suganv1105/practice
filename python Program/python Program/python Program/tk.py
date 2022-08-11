from future.moves import tkinter
top = tkinter.Tk()
# Code to add widgets will go here...
top.mainloop()

print('---------------------')

from future.moves import tkinter
from future.moves import tkMessageBox
top = tkinter.Tk()

def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")

B = tkinter.Button(top, text ="Hello", command = helloCallBack)

B.pack()
top.mainloop()