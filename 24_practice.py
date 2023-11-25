# 1
num1 = int(input("enter number 1: "))
num2 = int(input("enter number 2: "))
num3 = int(input("enter number 3: "))
num4 = int(input("enter number 4: "))

if(num1>num4):
    f1 = num1
else:
    f1 = num4

if(num2>num3):
    f2 = num2
else:
    f2 = num3

if(f1>f2):
    print(str(f1)+ " is greatest")
else:
    print(str(f2)+ "is greatest")

# 
sub1 = int(input("enter 1st subject marks"))
sub2 = int(input("enter 1st subject marks"))
sub3 = int(input("enter 1st subject marks"))

if(sub1<33 or sub2<33 or sub3<33):
    print("you are fail less than 33%")
elif(sub1+sub2+sub3)/3 <40:
        print("you are fail due to total % less than 40")
else:
     print("cong! you passed the exam")

#  3
text = input("enter the text\n")

if("make a lot of money" in text):
     spam = True
elif("buy now" in text):
     spam = True
elif("click now" in text):
     spam = True     
elif("subscribe now" in text):
     spam = True  
else:
     spam = False
if(spam):
     print("This text is spam")
else:
     print("this text is not spam")  

# 4
a = input("Enter you name:\n")
chars = len(a)

if(chars>10):
  print("This name have more than 10 alphabets")  
elif(chars==10):
  print("This name have 10 Alphabets")
else:
  print("This name have less than 10 Alphabets") 