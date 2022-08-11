# Python Print Examples
print("Hello World")
print('Hello World!')
print("Learn", 'Python Programming')
print("Learn", 'Python', 'Programming')
print()
print(' ')
print()
print(' ')
print("Hello World")
print()
print('Learn', 'Python Programming')
print(' ')
print('Hi')
number = 100

print(number)
print('number')
name = 'Tutorial'
print(name)
print('name')
print('Number = ', number)
print('Name = ', name)

numbers_list = [10, 20, 30, 40, 50]
fruits_list = ['apple', 'cherry', 'mango', 'kiwi']

print(numbers_list)
print(fruits_list)

numbers_tuple = (15, 25, 35, 45, 55)
fruits_tuple = ('apple', 'cherry', 'kiwi', 'mango')

print(numbers_tuple)
print(fruits_tuple)

numbers_Set = {1, 2, 3, 4, 5}
fruits_Set = {'apple', 'kiwi', 'banana', 'orange'}
mixed_Set = {'banana', 1, 2, (1, 2, 3)}

print(numbers_Set)
print(fruits_Set)
print(mixed_Set)

myDict = {'name': 'Kevin', 'age': 25, 'job': 'Developer'}
print(myDict)

print("A", "B", "C", sep="")
print("A", "B", "C", sep=" ")

print("Hello", "World", sep="*")

print('Learn', 'Python Programming', sep="---")

print('Learn', 'Python', 'Programming', sep=" ")
print('Learn', 'Python', 'Programming', sep=" # ")

print("Hello", "World", sep=" AAA ")
print("Hello", "World", sep=',,,...,,,')

print('Welcome to')
print('Tutorial python')

print('-----')
print('Welcome to', end=' ')
print('Tutorial', end='.')
print()
print(10, 20, 30)
print('A', 'B', 'C')

print(10, 20, 30, sep=' , ')
print('A', 'B', 'C', sep=', ')

print(10, 20, 30, sep=' @ ')
print('A', 'B', 'C', sep=' -- ')

print('-------------')
print(10, 20, 30, sep=' @ ', end=' **** ')
print()
print('A', 'B', 'C', sep='--', end=' . ')

print()
print('A', 'B', 'C', sep=' , ', end='  #####  ')
print(10, 20, 30, sep=' @ ', end=' !!! ')

num = 1234

print('Number = ', num, sep='****', end='!')
print()
print('Number = ', num, sep='0000', end='.')
print()
print('Number = ', num, sep='0000', end='?\n\n\n')
print('Number = ', num, sep='0000', end='@\n')

name = 'Babu Megavarnam'
person = 'Navis'
year = 2020

print('{0} is working at {1}'.format(person, name))
print('Copyright {} at {}'.format(name, year))

s = 'Hi there, "How are You?"'
s1 = 'Hi there, \"How are You?\"'

print(s)
print(s1)

print('I Can\'t Do that')
print('I Don\'t Know you')

value = 100000
text = 'BABU MEGAVARNAM'
science = 1.20023456341
cr = 'u'

print('%d' % value)
print('%i' % value)
print('%u' % value)
print('%o' % value)
print('%x' % value)
print('%X' % value)

print('%f' % science)
print('%e' % science)
print('%E' % science)

print('%g' % science)
print('%G' % science)

print('%c' % cr)
print('%s is a string representation' % value)
print('%s' % text)