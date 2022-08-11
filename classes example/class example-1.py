#single inheritance
class father():
    def __init__(self,fname,fage):
        self.fname=fname
        self.fage=fage
    def printfatherdetails(self):
        print(f"father name={self.fname} and age={self.fage}")
class son(father):
    def __init__(self,fname,fage,name,age):
        father.__init__(self,fname,fage)
        self.name=name
        self.age=age
    def printson(self):
        print(f"son name={self.name} and age={self.age}")

s=son('Sugan',55,'Vengadasan',24)
s.printfatherdetails()
s.printson()

# -----------------------------------------------------------------------------------
class parent:
    def __init__(self,pname,page):
        self.pname=pname
        self.page=page

    def printparent(self):
        print(self.pname)
        print(self.page)

class child(parent):
    def __init__(self, pname,page,cname,cage):
        parent.__init__(self,pname,page)
        self.cname=cname
        self.cage=cage

    def printchild(self):
        print(self.cname)
        print(self.cage)


c=child('vengadasan',50,'sugan',20)

c.printparent()
c.printchild()
