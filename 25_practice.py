# 1
names = ["ak", "py", "sk", "vk", "sy"]
name = input("enter name to check\n")

if name in names:
    print("your name is present in the list")
else:
    print("your name is not prsent in the list")

# 2
marks = int(input("enter your marks\n"))

if marks>90:
    grade ="EX"
elif marks>=70:
    grade = "A"
elif marks>=80:
    grade = "B"
elif marks>=60:
    grade = "C"
elif marks>=50:
    grade = "D"
else:
    grade= "F"
print("Your grade is: "+grade)
