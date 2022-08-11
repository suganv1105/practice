import _thread
import time

sq=[]
cu=[]

def square(Threadname,endpoint,delay):
    for i in range(1,endpoint+1):
        sq.append(i*i)
        print("Tread name was=",Threadname,"and sq value is =",sq)
        time.sleep(delay)

def cube(Threadname,endpoint,delay):
    for i in range(1,endpoint+1):
        cu.append(i**i)
        print("Tread name was=",Threadname,"and cu value is =",cu)
        time.sleep(delay)

try:
    # thread syntax(_thread.start_new_thread)
    _thread.start_new_thread(square,("thread-1",5,1))
    _thread.start_new_thread(square, ("thread-2",6,1))
    _thread.start_new_thread(square, ("thread-3",7,1))
    _thread.start_new_thread(cube, ("thread-4",8,1))
    _thread.start_new_thread(cube, ("thread-5",10,1))

except:
    print("Error:enable start to thread")


while 1:
    pass