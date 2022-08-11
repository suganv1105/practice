f=open('t.txt','w')
L=['hi\n','i am\n','from chennai\n']
f.write('hi welcome\n')
f.writelines(L)
f.close()

a=open('t.txt','r')

# t=a.read()
# print(t)

# t1=a.readline()
# print(t1)

t2=a.readlines()
print(t2)