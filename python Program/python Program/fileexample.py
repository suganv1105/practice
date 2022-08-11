import os

print(os.getcwd())
print(' ')
print(os.listdir())

f_open = open("PythonSample.txt", "r")
print(f_open.read())

f_open = open("PythonSample.txt", "r")
print(f_open.read(5))
print(f_open.read(2))

f_open = open("PythonSample.txt", "r")
for char in f_open:
    print(char)
f_sample = open("PythonSample.txt", "r")
print(f_sample.readline())

f_sample = open("PythonSample.txt", "r")
print(f_sample.readline())
print(f_sample.readline())
print(f_sample.readline())

f_sample = open("PythonSample.txt", "r")
print(f_sample.readlines())
f_sample = open("PythonSample.txt", "r")
print(f_sample.readline())

f_sample.close()
f_demo = open("PythonSample.txt", "w")
f_demo. write("Welcome to Tutorial python")
f_demo.close()

f_demo = open("PythonSample.txt", "r")
print(f_demo.read())
f_writedemo = open("PythonSample.txt", "w")
f_writedemo. write("Python")
f_writedemo. write("\nTutorial programs")
f_writedemo. write("\nHappy Coding!")
f_writedemo. write("\nHi \nHello \nCheers")
f_writedemo.close()

f_writedemo = open("PythonSample.txt", "r")
print(f_writedemo.read())

f_writelinesdemo = open("PythonSample.txt", "w")
text = ["First Line\n", "Second Line\n", "Third Line\n", "Fourth Line"]
f_writelinesdemo. writelines(text)
f_writelinesdemo.close()

f_writelinesdemo = open("PythonSample.txt", "r")
print(f_writelinesdemo.read())

f_demo = open("PythonSample.txt", "a")
f_demo. write("\nHell World!")
f_demo.close()

f_demo = open("PythonSample.txt", "r")
print(f_demo.read())

f_loopdemo = open("Sample10.txt", "w")

for i in range(1, 11):
    f_loopdemo.write("This is the %d Line\n" %(i))
f_loopdemo.close()

f_loopdemo = open("Sample10.txt", "r")
print(f_loopdemo.read())

f_create = open("Sample101.txt", "x")
f_create = open("Sample102.txt", "x")
f_create.write("Python Program")
f_create.close()

f_create = open("Sample102.txt", "r")
print(f_create.read())

os.rename("Sample102.txt", "NewSample.txt")
os.remove("Sample101.txt")

