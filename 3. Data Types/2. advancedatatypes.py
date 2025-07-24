# This part is optional since it will be repeated later in detail

# Variables can be in the form of data structures like lists, tuples, dictionaries etc.

# 1. SETS
'''A set is an unordered collection of data that is iterable 
(capable of returning its members one at a time), mutable (value can be changed), 
and has no duplicate elements.'''

set_one = {1,2,3,4,5, "New Stack"}
print("Set One: ",set_one)

# Set Operations
x = {"Hello"}
y = {"World"}
print(x|y) # Union
print(x&y) # Intersection

# 2. Dictionary - stores values in key value pairs
'''This type is an unordered collection of data values that are stored in key-value pairs'''

dict = {
"name": "Jack Wallen",
"client": "The New Stack",
"subject": "Python"
}

# accessing values inside a dictionary
print(dict["client"])

# 3. LISTS -- Lists are used to store multiple items in a single variable. 
'''Lists are mutable, ordered. Duplicates are allowed.  Elements can be accessed via index or List Slicing (later)'''

list_one = [1,2,3,4,5]
print(list_one)