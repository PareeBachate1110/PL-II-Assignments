#Method Overloading
class calc:
    def add(self,a,b=0,c=0):
        return a+b+c
    
c=calc()
print(c.add(10))
print(c.add(10,30))
print(c.add(10,20,30))
print("---------------------------------------------")

#Method Overriding
class vehicle:
    def move(self):
        print("Vehicle is Moving")

class car(vehicle):
    def move(self):
        print("Driving on the Road")

class cycle(vehicle):
    def move(self):
        print("Pedalling on the Road")

c=car()
c1=cycle()

c.move()
c1.move()
print("---------------------------------------------")


#Operator Overloading
class Box:
    def __init__(self,weight):
        self.weight=weight

    def __add__(self,other):
        return self.weight+other.weight
    
b1=Box(500)
b2=Box(200)
print(b1+b2)
print("---------------------------------------------")
