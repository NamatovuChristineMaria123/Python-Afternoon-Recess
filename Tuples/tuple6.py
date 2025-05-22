# Write a python program to remove/delete the first item in your tuple.
x = ("samsung", "iphone", "tecno", "redmi")
x = list(x)
del x[0]
x = tuple(x)
print(x)