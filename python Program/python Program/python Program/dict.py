# Create a dictionary to store employee record
D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev',
     'city': 'New York',
     'email': 'bob@web.com'}

# Create a dictionary with a list of two-item tuples
L = [('name', 'Bob'),
     ('age', 25),
     ('job', 'Dev')]

D = dict(L)
print(D)
# Prints {'name': 'Bob', 'age': 25, 'job': 'Dev'}

# Create a dictionary with a tuple of two-item lists
T = (['name', 'Bob'],
     ['age', 25],
     ['job', 'Dev'])

D = dict(T)
print(D)
# Prints {'name': 'Bob', 'age': 25, 'job': 'Dev'}

D = dict(name = 'Bob',
         age = 25,
         job = 'Dev')

print(D)
# Prints {'name': 'Bob', 'age': 25, 'job': 'Dev'}

# Create a dictionary with list of zipped keys/values
keys = ['name', 'age', 'job']
values = ['Bob', 25, 'Dev']

D = dict(zip(keys, values))

print(D)
# Prints {'name': 'Bob', 'age': 25, 'job': 'Dev'}


# Initialize dictionary with default value '0' for each key
keys = ['a', 'b', 'c']
defaultValue = 0

D = dict.fromkeys(keys,defaultValue)

print(D)
# Prints {'a': 0, 'b': 0, 'c': 0}

D = {'name': 'Bob',
     'age': 25,
     'name': 'Jane'}
print(D)
# Prints {'name': 'Jane', 'age': 25}

D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}

print(D['name'])
# Prints Bob

# When key is present
print(D.get('name'))
# Prints Bob

# When key is absent
print(D.get('salary'))
# Prints None

D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}

D['name'] = 'Sam'
print(D)
# Prints {'name': 'Sam', 'age': 25, 'job': 'Dev'}

D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}

D['city'] = 'New York'
print(D)
# Prints {'name': 'Bob', 'age': 25, 'job': 'Dev', 'city': 'New York'}

D1 = {'name': 'Bob',
      'age': 25,
      'job': 'Dev'}

D2 = {'age': 30,
      'city': 'New York',
      'email': 'bob@web.com'}

D1.update(D2)
print(D1)
# Prints {'name': 'Bob', 'age': 30, 'job': 'Dev',
#         'city': 'New York', 'email': 'bob@web.com'}

D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}

x = D.pop('age')
print(D)
# Prints {'name': 'Bob', 'job': 'Dev'}

# get removed value
print(x)
# Prints 25

D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}

del D['age']
print(D)
# Prints {'name': 'Bob', 'job': 'Dev'}

D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}

x = D.popitem()
print(D)
# Prints {'name': 'Bob', 'age': 25}

# get removed pair
print(x)
# Prints ('job', 'Dev')

D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}

D.clear()
print(D)
# Prints {}

D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}

# get all keys
print(list(D.keys()))
# Prints ['name', 'age', 'job']

# get all values
print(list(D.values()))
# Prints ['Bob', 25, 'Dev']

# get all pairs
print(list(D.items()))
# Prints [('name', 'Bob'), ('age', 25), ('job', 'Dev')]

D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}

for x in D:
    print(x)
# Prints name age job

D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}

for x in D:
    print(D[x])
# Prints Bob 25 Dev

D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}

print('name' in D)
# Prints True
print('salary' in D)
# Prints False

D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}

print('Bob' in D.values())
# Prints True
print('Sam' in D.values())
# Prints False

D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}

print(len(D))
# Prints 3
