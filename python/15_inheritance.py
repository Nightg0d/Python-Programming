class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

d = Dog()
d.eat()
d.bark()


# Polymorphism    1.Methodoverriding
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

class SmartPhone(Phone):
    def buy(self):
        print("Buying a smartphone")


s = SmartPhone(20000, "Apple", 13)
s.buy()


# Super keyword

class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

class SmartPhone(Phone):
    def buy(self):
        print("Buying a smartphone")
        super().buy()

s = SmartPhone(20000, "Apple", 13)
s.buy()




class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

class SmartPhone(Phone):
    def __init__(self, price, brand, camera, os, ram):
        super().__init__(price, brand, camera)
        self.os = os
        self.ram = ram
        print("Inside smartphone constructor")

s = SmartPhone(20000, "Samsung", 12, "Android", 2)

print(s.os)
print(s.brand)



# Method overloading and operator overloading

class Geometry:
    def area(self, a, b=0):
        if b == 0:
            print("Circle", 3.14 * a * a)
        else:
            print("Rect", a * b)

obj = Geometry()
obj.area(4)
obj.area(4, 5)




