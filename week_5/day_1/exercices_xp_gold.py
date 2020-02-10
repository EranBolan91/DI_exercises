import random
#Exercise1
#1) Write a class called Circle that receives a radius as argument (default is 1.0):
#2) Write two (class) methods to compute perimeter and area:
class Radius():
    def __init__(self,radius):
        if radius == "":
            self.radius = 1.0
        else:
            self.radius = radius

    def perimeter(self):
        peri = 2 * 3.14 * self.radius
        return peri

    def area(self):
        ar = 3.14 * self.radius**2
        return ar

def geometrical(circle):
    perimeter = circle.perimeter()
    area = circle.area()
    print(f'The perimeter of the circle is {perimeter} And the area is {area}')


#circle = Radius(8)
#geometrical(circle)

#Custom List Class
#1) Write a custom list class called MyList, it receives a non empty python list (check it !!):
#2) Write a method that returns the reversed list:
#3) Write a method that returns the sorted list
#4) Write a method that generate a random list of the same length: TODO: Not clear what to do

class MyList():
    def __init__(self,list):
        if isinstance(list,list):
            self.list = list
        else:
            print("Its not a list")

    def reversedList(self,list):
        return list.reverse()

    def sortList(self,list):
        return list.sort()


#In the Quantum Realm
#1) Write a class called QuantumParticle and implement the following:
class QuantumParticale():
    def __init__(self,x,p,s):
        self.position = x
        self.momentum = p
        self.spin = s

    def position(self):
        return random.randrange(1,20)
    def momentum(self):
        return random.uniform(1,20)
    def spin(self):
        return random.randrange(0.5,-0.5)