h_letters = []

for letter in 'human':
    h_letters.append(letter)

print(h_letters)

h_letters = [ letter for letter in 'human' ]
print( h_letters)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


newlist = [x.upper() for x in fruits]
print(newlist)

for y in range(100):
    if y % 2 == 0:
        if y % 5 == 0:
            print(y)

num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)

for i in range(10):
    if i % 2 == 0:
        print("even")
    else:
        print("odd")


obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
print(obj)

for i in range(7,9):
        for j in range(1,11):
               print(f"{i}*{j}={i*j}")
l2=[]
[[l2.append(i*j) for j in range(1,11)] for i in range(7,9)]
print(l2)

l=[]
[l.append(i) for i in range(8) if i%2==0 if i%3==0]
print(l)

tags = ['man', 'you', 'are', 'awesome']
entries = [['man', 'thats'],[ 'right','awesome']]

result = []

for tag in tags:
    for entry in entries:
        if tag in entry:
            result.extend(entry)

print(result)
res=[]
[res.extend(entry) for tag in tags for entry in entries if tag in entry]
print(res)

lst = []
for i in range(100):
    if i > 10:
        for j in range(i):
            if j < 20:
                lst.append(j)

print(lst)
j1=[]
[j1.append(j) for i in range(100) if i > 10 for j in range(i) if j < 20]

print(j1)


