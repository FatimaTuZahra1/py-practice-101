# VARIABLE NAMES

'''
Rules for Python variables:

A variable name must start with a letter or the underscore character (e.g. age, _age, full_name)
A variable name cannot start with a number (e.g. 25name is incorrect)
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
'''

full_name = "John Smith"

# _age and age are not the same. Python is case sensitive
_age = 25
age = 30

# Printing different data types together
x = 30
y = 30

# the + operator adds ints
print(x+y)

# the + operator concatenates strings
str_one = "Hi, I am Learning "
str_two = "Python"
print(str_one + str_two)

# ints and str can be printed together with , or using formatted strings
print("Sum: ",x+y)
print(f'The sum is {x+y}') # formatted string

# Cases:

# 1. Snake Case:
full_name = "Fatima Tu Zahra"

# 2. Screaming Snake Case -- used for declaring constants
GRAVITATIONAL_CONSTANT = 9.8

# 3. Camel Case -- first word non-capitalized
myVariableName = 30

# 4. Pascal Case -- all words capitalized
MyVariableName = 30