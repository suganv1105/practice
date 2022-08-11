# any non-zero value
if -3:
    print('True')
# Prints True

# mathematical expression
x, y = 7, 5
if x + y:
    print('True')
# Prints True

# nonempty container
L = ['red','green']
if L:
    print('True')
# Prints True

x, y, z = 7, 4, 2
if x > y:
    print("x is greater than y")
    if x > z:
        print("x is greater than y and z")

# Prints x is greater than y
# Prints x is greater than y and z

x, y = 7, 5
if x < y:
    print('y is greater')
else:
    print('x is greater')

# Prints x is greater

x, y = 5, 5
if x > y:
    print('x is greater')
elif x < y:
    print('y is greater')
else:
    print('x and y are equal')

# Prints x and y are equal

choice=1

if choice == 1:
	print('case 1')
elif choice == 2:
	print('case 2')
elif choice == 3:
	print('case 3')
elif choice == 4:
	print('case 4')
else:
	print('default case')

x, y, z = 7, 4, 2
if x > y and x > z:
    print('x is greater')

# Prints x is greater


x, y, z = 7, 4, 9
if x > y or x > z:
    print('x is greater than y or z')

# Prints x is greater than y or z


x, y = 7, 5
if not x < y:
    print('x is greater')

# Prints x is greater


x, y = 7, 5
if x > y: print('x is greater')

# Prints x is greater


x, y = 7, 5
if x > y: print('x is greater'); print('y is smaller'); print('x and y are not equal')


# list
L = ['red', 'green', 'blue']
if 'red' in L:
    print('yes')
# Prints yes

# tuple
T = ('red', 'green', 'blue')
if 'red' in T:
    print('yes')
# Prints yes

# string
S = 'Hello, World!'
if 'Hello' in S:
    print('Yes')
# Prints yes


age=int(input("enter the age"))
if(age<18):
    print("no vote")
    print("wer")
    
else:
    print("vote")
y=25
z=3
y/=z
print(y)
    

