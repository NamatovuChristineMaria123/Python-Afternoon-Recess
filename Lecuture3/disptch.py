from multipledispatch import dispatch

@dispatch(int, int, int)
def multiply(a, b, c):
    result = a * b * c
    print(result)

@dispatch(float, float, float)
def multiply(x, y, z):
    result = x * y * z
    print(result)

multiply(2, 3, 4)        
multiply(1.5, 2.5, 3.5)  