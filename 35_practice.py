# 1
class Programmer:
    company = "Microsoft"
    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
            print(f"The name of the {self.company} programmer is\{self.name} and the product is {self.product}")

AK = Programmer("AK","Wipro")   
RK = Programmer("AK", "Hitachi")  
AK.getInfo()   


# 2
class calculator:
     def __init__(self, num):
          self.num =num
     def square(self):
      print(f"The value of {self.num} square is {self.num **2}")
     def squareRoot(self):
      print(f"The value of {self.num} squareroot is {self.num **0.5}")
     def cube(self):
      print(f"The value of {self.num} cube is {self.num **3}")
   
     @staticmethod
     def greet():
         print("Hello to the finest Cal C")
a=calculator(3)
a.greet()
a.square()
a.squareRoot()
a.cube()

# 3
class Sample:
    a ="AK"
    def __init__(AK, name):
        AK.name = name
obj = Sample("AK")
print(Sample.a)


# 4
class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats
    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}")

    def fareInfo(self):
        print(f"The price of the ticket is : Rs {self.fare}") 

    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked! Your seat number is{self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry thie trai is full! Kindly try in Tatakal")

    def cancelTicket(self, seatNo):
            self.seats = self.seats + 1


intercity = Train("Intercity Express: 14015", 90, 1)
intercity.getStatus()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()
intercity.fareInfo()


# 5
     