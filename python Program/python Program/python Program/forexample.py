'''
a=int(input("enter the value"))
if(a>10):
    print('a value is=',a,'enter')
else:
    print('a is less than')


b=int(input("enter the value"))
if((b%2)==0):
    print('even number and user  enter is',b)
else:
    print('odd number and user enter is',b)

c=int(input("enter the value"))
if(a>=18):
    print('vote')
else:
    print('no vote')
    b=18-c
    print('you must need to wait ',b,'year')
n=int(input('enter the no of person')):
for i in range(1,n+1):

    a = int(input("enter the value"))
    if (a > 10):
        print('a value is=', a, 'enter')
    else:
        print('a is less than')

'''
'''
a=10
b=5
c=2
if((a>b)and(a>c)):
    print('a is greater')
elif((b>a)and(b>c)):
    print('b is greater')
else:
    print('c is greater')
print('------------------')

for i in range(1,3):
    print('------------------')
    a = int(input('enter the value'))
    b = int(input('enter the value'))
    c = int(input('enter the value'))
    if ((a > b) and (a > c)):
        print('a is greater')
    elif ((b > a) and (b > c)):
        print('b is greater')
    else:
        print('c is greater')
'''
'''
a=int(input("enter the number"))
b=int(input("enter the number"))
print(a+b)
'''
a=int(input('enter the age'))
country=input("enter the country")
if(country=="us"):
    print("us")

    if (a >= 18):
            print('vote')
    else:
            print('no vote')
elif(country=="india"):
    print("india")
    if (a >= 18):
            print('vote')
    else:
            print('no vote')
elif(country=="pakistan"):
    print("pakistan")
    if(a>=18):
        print('vote')
    else:
        print('no vote')
else:
    print("invalid country")
    if (a >= 18):
        print('vote')
    else:
        print('no vote')


