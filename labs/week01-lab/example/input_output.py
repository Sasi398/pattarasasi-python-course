# Exercise # Exercise 1: Basic Input
print("=== Exercise 1: Basic Input ===")
user_name = "Pattarasasi"
print("Hello,", user_name, "!")
print("Nice to meet you,", user_name)

# Exercise 2: Input with Numbers
print("\n=== Exercise 2: Working with Numbers ===")
age = 21
print("You are", age, "years old")
print("Next year you will be", age + 1, "years old")

# Exercise 3: Multiple Inputs
print("\n=== Exercise 3: Multiple Inputs ===")
first_name = "Pattarasasi"
last_name = "Sasi"
birth_year = 2005

current_year = 2026
calculated_age = current_year - birth_year

print("Full name:", first_name + " " + last_name)
print("Calculated age:", calculated_age)

# Exercise 4: Different Print Formats
print("\n=== Exercise 4: Print Formatting ===")
name = "Alice"
score = 95
subject = "Math"

print("Student:", name, "Score:", score, "Subject:", subject)
print("Student: " + name + " Score: " + str(score) + " Subject: " + subject)
print("Student:", name, "scored", score, "in", subject)

# Exercise 5: Input Validation Practice
print("\n=== Exercise 5: Your Turn ===")

favorite_num = 9
print("Your favorite number times 2 is:", favorite_num * 2)

num1 = 10
num2 = 5
result = num1 + num2
print("The sum of", num1, "and", num2, "is", result)

# Exercise 6: Personal Information Collector
print("\n=== Exercise 6: Personal Information ===")

name = "Pattarasasi"
age = 21
color = "Blue"
hometown = "Chonburi"
birth_date = "9 March 2005"
favorite_number = 9

print("\n--- Your Information ---")
print("Name:", name)
print("Age:", age)
print("Birth Date:", birth_date)
print("Favorite Color:", color)
print("Hometown:", hometown)
print("Favorite Number:", favorite_number)
print("Thank you for sharing!")

# Exercise 7: Simple Calculator
print("\n=== Exercise 7: Simple Calculator ===")

number1 = 10
number2 = 5
operation = "+"

if operation == "+":
    result = number1 + number2
elif operation == "-":
    result = number1 - number2
elif operation == "*":
    result = number1 * number2
elif operation == "/":
    result = number1 / number2
else:
    result = "Invalid operation"

print("Result:", number1, operation, number2, "=", result)

# Exercise 8: Practice Problems
print("\n=== Exercise 8: Practice Problems ===")

user_name = "Pattarasasi"
user_age = 21
birth_year = 2026 - user_age
print(user_name + ", you were born in approximately", birth_year)

celsius = 30
fahrenheit = (celsius * 9/5) + 32
print(celsius, "degrees Celsius is", fahrenheit, "degrees Fahrenheit")

length = 10
width = 5
area = length * width
print("The area of a rectangle with length", length, "and width", width, "is", area)