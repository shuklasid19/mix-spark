def add(x, y):
    return  x+y

def subtract(x, y):
    return x-y

def multiply(x, y):
    return  x*y

def division(x, y):
    if y==0:
        raise ValueError("0 division problem give another one")
    return x/y