mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
print('-------------------')
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print('-------------------')
string = 'tutorialpython'

for x in string:
    print(x, end='  ')

print("\n**** Iterator Example *****")
itr = iter(string)

print(next(itr))
print('-------------------')
string = 'tutorialpython'

for x in string:
    print(x, end='  ')

print("\n**** Iterator Example *****")
itr = iter(string)

print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

print('-------------------')
numbers = [10, 20, 30, 40, 50]

itr = iter(numbers)

print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print('-------------------')

'''
In this list iterator example, we used the __next__() special method. 
If you observe the last statement, we are trying 
to return the next element that doesn’t exist. That’s why Python Iterator is calling StopIteration.
'''
numbers = [10, 20, 30, 40, 50]

itr = iter(numbers)

print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
#print(itr.__next__())
print('-------------------')
#set iter
mySet = {1, 2, 3, 4, 5}

ittr = iter(mySet)

print(ittr.__next__())
print(ittr.__next__())
print(ittr.__next__())
print(ittr.__next__())
print(ittr.__next__())
print('-------------------')
#tuple iterator
fruits = ('Apple', 'Orange', 'Grape', 'Banana', 'Kiwi')

fruit_itr = iter(fruits)

print(next(fruit_itr))
print(next(fruit_itr))
print(next(fruit_itr))
print(next(fruit_itr))
print(next(fruit_itr))
print('-------------------')
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print('-------------------')
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)