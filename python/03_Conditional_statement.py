age = 17
if age >= 18:
    print("You are an adult")
else:
    print("You are kids")

money = int(input("Please provide me money"))
if money >=10:
    print("I will bye ice cream")
else:
    print("I will bye chocklate")


marks = 75

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
else:
    print("D")


# Q1. Accept two numbers and print the greatest
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("Greatest number is:", num1)
elif num2 > num1:
    print("Greatest number is:", num2)
else:
    print("Both numbers are equal")

# Q2. Accept gender and print greeting
gender = input("Enter your gender (M/F): ")

if gender == "M":
    print("Good Morning Sir")
elif gender == "F":
    print("Good Morning Ma'am")
else:
    print("Invalid gender")

# Q3. Check whether a number is even or odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Q4. Check whether the user is a valid voter
name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print("Hello", name, "you are a valid voter")
else:
    print("Hello", name, "you are not a valid voter")

# Q5. Check whether a year is a leap year
year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")


# 🌡️ Temperature if-elif Ladder
temperature = float(input("Enter temperature in Celsius: "))

if temperature < 0:
    print("Freezing Cold")
elif temperature < 10:
    print("Very Cold")
elif temperature < 20:
    print("Cold")
elif temperature < 30:
    print("Pleasant")
elif temperature <= 40:
    print("Hot")
else:
    print("Very Hot")
