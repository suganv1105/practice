class grandfather():
    def _init_(self,gname,gage):
        self.gname=gname
        self.gage=gage
    def printgrandfather(self):
        print(f"grandfather name={self.gname} and age={self.gage}")


class father(grandfather):
    def _init_(self,gname,gage,fname,fage):
        grandfather._init_(self,gname,gage)
        self.fname=fname
        self.fage=fage
    def printfatherdetails(self):
        print(f"father name={self.fname} and age={self.fage}")

class mother():
    def _init_(self,mname,mage):
        self.mname=mname
        self.mage=mage
    def printmotherdetails(self):
        print(f"mother name={self.mname} and age={self.mage}")


class son(father,mother):
    def _init_(self,gname,gage,fname,fage,mname,mage,name,age):
        father._init_(self,gname,gage,fname,fage)
        mother._init_(self,mname,mage)
        self.name=name
        self.age=age
    def printson(self):
        print(f"son name={self.name} and age={self.age}")

s=son('ssk',90,'kumar',55,'paramu',48,'santhosh',24)
s.printgrandfather()
s.printfatherdetails()
s.printmotherdetails()
s.printson()