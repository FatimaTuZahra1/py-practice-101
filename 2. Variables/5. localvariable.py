# Global variable
x = "awesome"

def func():
    x = "easy"
    # Inside func(), Python looks for a local variable named x, finds it, and uses it.
    print("python is",x)

func()
