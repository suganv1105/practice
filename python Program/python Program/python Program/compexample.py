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


transposed = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]

for i in range(len(matrix[0])):
    transposed_row = []

    for row in matrix:
        print(matrix)
        print(row[i])
        transposed_row.append(row[i])
        print(transposed_row)
    transposed.append(transposed_row)

print(transposed)

matrix = [[1, 2], [3,4], [5,6], [7,8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print (transpose)