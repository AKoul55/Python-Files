# empty dict
a ={}
print(type(a))
# addig values to empty set
b = set()
print(type(b))
b.add(4)
b.add(5)
b.add(4) # adding a value repeatively don't change set
b.add((9,6,5))

# b.add({4:5}) #list and dict can't be add in sets
print(b)

# print((4,5,6))
# print(len(b)) #length of sets

b.remove(5)
# b.remove(15) #throws an error while removing the values which is not present
print(b)

print(b.pop())
print(b)