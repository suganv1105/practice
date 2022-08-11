'''
x=lambda x1:x1+5
print(x(10))
n=int(input("enter the number"))
print(x(n))
add=lambda a,b :a+b
print(add(27,51))

n1=int(input("enter the number"))
n2=int(input("enter the number"))
print(add(n1,n2))


x1=lambda x,y=5:x*y
print(x1(5,10))
print(x1(5)

l1=[1,2,3,4,5,6,7,8,]
x=lambda x:x**x
for b in range(0,len(l1)):
    print(x(l1[b]),end=" ,")

first_name=['sandy','latha','pradeepa']
last_name=['k','k','e']
print(first_name)
print(last_name)
x=lambda x,y:x+'-'+y
for a in range(0,len(first_name)):
     print(x(first_name[a],last_name[a]))

l1=[1,2,3,4,5,6,7,8,9]
print(l1)
print(l1[:])
print(l1[2:4])
print(l1[1:5])
l1.pop(3)
print(l1)
l1.append(11)
print(l1)
l1.sort()
print(l1)
l1.sort(reverse=1)
print(l1)

l1=[1,2,3,4,5,]
for i in range (1,5):
    l1.append(i)
    print(l1)
n=int(input("enter the no to ad"))
l2=[]
for i in range(1,n+1):
    l2.append(i)
print(l2)

l1=[1,2,3]
l2=[4,5,6]
l1.extend(l2)
print(l1)

l=[]
for a in range(1,5):
    l.append(a**a)
    print(l)

   n1=int(input("enter the number i"))

      if(n1<0):
          l1.append(n1)
          nsum+=n1
      else:
          l2.append(n1)
          psum+=n1
print(l1)
print(l2)
print(nsum)
print(psum)

'''
l1=[ ]
l2=[ ]
n= int(input("enter the number"))
for i in range(1,n+1):
    n1=int(input("enter the numberi"))
    if(n1%2)==0:
        l1.append(n1)
        print('even')
    else:
        l2.append(n1)
        print('odd')
print(l1)
print(l2)





















