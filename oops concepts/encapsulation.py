class A :
    def __init__(self,a):
        self.__a=a # this is the variable(private)
    def show(self):
        print("the private variable:" , self.__a)
class B(A):
    def __init__(self,b):
        super().__init__(b)
    def showB(self):
        print(self.__a)
obj = B(20)
obj.showB()
# class A :
#     def __init__(self,a):
#         self._a=a # this is the variable(protected) this value can be accessed by other classes too
#     def show(self):
#         print("the private variable:" , self._a)
# class B(A):
#     def __init__(self,b):
#         super().__init__(b)
#     def showB(self):
#         print(self._a)
# obj = B(20)
# obj.showB()