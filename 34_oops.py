# 1
class Numbers:
    def sum(self):
        return self.a + self.b
    
num = Numbers()
num.a =4
num.b =5
s = num.sum()
print(s)

# 2
    class RailwayForm:
        formType = "RailwayForm"
        def printData(self):
            print(f"Name is {self.name}")
            print(f"Train is {self.train}")

aksapplication = RailwayForm()
aksapplication.name = "AK"
aksapplication.train = "Rajdhani Express"
aksapplication.printData()


# 3
class Remote():
    pass
class Player:
    def moveRight(self):
        pass
    def moveLeftt(self):
        pass
    def moveForward(self):
        pass

remote1 = Remote()
player1 = Player()

if(remote1.isLeftPressed()):
    player1.moveLeft    


# 4
class Employee:
    company = "Google"
    salary = 100    
AK = Employee()
RK = Employee()
AK.salary = 793
RK.salary =43074
print(AK.company)
print(RK.company)
Employee.company = "YouTube"
print(AK.company)
print(RK.company)
print(AK.salary)
print(RK.salary)
# belowlibne throws an error as address line is not present in class
print(AK.address)


# 5
class Employee:
    company ="Google"
    def getSalary(self, signature):
        print(f"Salary for this employee workingin {self.company} is {self.salary}\n {signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir") 

    @staticmethod
    def time():
        print("Time is 9AM")            
AK = Employee()
AK.salary =10000
AK.getSalary("Thanks!")
AK.greet() 
AK.time()  
# Employee.getSalary(AK)   

# 6
class Employee:
    company ="Google"
    def __init__(self, name, salary,subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("employee is created!")

    def getDetails(self):
        print(f"The name of the employee{self.name}")
        print(f"The salary of the employee{self.salary}")
        print(f"The employer of the employee{self.subunit}")
    def getSalary(self, signature):
        print(f"Salary for this employee workingin {self.company} is {self.salary}\n {signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir") 

    @staticmethod
    def time():
        print("Time is 9AM")    

AK = Employee("AK", 746, "XYZ")  
# AK = Employee()#this throws an error arguments:
AK.getDetails()        
