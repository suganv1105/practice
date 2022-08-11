#Hiear child
class father():
    def __init__(self,fname,fage):
        self.fname=fname
        self.fage=fage
    def printfatherdetails(self):
        print(f"father name={self.fname} and age={self.fage}")


class son1(father):
    def __init__(self,fname,fage,name,age):
        father.__init__(self,fname,fage)
        self.name=name
        self.age=age
    def printson1(self):
        print(f"son1 name={self.name} and age={self.age}")


class son2(father):
    def __init__(self, fname, fage, name, age):
        father.__init__(self, fname, fage)
        self.name = name
        self.age = age

    def printson2(self):
        print(f"son2 name={self.name} and age={self.age}")


class son3(father):
    def __init__(self, fname, fage, name, age):
        father.__init__(self, fname, fage)
        self.name = name
        self.age = age

    def printson3(self):
        print(f"son3 name={self.name} and age={self.age}")



s1=son1('Vengadasan',55,'Sugan',24)
s2=son2('Vengadasan',55,'moni',26)
s3=son3('Vengadasan',55,'sugan',28)

s1.printfatherdetails()
s1.printson1()

s2.printson2()
s3.printson3()
# -----------------------------------------------------------------------------------------------------------
class grandfather():
    def __init__(self,gname,gage):
        self.gname=gname
        self.gage=gage
    def printgrandfather(self):
        print(f"grandfather name={self.gname} and age={self.gage}")


class father(grandfather):
    def __init__(self,gname,gage,fname,fage):
        grandfather.__init__(self,gname,gage)
        self.fname=fname
        self.fage=fage
    def printfatherdetails(self):
        print(f"father name={self.fname} and age={self.fage}")

class mother():
    def __init__(self,mname,mage):
        self.mname=mname
        self.mage=mage
    def printmotherdetails(self):
        print(f"mother name={self.mname} and age={self.mage}")


class son(father,mother):
    def __init__(self,gname,gage,fname,fage,mname,mage,name,age):
        father.__init__(self,gname,gage,fname,fage)
        mother.__init__(self,mname,mage)
        self.name=name
        self.age=age
    def printson(self):
        print(f"son name={self.name} and age={self.age}")

s=son('ssk',90,'Vengadasan',55,'Latha',48,'Sugan',24)
s.printgrandfather()
s.printfatherdetails()
s.printmotherdetails()
s.printson()