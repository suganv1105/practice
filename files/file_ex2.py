import re

f=open(r'F:\PycharmProjects\practice\name_1.txt','r')
t=f.read()
f.close()
a1=input("change this")
a2=input("To change this")
# o=re.sub(a1,a2,t)
o=re.sub('hhhhhhh','to',t)
f=open(r'F:\PycharmProjects\practice\name_1.txt','w')
f.writelines(o)
f=print(o)


