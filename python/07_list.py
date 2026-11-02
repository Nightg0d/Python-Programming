a = [12,13,14,15,16,34.5,True]
print(a[0])
print(a[0:4])

# List traversing and methord
fruits = ["apple", "banana", "mango", "orange"]
for fruit in fruits:
    print(fruit)

# 1. append() — Add an item at the end
fruits = ["apple", "banana"]
fruits.append("mango")
print(fruits)

# 2. insert() — Add at a specific position
fruits = ["apple", "mango"]
fruits.insert(1, "banana")
print(fruits)

# 3. extend() — Add multiple items
numbers = [1, 2, 3]
numbers.extend([4, 5, 6])
print(numbers)


# 4. remove() — Remove a value
fruits = ["apple", "banana", "mango"]
fruits.remove("banana")
print(fruits)

# 5. pop() — Remove by index
fruits = ["apple", "banana", "mango"]
fruits.pop(1)
print(fruits)

# 6. clear() — Remove everything
numbers = [10, 20, 30]
numbers.clear()
print(numbers)

# 7. index() — Find the index
fruits = ["apple", "banana", "mango"]
position = fruits.index("banana")
print(position)

# 8. count() — Count occurrences
numbers = [10, 20, 10, 30, 10]
print(numbers.count(10))

# 9. sort() — Sort the list
numbers = [50, 20, 40, 10, 30]
numbers.sort()
print(numbers)

# 10. reverse() — Reverse the list
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)

# 1. Print Positive and Negative Elements of a List
numbers = [10, -5, 20, -8, 0, 15, -2]

print("Positive numbers:")
for number in numbers:
    if number > 0:
        print(number)
print("Negative numbers:")
for number in numbers:
    if number < 0:
        print(number)


# 2. Find Mean of List Elements
numbers = [10, 20, 30, 40, 50]
total = 0
for number in numbers:
    total += number
mean = total / len(numbers)
print("Mean =", mean)


# 3. Find Greatest Element and Print Its Index
numbers = [10, 45, 20, 80, 35]

greatest = numbers[0]
index = 0
for i in range(len(numbers)):
    if numbers[i] > greatest:
        greatest = numbers[i]
        index = i
print("Greatest element =", greatest)
print("Index =", index)


# 4. Check if List is Sorted or Not
numbers = [10, 20, 30, 40, 50]

if numbers == sorted(numbers):
    print("List is sorted")
else:
    print("List is not sorted")
