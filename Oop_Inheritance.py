#OOP (Object-Oriented Programming).
#Multiple     → Many Parents → One Child
#Multilevel   → Grandparent → Parent → Child
#Hierarchical → One Parent → Many Children
#Polymorphism → One Method → Many Behaviors

#Multiple Inheritance
#Multiple independent parents give access to a single child class


class Father:
    def skill1(self):
        print("Father is working in Army")

class Mother:
    def skill2(self):
        print("Mother is a Designer")

class Child(Father, Mother):
    def skill3(self):
        print("Child is a Programmer")

obj = Child()

obj.skill1()
obj.skill2()
obj.skill3()


#Multilevel Inheritance
#If a child is inheritance and depending on the props of another inheritance in a child.


class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

class SportsCar(Car):
    def speed(self):
        print("Sports car is fast")

obj = SportsCar()

obj.start()
obj.drive()
obj.speed()


#Hierarchical Inheritance
#if a single parent is having multiple child so that the property access is distributed a among all the child in a limited way.

class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

class Bike(Vehicle):
    def ride(self):
        print("Bike is riding")

car = Car()
bike = Bike()

car.start()
car.drive()

bike.start()
bike.ride()


#Polymorphism
#If a function with same name performs different behaviours in a same program.


class Car:
    def move(self):
        print("Car is moving")

class Boat:
    def move(self):
        print("Boat is sailing")

for vehicle in [Car(), Boat()]:
    vehicle.move()













