# VERSION 1
'''
# Global variable
x = "awesome"

def func():
    # local variable given global access
    global x 
    x = "easy"

func() # changes the value of x
print("python is",x)
'''
# VERSION 2

def func():
    # local variable given global access
    global x 
    x = "easy"

func() # changes the value of x

x = "awesome" # Global variable, changes the value of x again
print("python is",x)

