# 1
num = int(input("Enter the no."))
for i in range(1, 11):
    # print(str(num)+ "X" + str(i) + '=' +str(i*num))
    print(f"{num}X{i}={num*i}")

    #  2
l1 =["Ak", "Sv", "Te", "yr"]

for name in l1:
    if name.startswith("S"):
        print("hello " + name)    


# 3
num = int(input("enter the number\n")) 
prime = True

for i in range(2, num):
    if(num%i ==0):
        prime = False
        break
    if prime:
        print("this number is prime")
    else:
        print("this number is not prime")
        
# 4
num = int(input("enter the number\n")) 
factorial =1
for i in range(1, 1+num):
    factorial = factorial *i
print(f"the factorial of thie {num} is {factorial}")

# 5
num = int(input("enter the number\n")) 
sum =0
for i in range(1, num+1):
    sum = sum*i
print(f"the sum of thie {num} is {sum}")


# 6
n = 4
for i in range(4):
    print("*" * (i+1))

#7
n=3
for i in range(3):
    print(" " * (n-i-1), end="")
    print("*" * (2*i+1), end="")
    print(" " * (n-i-1)) 

#8
num = int(input("Enter the no."))
for i in range(1,11):
    # print(str(num)+ "X" + str(i) + '=' +str(i*num))
    print(f"{num}X{i}={num*i}") 