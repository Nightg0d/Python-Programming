# Encapsulation:- combining data and the methods that work on that data inside a single class.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
s1 = Student("Harsh", 85)
print(s1.name)
print(s1.marks)
s1.marks = -100

print(s1.marks)


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks
    def get_marks(self):
        return self.__marks
s1 = Student("Harsh", 85)
print(s1.name)
print(s1.get_marks())


# Getter: A method used to access or read a private-style attribute.
# Setter: A method used to update a private-style attribute with some validation.
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    # Getter
    def get_balance(self):
        return self.__balance

    # Setter
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
            print("Balance updated successfully")
        else:
            print("Balance cannot be negative")


account = BankAccount("Harsh", 5000)

print(account.get_balance())

account.set_balance(8000)
print(account.get_balance())

account.set_balance(-2000)
print(account.get_balance())


# Reference variable:-variable that refers to an object in memory
class Customer:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
def greet(customer):
    if customer.gender == "Male":
        print("Hello", customer.name, "sir")
    else:
        print("Hello", customer.name, "ma'am")
cust = Customer("Nitish", "Male")
greet(cust)


# Collection of object
class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
c1 = Customer("Nitish", 34)
c2 = Customer("Ankit", 45)
c3 = Customer("Neha", 32)

L = [c1, c2, c3]

for i in L:
    print(i.name, i.age)



# Static variables and methods.
# An instance variable stores data that belongs to a particular object.
class Student:
    def __init__(self, name):
        self.name = name
s1 = Student("Harsh")
s2 = Student("Rahul")
print(s1.name)
print(s2.name)

# A static variable, commonly called a class variable in Python, belongs to the class and is shared by its instances.
class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

s1 = Student("Harsh")
s2 = Student("Rahul")

print(s1.name)
print(s2.name)

print(s1.school)
print(s2.school)
print(Student.school)


# Change the static variable
class Student:
    school = "ABC School"
s1 = Student()
s2 = Student()

Student.school = "XYZ School"

print(s1.school)
print(s2.school)



# A static method is a method defined inside a class that does not automatically receive self or cls.
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
print(Calculator.add(10, 20))


class Student:
    school = "ABC School"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def is_adult(age):
        return age >= 18
s1 = Student("Harsh", 20)
print(s1.name)
print(Student.school)
print(Student.is_adult(20))
print(Student.is_adult(15))


# Class relationship aggregation
class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

    def edit_profile(self, new_name, new_city, new_pin, new_state):
        self.name = new_name
        self.address.change_address(new_city, new_pin, new_state)


class Address:
    def __init__(self, city, pincode, state):
        self.city = city
        self.pincode = pincode
        self.state = state

    def change_address(self, new_city, new_pin, new_state):
        self.city = new_city
        self.pincode = new_pin
        self.state = new_state


add = Address("Kolkata", 700156, "WB")
cust = Customer("Nitish", "Male", add)

cust.edit_profile("Ankit", "Gurgaon", 122011, "Haryana")
print(cust.address.city)
print(cust.address.pincode)
