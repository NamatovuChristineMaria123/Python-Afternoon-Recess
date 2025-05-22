# Write a set of 4 items and a list of two items. Write a python program to add elements in the list to elements in the set.
mySet = {"benz", "toyota", "volvo", "pickup"}
myList = ["tyres", "mirrors"]
mySet.update(myList)
print(mySet)