i = 1
while i <= 30:
    print(i)
    i += 1

# 1. Separate each digit of a number
num = int(input("Enter a number: "))
while num > 0:
    digit = num % 10
    print(digit)
    num = num // 10

# 2. Accept a number and print its reverse
num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print("Reverse =", reverse)

# 3. Check whether a number is Palindrome
num = int(input("Enter a number: "))

original = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome number")


# 4. Random Number Guessing Game 🎯
import random
secret_number = random.randint(1, 100)
guess = int(input("Guess the number (1-100): "))
while guess != secret_number:
    if guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
    guess = int(input("Try again: "))
print("Congratulations! You guessed it!")