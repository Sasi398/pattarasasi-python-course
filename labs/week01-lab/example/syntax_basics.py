"""
Week 1 Lab - Python Syntax Basics
Learn about variables, data types, and basic Python syntax.
"""

# Exercise 1: Variables and Assignment
name = "Pattarasasi"
age = 21
height = 5.41
is_student = True

# Print all variables
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# Exercise 2: Data Types
my_string = "Hello Python"
my_integer = 42
my_float = 3.14
my_boolean = False

# Use type() to see the data type
print("Type of my_string:", type(my_string))
print("Type of my_integer:", type(my_integer))
print("Type of my_float:", type(my_float))
print("Type of my_boolean:", type(my_boolean))

# Exercise 3: String Operations
first_name = "John"
last_name = "Doe"

# Concatenate strings
full_name = first_name + " " + last_name
print("Full name:", full_name)

# String length
print("Length of full name:", len(full_name))

# Exercise 4: Numbers and Arithmetic
num1 = 10
num2 = 3

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Integer Division:", num1 // num2)
print("Remainder (Modulo):", num1 % num2)
print("Power:", num1 ** num2)

# Exercise 5: Variable Reassignment
counter = 0
print("Initial counter:", counter)

counter = counter + 1
print("After increment:", counter)

counter = counter + 5
print("After adding 5:", counter)

# Exercise 6: Multiple Assignment
x, y, z = 1, 2, 3
print("x =", x, "y =", y, "z =", z)

# All variables get the same value
a = b = c = 10
print("a =", a, "b =", b, "c =", c)

# Exercise 7: Practice with Different Data Types

# String variable containing your favorite color
favorite_color = "Blue"

# Integer variable with the current year
current_year = 2026

# Float variable with your favorite number (with decimal)
favorite_number = 9.0

# Boolean variable indicating if you like pizza
likes_pizza = True

# Print all variables with descriptive messages
print("My favorite color is:", favorite_color)
print("The current year is:", current_year)
print("My favorite number is:", favorite_number)
print("Do I like pizza?", likes_pizza)