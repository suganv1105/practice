#multiple inheritance
class father():
    def __init__(self,fname,fage):
        self.fname=fname
        self.fage=fage
    def printfatherdetails(self):
        print(f"father name={self.fname} and age={self.fage}")

class mother():
    def __init__(self, mname, mage):
        self.mname = mname
        self.mage = mage
    def printmotherdetails(self):
        print(f"mother name={self.mname} and age={self.mage}")

class son(father,mother):
    def __init__(self,fname,fage,mname,mage,name,age):
        father.__init__(self,fname,fage)
        mother.__init__(self,mname,mage)
        self.name=name
        self.age=age
    def printson(self):
        print(f"son name={self.name} and age={self.age}")

s=son('Vengadasan',48,'Latha',55,'sugan',20)
s.printfatherdetails()
s.printmotherdetails()
s.printson()