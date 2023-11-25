class Person:
    country = "India"
    def __init__(self):
         print("Intializing Person..\n")
    
    def takeBreak(self):
        print("I am Breathing...")

class Employee(Person):
    company = "Honda"

    def __init__(self):
         super().__init__()
         print("Initializing Employee...\n")

    def getSalary(self):
        print(f"Salary is{self.salary}")

    def takeBreak(self):
        super().takeBreak()
        print("I am an employee so I am luckily breathing..")

class Programmer(Employee):
    company = "Fiverr"

    def __init__(self):
         super().__init__()
         print("Initializing Programmer..\n")

    def getSalary(self):
        print(f"No salary to programmers")

    def takeBreak(self):
            super().takeBreak()
            print("I am an pagal so I am luckily breathing..")

# p = Person()
# p.takeBreak()
# print(p.company) #throws an error
# e = Employee()
# e.takeBreak()
# print(e.company)
pr = Programmer()
# pr.takeBreak()     
# print(pr.company)
# print(pr.country)       