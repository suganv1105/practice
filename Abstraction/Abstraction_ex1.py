from abc import ABC,abstractmethod
class car(ABC):
    def mileage(self):
        pass

class hyundai(car):
    def mileage(self):
        print(f"hyundai mileage is 20km/pl")

class BMW(car):
    def mileage(self):
        print(f"BMW mileage is 30km/pl")

class audi(car):
    def mileage(self):
        print(f"audi mileage is 40km/pl")

class tata(car):
    def mileage(self):
        print(f"tata mileage is 50km/pl")

h=hyundai()

b=BMW()

a=audi()

t=tata()

for z in(h,b,a,t):
    z.mileage()
