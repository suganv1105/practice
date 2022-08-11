import _thread
import time
import datetime

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print(threadName,datetime.datetime.now())

# Create two threads as follows
try:
   _thread.start_new_thread( print_time, ("Thread-1", 1, ) )
   _thread.start_new_thread( print_time, ("Thread-2", 1, ) )
except:
   print("Error: unable to start thread")

while 1:
   pass