# for i in range (7):
#     a= i+1
#     b=7-1
#     for j in range(i+1):
#         print(a,end=" ")
#         a=a+b
#         b=b-1
#
#     print()



a=list(range(1,11))
print(a)



a=[[2,3]]*2
a=[1][0]=3
print(a)

a=0
for i in range(4,8):
   if i%2==0:
     a=a+i
print(a)

list=["sugan","monisha"]
print("-".join(list))

set1={"red","blue","green",}
set2={"blue","orange","black"}
set3=set2.difference(set1)
print(set3)


a=[1,2,3,4,5]
print(a.pop(0))
print(a.pop(2))


a=10
b=10
print(a+b)
