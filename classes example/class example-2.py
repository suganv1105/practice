#multilevel inheritance
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
class son(father):
    def __init__(self,gname,gage,fname,fage,name,age):
        father.__init__(self,gname,gage,fname,fage)
        self.name=name
        self.age=age
    def printson(self):
        print(f"son name={self.name} and age={self.age}")

s=son('ssk',90,'vengadasan',55,'sugan',20)
s.printgrandfather()
s.printfatherdetails()
s.printson()