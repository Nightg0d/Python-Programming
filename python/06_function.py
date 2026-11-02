def hello():
    print("This is a hello function and this print hello")
hello()

def add(a, b):
    print(f"The sun of two number is {a + b}")
add(45,45)

# 1. Positional Arguments
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student("Ritik", 22)

# 2. Keyword Arguments
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=22, name="Harsh")


# Default argument
def add(a, b=10):
    return a + b
print(add(5))


def pallindrome(st):
    rev = ""
    for i in range(len(st)-1, -1, -1):
        rev = rev + st[i]
    if rev == st:
        print("pallindrome")
    else:
        print("not a pallindrome")

pallindrome('naman')
pallindrome("Ritik")