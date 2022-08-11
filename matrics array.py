import numpy as np
m1=[]
m2=[]
tm1=[]
tm2=[]
for a in range(0,3):
    tm1=[]
    for b in range(0,3):
        c=int(input(f"enter the row{a}and column{b}"))
        tm1.append(c)
    m1.append(tm1)

for a in range(0,3):
    tm2=[]
    for b in range(0,3):
        c=int(input(f"enter the row{a}and column{b}"))
        tm2.append(c)
    m2.append(tm2)
print(m1)
print(m2)
a=np.array(m1)
b=np.array(m2)
print(a+b)