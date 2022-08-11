#inbuild polymarphism

a=5
b=6
print(a+b)
a='sugan'
b='moni'
print(a+b)

l="Hello"
print(len(l))
l1=[1,2,3,4]
print(len(l1))

#polymorphism with function

def addnumber(num1=0,num2=0):
   return num1+num2

a=addnumber(5,6)
b=addnumber(5)
c=addnumber()
print(a)
print(b)
print(c)


#polymorphism with class
class USA():
    def polymorphism(self):
        print("its my country")
    def countrytype(self):
        print('up')

class india():
    def polymorphism(self):
        print("its my country")
    def countrytype(self):
        print('tamilnadu')

a = USA()
b = india()

# a.polymorphism()
# a.countrytype()
#
# b.polymorphism()
# b.countrytype()

for c in (a,b):
    c.polymorphism()
    c.countrytype()




