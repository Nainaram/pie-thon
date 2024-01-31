# Classes are created by using the keyword class
# Creating an empty string in Python
class Dog:
    tail = 1# this variable is also a property of a class
# AN Object is the anything any real world entitity like a chair, car , dog  and in oops concepts everything is object
# object having states i.,e properties of an object
# creating an object
obj = Dog()# this is the obj  and with out this you cannot access the any property of class
print(obj.tail)
# calling a function through the obj 
class CallFunction:
    def CallFunction(self):
        print("hi, i'm a function")
obj1= CallFunction()
obj1.CallFunction()
#How to create a constructor
class MyConstructor:
    # creating a MyConstructor
    def __init__(self,name,age):
       self.name = name
       self.age = age
    def myfunction(self):
        print("My name is :"+self.name)
#creating an object for the class
m1 = MyConstructor("ram",21)

# we can manipulate the data as per need 
m1.age  = 22
print(m1.name)
print(m1.age)
#deleting the obj
del m1.age
print(m1.age)
