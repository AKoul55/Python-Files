class Employee:
    comapny = "Camel"
    salary = 100
    location = "Delhi"
    # company = "Bharat Gas"
    # salary = 47683
    # salarybonus = 434

    # def changeSalary(self, sal):
    #     self.__class__.salary = sal

    @classmethod
    def changeSalary(cls, sal):
        cls.salary = sal
    # @property
    # def totalSalary(self):
    #     return self.salary + self.salarybonus
    

e = Employee()
print(e.employee)  
e.changeSalary(7346)
print(e.salary)  
print(Employee.salary)


# getter
class Employee:
    company = "Bharat Gas"
    salary = 50000
    salarybonus = 400
    
    @property
    def totalSalary(self):
        return self.salary + self.salarybonus
    
    # setter
    @totalSalary.setter
    def totalSalary(self, val):
        self.salarybonus = val - self.salary
    

e = Employee()
print(e.totalSalary)
e.totalSalary =60088
print(e.salary)
print(e.salarybonus)

# overloading
class Number:
    def __init__(self, num):
        self.num = num
    
    def __add__(self, num2):
        print("Lets add")
        return self.num +num2.num
    
    def __mul__(self, num2):
        print("Lets multiply")
        return self.num *num2.num
    
    def __str__(self):
      return f"Decimal Number: {self.num}"  
    
    def __len__(self):
        return 1
    
n = Number(9)
print(n)
print(len(n))


# n1 = Number(4)
# n2 = Number(6)
# sum =n1+n2
# mul = n1*n2
# print(sum)
# print(mul)




