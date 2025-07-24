# Global variable
x = "awesome"

def func():
    # Inside func(), Python looks for a local variable named x, doesn't find it, and uses the global x instead.
    print("python is",x)

func()
