#Inheritance means taking a  properties of another class into another class
#Different types single inheritance,multilevel inheritance
# multiple inheritance,hierarical inheritance, hybrid inheritance
# #SINGLE INHERITANCE
# class Parent:
#     def ParentFunc(self):
#         print("this is the parent class")
# class Child(Parent):
#     def ChildFunc(self):
#         print("this is the child class")
# obj = Child()
# obj.ParentFunc()
# obj.ChildFunc()
#MULTILEVEL INHERITANCE
# class A:
#     def parentFunc(self):
#         print("this is the A")
# class B(A):
#     def childFunc(self):
#         print("this is  the B")
# class C(B):
#     def child(self):
#         print("this is c child")
# obj = C()
# obj.parentFunc()
# obj.childFunc()
# obj.child()
#MULTIPLE INHERITANCE
# class A:
#     def parentFuncA(self):
#         print("this is the A")
# class B:
#     def parentFuncB(self):
#         print("this is  the B")
# class C(A,B):
#     def child(self):
#         print("this is c child")
# obj = C()
# obj.parentFuncA()
# obj.parentFuncB()
# obj.child()
#Hierarchical inheritance
# class A:
#     def parentFuncA(self):
#         print("this is the A")
# class B(A):
#     def ChildB(self):
#         print("this is  the B")
# class C(A):
#     def childC(self):
#         print("this is c child")
# obj = C()
# OBJ = B()
# obj.parentFuncA()
# obj.childC()
# OBJ.parentFuncA()
# OBJ.ChildB()
class A :
    def A(self):
        print("This is A")
class B(A) :
    def B(self):
        print("This is B")
class C(A) :
    def C(self):
        print("This is C")
class D(B,C) :
    def D(self):
        print("This is D")
OBJ = D()
OBJ.A()
OBJ.B()
OBJ.C()
OBJ.D()