a = (1,2,3,4,5,4,5)
print(a[2])
print(type(a))

numbers = (10, 20, 30, 40, 50)
print(numbers[1:4])

# Tuple methord:   1.Count
numbers = (10, 20, 10, 30, 10)
print(numbers.count(10))

# Index: Find the index of the value
numbers = (10, 20, 30, 40)
print(numbers.index(30))



# Set
s={1,2,3,4,5}
print(s)

# 2. Duplicate Values
numbers = {10, 20, 10, 30, 20, 40}
print(numbers)

# 4. Sets Are Mutable
numbers = {10, 20, 30}
numbers.add(40)
print(numbers)

# 6. update()
numbers = {1, 2, 3}
numbers.update([4, 5, 6])
print(numbers)

# 7. remove()
numbers = {10, 20, 30}
numbers.remove(20)
print(numbers)

# 9. pop():-pop() removes an arbitrary element from a set.
numbers = {10, 20, 30}
numbers.pop()
print(numbers)

# 10. clear()
numbers = {10, 20, 30}
numbers.clear()
print(numbers)

# 11. len():-You can find the number of elements:
numbers = {10, 20, 30, 40}
print(len(numbers))