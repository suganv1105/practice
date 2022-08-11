class student():
    def __init__(self,ID,name,age,location,phone):
        self.ID=ID
        self.name=name
        self.age=age
        self.location=location
        self.phone=phone
    def printstudentdetails(self):
        print(f"ID={self.ID}, name={self.name}, age={self.age}, location={self.location}, phone={self.phone}")

a=student(1,"Sugan",20,"SPR",8220926508)
a.printstudentdetails()