# case 1 - if the file is not present
f = open('sample.txt','w')
f.write('Hello world')
f.close()

# write multiline strings
f = open('sample1.txt','w')
f.write('hello world')
f.write('\nhow are you?')
f.close()

# case 2 - if the file is already present
f = open('sample.txt','w')
f.write('salman khan')
f.close()

# Problem with w mode
# introducing append mode
f = open('sample1.txt','a')
f.write('\nI am fine')
f.close()

# write lines
L = ['hello\n','hi\n','how are you\n','I am fine']

f = open('sample.txt','w')
f.writelines(L)
f.close()

# reading from files
# -> using read()
f = open('sample.txt','r')
s = f.read()
print(s)
f.close()

# reading upto n chars
f = open('sample.txt','r')
s = f.read(10)
print(s)
f.close()

# readline() -> to read line by line
f = open('sample.txt','r')
print(f.readline(),end='')
print(f.readline(),end='')
f.close()

# reading entire using readline
f = open('sample.txt','r')

while True:

  data = f.readline()
  if data == '':
    break
  else:
    print(data,end='')
f.close()


# with
with open('sample1.txt','w') as f:
  f.write('selmon bhai')

# try f.read() now
with open('sample.txt','r') as f:
  print(f.readline())


# benefit? -> to load a big file in memory
big_L = ['hello world ' for i in range(1000)]
with open('big.txt','w') as f:
  f.writelines(big_L)

with open('big.txt','r') as f:
  chunk_size = 100
  while len(f.read(chunk_size)) > 0:
    print(f.read(chunk_size),end='***')
    f.read(chunk_size)


# seek and tell function
with open('sample.txt','r') as f:
  f.seek(15)
  print(f.read(10))
  print(f.tell())
  
  print(f.read(10))
  print(f.tell())


# seek during write
with open('sample.txt','w') as f:
  f.write('Hello')
  f.seek(0)
  f.write('Xa')

# more complex data
d = {
    'name':'nitish',
     'age':33,
     'gender':'male'
}
with open('sample.txt','w') as f:
  f.write(str(d))


# Serialization and Deserialization
# serialization using json module
# list
import json
L = [1,2,3,4]
with open('demo.json','w') as f:
  json.dump(L,f)


# dict
d = {
    'name':'nitish',
     'age':33,
     'gender':'male'
}
with open('demo.json','w') as f:
  json.dump(d,f,indent=4)


# deserialization
import json
with open('demo.json','r') as f:
  d = json.load(f)
  print(d)
  print(type(d))


# serialize and deserialize tuple
import json
t = (1,2,3,4,5)
with open('demo.json','w') as f:
  json.dump(t,f)


# serialize and deserialize a nested dict
d = {
    'student':'nitish',
     'marks':[23,14,34,45,56]
}
with open('demo.json','w') as f:
  json.dump(d,f)


# Serializing and Deserializing custom objects
class Person:
  def __init__(self,fname,lname,age,gender):
    self.fname = fname
    self.lname = lname
    self.age = age

person = Person('Nitish','Singh',33,'male')


# As a string
import json

def show_object(person):
  if isinstance(person,Person):
    return "{} {} age -> {} gender -> {}".format(person.fname,person.lname,person.age,person.gender)
with open('demo.json','w') as f:
  json.dump(person,f,default=show_object)


# As a dict
import json
def show_object(person):
  if isinstance(person,Person):
    return {'name':person.fname + ' ' + person.lname,'age':person.age,'gender':person.gender}

with open('demo.json','w') as f:
  json.dump(person,f,default=show_object,indent=4)


# deserializing
import json

with open('demo.json','r') as f:
  d = json.load(f)
  print(d)
  print(type(d))


# Pickling and unpickling
class Person:

  def __init__(self,name,age):
    self.name = name
    self.age = age

  def display_info(self):
    print('Hi my name is',self.name,'and I am ',self.age,'years old')

p = Person('nitish',33)

# pickle dump
import pickle
with open('person.pkl','wb') as f:
  pickle.dump(p,f)

# pickle load
import pickle
with open('person.pkl','rb') as f:
  p = pickle.load(f)

p.display_info()


