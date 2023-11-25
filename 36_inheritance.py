# single inheritance
class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):
    language = "Python"
    company ="youtube"
    def getlanguage(self):
        print(f"The language is{self.language}")


    def showDetails(self):
        print("This is an programmer")

e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
print(p.company)


# multiple inheritance

class Employee:
    company = "Visa"
    ecode =120

class Freelancer:
    company = "Fiverr"
    level =2

    def upgradeLevel(self):
        self.level = self.level +1

class Program(Employee, Freelancer):
    name = "Rohit"

p = Program()  
p.upgradeLevel()
print(p.company)    


# multilevelinheritance

class Person:
    country = "India"
    def takeBreak(self):
        print("I am Breathing...")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is{self.salary}")

    def takeBreak(self):
        print("I am an employee so I am luckily breathing..")

class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print(f"No salary to programmers")

    def takeBreak(self):
            print("I am an pagal so I am luckily breathing..")

p = Person()
p.takeBreak()
# print(p.company) #throws an error
e = Employee()
e.takeBreak()
print(e.company)
pr = Programmer()
pr.takeBreak()     
print(pr.company)
print(pr.country)       
          


