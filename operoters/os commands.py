#TO CREATE A SINGLE FOLDER

import os

print(os.getcwd())
print(os.listdir())
l=os.listdir()
for a in range(len(l)):
    print(l[a])

os.chdir(r'C:\Users\Dell\Desktop')
print(os.getcwd())
print(os.listdir())
l1=os.listdir()
for a in range(len(l1)):
    print(l1[a])

foldername=input("enter the folder name")
os.mkdir(foldername)
print(os.mkdir())


#TO CREATE A MULTIPLE FOLDER

print(os.getcwd())
print(os.listdir())
os.chdir(r'C:\Users\Dell\Desktop')
y=['2001','2002','2003','2004']
for a in range(len(y)):
    foldername=y[a]
    os.mkdir(foldername)
print(os.listdir())



# TO CREATE A FOLDER IN MULTIPLE FOLDER

import os
print(os.getcwd())
print(os.listdir())
os.chdir(r'C:\Users\Dell\Desktop')
c=os.getcwd()
y = ['1990', '1991', '1992', '1993', '1994', '1995']
for a in range(len(y)):
    foldername = y[a]
    os.mkdir(foldername)
    p=f"{c}\{foldername}"
    print(p)
    os.chdir(p)
    for i in range(1,13):
        os.mkdir(str(i))
    os.chdir(c)
print(os.listdir())


# TO CHECK A FILE AND FOLDER

import os.path
fileexit=os.path.isfile(r'C:\Users\Dell\Desktop\')
print(fileexit)
foldername=os.path.isdir(r'C:\Users\Dell\Desktop\')
print(foldername)



#TO REMOVE A FILE (OR) FOLDER

os.rmdir(r'C:\Users\Dell\Desktop\1990\1')
print(c)



