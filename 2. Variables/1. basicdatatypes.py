# Variables are used to temporarily store data in the computer's memory

# they have a name and value
# variable_name = variable_value

# Variables have 4 basic data types
# type(variable_name) -- to get the data type of the variable

# 1. INTEGERS (int)
price = 10
price = 20 # line by line running overwrites the values
print('price: ',price)
print("Data type of Price: ", type(price))

# 2. Floats/ Decimals (float)
rate = 4.9 #floats
print("Rate: ",rate)
print("Data type of Rate: ", type(rate))

# 3. Booleans (bool) -- they have 2 possible balues, either "True" or "False"
is_published = False
print("is_published: ",is_published)
print("Data type of 'is_published': ", type(is_published))

# 4. Strings (str)
name = "Fatima"
print("name: ",name)
print("Data type of name: ", type(name))

# Difference between bool and str
str_value = "True"
bool_value = True

# EXERCISE
'''We check in a patient John Smith. He is 20 years old and is a new to the clinic'''
# Solution
patient_name = "John Smith"
patient_age = 20
is_new = True

# More on built-in datatypes: https://www.w3schools.com/python/python_datatypes.asp