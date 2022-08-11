for i in range(10):
    print(i)
print('------')

for i in range(1,10,3):
    print(i)
print('------')

for i in range(1,10):
    print(i)
for j in range(1,10):
    print(j,end=" ")
print()
for k in range(1,10):
    print(k,end="class")



L=['a','e','i']
print(len(L))
for c in range(len(L)):
    print(L[c])
print(L[0])
print(L[1])
print(L[2])
L=['d','1','2','a']
print(len(L))
for i in range(0,len(L)):
    print(i)
    print(L[i])
for i in range(1,5):
    for j in range(1,i+1):
        print('*',end=" ")
    print()
        
n=int(input("enter the number"))
sum=0
for i in range(1,n+1):
    m=int(input("enter the number"))
    sum+=m
    print(sum)
print(sum)
for k in range(1,10):
    for y in range(1,10):
        print(k*y,end=" ")
    print()
num=1
for i in range(1,5):
    for j in range(1,i+1):
        print(num,end=" ")
        num+=1
    print()
sum=0
n=int(input("enter the number to add"))
for a in range(1,n+1):
    n1=int(input("enter the number"))
    sum=sum+n1
    print(sum)
print(sum)
for i in range(1,11):
    for j in range(1,11):
        print(i,'*',j,'=',i*j)
    print('----------')

