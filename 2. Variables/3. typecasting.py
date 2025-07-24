#Tyep Casting: converting one data type to another
name = "Jane Doe"
age = 19
subjects = ["Math", "English", "Physics", "Chemistry"]
subjects_two = {"Math", "English", "Physics", "Chemistry"}

print(type(name)) #<class 'str'>
print(type(age)) #<class 'int'>
print(type(subjects)) # <class 'list'>
print(type(subjects)) # <class 'set'>

# we can convert some data types to other
# 1. int, float, str to int
print("Casting to Integers")
x = int(1)   # x to int
y = int(2.8) # y to int -- y = 2 (removed decimal)
z = int("3") # z to str, z = "3"
print(x, y, z)

# 2. int, float, str to float
print("Casting to Floats")
x1 = float(1)     # x will be 1.0
y2 = float(2.8)   # y will be 2.8
z2 = float("3")   # z will be 3.0
w2 = float("4.2") # w will be 4.2
print(x1, y2, z2, w2)

# 3. float, int, str to str
print("Casting to Strings")
x3 = str("s1") # x will be 's1'
y3 = str(2)    # y will be '2'
z3 = str(3.0)  # z will be '3.0'
print(x3, y3, z3)