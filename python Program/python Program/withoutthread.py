sq=[]
cu=[]
def square(Threadname,endpoint,delay):
    for i in range(1,endpoint+1):
        sq.append(i*i)
        print("Tread name was=",Threadname,"and sq value is =",sq)

def cube(Threadname,endpoint,delay):
    for i in range(1,endpoint+1):
        cu.append(i**i)
        print("Tread name was=",Threadname,"and cu value is =",cu)


square("thread1",10,2)
print("---------------------------------------------")
cube("thread2",10,2)

