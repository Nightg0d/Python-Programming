student = {
    "name": "Harsh Raj",
    "age": 22,
    "city": "Delhi"
}
print(student)
print(student["name"])
student["name"] = "Ritik kumar"
print(student["name"])
student.update ({'Mob no':9102233327})   # Crearing
print(student)
student["Marks"] = 94
print(student)

del student["city"]   # Deleting
print(student)


# Loop over dictionary
student = {
    "name": "Harsh",
    "age": 22,
    "course": "Python"
}

for key in student:
    print(key)

for i in student:
    print(student[i])

# 🐍 Dictionary Methods
# 1. keys() — Get all keys
student = {
    "name": "Harsh",
    "age": 22,
    "course": "Python"
}
print(student.keys())

# 2. values() — Get all values
print(student.values())

# 3. items() — Get keys + values
print(student.items())

# 4. get() — Get a value safely
print(student.get("city"))   # Output = none

# 5. update() — Add or update data
student.update({"city": "Delhi"})
print(student)

# 6. pop() — Remove a specific key
student = {
    "name": "Harsh",
    "age": 22,
    "course": "Python"
}
student.pop("age")
print(student)



# Q 1.Write a Python script to merge two Python dictionaries.
dict1 = {
    "name": "Harsh",
    "age": 22
}
dict2 = {
    "course": "Python",
    "city": "Delhi"
}
dict1.update(dict2)
print(dict1)


dict1 = {
    "name": "Harsh",
    "age": 22
}
dict2 = {
    "course": "Python",
    "city": "Delhi"
}
for key, value in dict2.items():
    dict1[key] = value
print(dict1)

# Q2. Write a Python program to sum all the values in a dictionary.
numbers = {
    "a": 10,
    "b": 20,
    "c": 30,
    "d": 40
}
total = 0
for value in numbers.values():
    total = total + value
print("Sum =", total)


# Q3. Count the frequency of each element
numbers = [1, 2, 2, 3, 1, 2]
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] = frequency[num] + 1
    else:
        frequency[num] = 1
print(frequency)


# Q4. Combine two dictionaries by adding values of common keys
dict1 = {
    "a": 10,
    "b": 20,
    "c": 30
}

dict2 = {
    "b": 30,
    "c": 40,
    "d": 50
}

result = dict1.copy()
for key, value in dict2.items():
    if key in result:
        result[key] = result[key] + value
    else:
        result[key] = value
print(result)