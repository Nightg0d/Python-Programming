# local and global
# global var
a = 2
def temp():
  # local var
  b = 3
  print(b)
temp()


# local and global
# global var
a = 2
def temp():
  # local var
  b = 3
  print(b)
temp()


# local and global -> local does not have but global has
a = 2
def temp():
  # local var
  print(a)
temp()
print(a)


a = 2
def temp():
  # local var
  global a
  a += 1
  print(a)
temp()
print(a)


# local and global -> global created inside local
def temp():
  # local var
  global a
  a = 1
  print(a)
temp()
print(a)


# built-in scope
import builtins
print(dir(builtins))


# Enclosing scope
def outer():
  def inner():
    print(a)
  inner()
  print('outer function')
outer()
print('main program')


# nonlocal keyword
def outer():
  a = 1
  def inner():
    nonlocal a
    a += 1
    print('inner',a)
  inner()
  print('outer',a)
outer()
print('main program')


# Decorators
# Python are 1st class function

def modify(func,num):
  return func(num)
def square(num):
  return num**2
modify(square,2)


# simple example

def my_decorator(func):
  def wrapper():
    print('***********************')
    func()
    print('***********************')
  return wrapper

def hello():
  print('hello')

def display():
  print('hello nitish')

a = my_decorator(hello)
a()

b = my_decorator(display)
b()



# Better syntax?
# simple example

def my_decorator(func):
  def wrapper():
    print('***********************')
    func()
    print('***********************')
  return wrapper

@my_decorator
def hello():
  print('hello')

hello()