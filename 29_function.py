def percent(marks):
    p = ((marks[0] + marks[1] +marks[2] +marks[3])/400)*100
    return p

marks1 = [45, 76, 54, 75]
percentage1 = percent(marks1)

marks2 = [95, 86, 34, 70]
percentage2 = percent(marks2)
print(percentage1, percentage2)


# quick
def greet(name="stranger"):
    print("Good Day, "+ name)

# def sum(num1, num2):
#     return num1+num2    
greet("AK")
greet()
s = sum(5, 6)
print(s)

