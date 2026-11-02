add = lambda a, b: a + b
print(add(10, 20))

check = lambda n: "Even" if n % 2 == 0 else "Odd"
print(check(8))
print(check(7))


def return_sum(func, L):
    result = 0

    for i in L:
        if func(i):
            result = result + i

    return result

L = [11, 14, 21, 23, 56, 78, 45, 29, 28]

x = lambda x: x % 2 == 0
y = lambda x: x % 2 != 0
z = lambda x: x % 3 == 0

print(return_sum(x, L))
print(return_sum(y, L))
print(return_sum(z, L))


# Map
l = [12,42,45,15,26,75]
print(list(map (lambda x : x*2,l)))
print(list(map (lambda x : x%2 == 0,l)))


# Filter
l = [1,2,3,4,5,6,7]
print(list(filter(lambda x:x>4,l)))

Fruits = ["Apple","oragnge","Mango","Banana"]
print(list(filter(lambda x: 'e' in x,Fruits)))


# Reduce
from functools import reduce
l = [1,2,3,4,5,6,7]
result = reduce(lambda x,y:x+y,l)
print(result)

L = [1, 2, 3, 4, 5, 6, 7]
print(L)

# Multiply each element by 2
L1 = [item * 2 for item in L]
print(L1)

# Calculate squares of numbers from 0 to 9
L2 = [i**2 for i in range(10)]
print(L2)

# Calculate cubes of numbers from 0 to 9
L3 = [i**3 for i in range(10)]
print(L3)
