m1 = int(input("enter marks for student no. 1: "))
m2 = int(input("enter marks for student no. 2: "))
m3 = int(input("enter marks for student no. 3: "))
m4 = int(input("enter marks for student no. 4: "))
m5 = int(input("enter marks for student no. 5: "))
m6 = int(input("enter marks for student no. 6: "))

myList =[m1, m2, m3, m4, m5, m6]
myList.sort()
print(myList)

# tuple change test

a = (2,5,7,8)
a[0] = 45

# sum a list
a =[3,7,97,5]
print(a[0]+a[1]+a[2]+a[3])
print(sum(a))

# count number of tuples
t=[6,0,8,0,4,6,0]
print(t.count(0))

