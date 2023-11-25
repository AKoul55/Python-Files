# 1
class C2dVec:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"
    
    
class C3dVec(C2dVec):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

v2d = C2dVec(1, 3)
v3d = C3dVec(1,9,7)
print(v2d)
print(v3d)


# 2
class Animals:
    animalType = "Mammal"

class Pets:
    color = "White"

class Dog:
    @staticmethod
    def bark(): 
        print("wuf wuf!")   

d = Dog()     
d.bark()       


# 3
class Employee:
    salary = 200
    increment = 2.4

    @property
    def salaryafterincrement(self):
        return self.salary*self.increment
    
    @salaryafterincrement.setter
    def salaryafterincrement(self, sai):
        self.increment = sai/self.salary

e = Employee()   
print(e.salaryafterincrement)

print(e.increment)
e.salaryafterincrement = 400
print(e.increment)     


# 4
# (a+bi)(c+di) = (ac-bd) + (ad+bc)i
class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i
    def __add__(self, c):
        return Complex(self.real + c.real, self.imaginary +c.imaginary)
    def __mul__(self, c):
        mulReal = self.real*c.real - self.imaginary*c.imaginary
        mulImg = self.real*c.imaginary + self.imaginary*c.real
        return Complex(mulReal, mulImg)
    def __str__(self):
        if self.imaginary<0:
            return f"{self.real} - {-self.imaginary}i"
        else:
            return f"{self.real} + {self.imaginary}"
        # return f"{self.real} + {self.imaginary}i"    
    
c1 = Complex(3,2)
c2 = Complex(1,7)
print(c1 + c2)    
print(c1 * c2)


# 5
class vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self): 
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index +=1
        return str1[:-1]   
    
    def __add__(self, vec2):
        newList = []
        for i in range (len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return vector(newList)
    
    def __mul__(self, vec2):
        sum = 0
        for i in range (len(self.vec)):
           sum += (self.vec[i] + vec2.vec[i])
        return sum

v1 = vector([1 ,4])
v2 = vector([5, 6])   
print(v1+v2)    
print(v1*v2) 



# 6

class vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self): 
      return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"

v1 = vector([1 ,4, 7])
v2 = vector([5, 6, 9])   
print(v1)    
print(v2) 

# 7
    
class vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self): 
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index +=1
        return str1[:-1]   
    
    def __add__(self, vec2):
        newList = []
        for i in range (len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return vector(newList)
    
    def __mul__(self, vec2):
        sum = 0
        for i in range (len(self.vec)):
           sum += (self.vec[i] + vec2.vec[i])
        return sum
    
    def __len__(self):
        return len(self.vec)

v1 = vector([1 ,4])
v2 = vector([5, 6])   
print(len(v1))    
print(len(v2)) 



