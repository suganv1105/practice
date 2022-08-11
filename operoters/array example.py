# import numpy as np

# l=[1,2,3,4,5]
# print(type(l))
# print(l)
# l1=[[1,2,3],[4,5,6],[7,8,9]]
# print(l1)
# print(type(l1))
# l2=[[[1,2,3,4,5,6,],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24,],[25,26,27,28,29,30],[31,32,33,34,35,36,]]]
# print(l2)
# print(type(l2))
#
# a=np.array(l)
# print(type(a))
# print(a)
# b=np.array(l1)
# print(type(b))
# print(b)
# c=np.array(l2)
# print(type(c))
# print(c)
#
# a=[1,2,3,4,5]
# o=[]
# for b in range(len(a)):
#     o.append(a[b]+2)
# print(o)
#
# a1=np.array(a)
# print(a1*2)

# l1=[[1,14,16],[18,20,22],[17,19,18]]
# o=[]
# print(len(l1))
# for a in range(len(l1)):
#     tmp=[]
#     for b in range(len(l1[a])):
#         tmp.append(l1[a][b]+2)
#     o.append(tmp)
# print(o)
#
# l2=np.array(l1)
# print(l2+2)


import numpy as np

m=[]
n=[]

for a in range (0,3):
    t=[]
    for b in range(0,3):
        t1 = []
        for a in range(0, 3):
            v = int(input("enter the number"))
            t1.append(v)
            t.append(t1)
    m.append(t)

for a in range (0,3):
    t=[]
    for b in range (0,3):
        t1=[]
        for a in range(0,3):
            v =int(input("enter the number"))
            t1.append(v)
            t.append(t1)
    n.append(t)

print(m)
print(n)

a=np.array(m)
b=np.array(n)

print(a+b)
