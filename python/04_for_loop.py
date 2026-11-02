for i in range(1,21,1):
    print(i)

# Print a table of n
table = int(input("Which table you want"))
for i in range(1,11):
    print(f"{table}*{i} = {table*i}")


a = "Hello world"
for i in range(len(a)):
    print(a[i])

name = "Ritik kumar"
for i in name:
    print(i)


# Break continue
for i in range(1,21):
    if i ==15:
        break
    else:
        print(i)


for i in range(1,21):
    if i ==15:
        continue
    print(i)

# 1. Accept an integer and print "Hello World" n times
n = int(input("Enter a number: "))
for i in range(n):
    print("Hello World")

# 2. Print natural numbers up to n
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print(i)

# 3. Reverse for loop — Print n to 1
n = int(input("Enter a number: "))
for i in range(n, 0, -1):
    print(i)
# 4. Take a number as input and print its table
table = int(input("Which table you want: "))
for i in range(1, 11):
    print(f"{table} * {i} = {table * i}")

# 5. Sum up to n terms
n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum =", total)

# 6. Factorial of a number
n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("Factorial =", factorial)

# 7. Sum of all even and odd numbers in a range separately
n = int(input("Enter a number: "))
even_sum = 0
odd_sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print("Sum of even numbers =", even_sum)
print("Sum of odd numbers =", odd_sum)

# 8. Print all factors of a number
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    if n % i == 0:
        print(i)

# 9. Check whether a number is a Perfect Number
n = int(input("Enter a number: "))
sum_factors = 0
for i in range(1, n):
    if n % i == 0:
        sum_factors += i
if sum_factors == n:
    print("Perfect number")
else:
    print("Not a perfect number")

# 10. Check whether a number is Prime
n = int(input("Enter a number: "))
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
if count == 2:
    print("Prime number")
else:
    print("Not a prime number")

# 11. Reverse a String Without Built-in Functions
text = input("Enter a string: ")
reverse = ""
for i in text:
    reverse = i + reverse
print("Reverse =", reverse)

# 12. Check if a String is Palindrome
text = input("Enter a string: ")
reverse = ""
for i in text:
    reverse = i + reverse
if text == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")