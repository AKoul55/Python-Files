# use open function to read the content of a file!
# f = open('sample.txt', 'r')
f = open("sample.txt") #by default the mode is r
# data = f.read()
data = f.read(5) #read first 5 character from the file
print(data)
f.close()


# readline function
f = open("sample.txt") 
# readfirst line
data = f.readline()
print(data)
# read 2nd line
data = f.readline()
print(data)
# read 3rd line
data = f.readline()
print(data)
f.close()

# write function
f = open('another.txt', 'w')
f.write("kya chl raha ha")
f.close()

f = open("this.txt",'w')
f.write("this is nice")
f.close()

# with statement
with open('another.txt', 'r') as f:
    a = f.read() 
with open('another.txt', 'w') as f:
    a = f.write("me")
    print(a) 