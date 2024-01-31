#METHOD OVERLOADING IS NOT POSSIBLE IN  PYTHON BECAUSE IT IS A INTERPRETED LANGUAGE
#see how
# class myclass:
#     def sum(self):
#         print("This performs the sum")
#     def sum(self,a,b):
#         return a+b
#     def sum(self,a,b,c):
#         return a+b+c
# obj = myclass()
# # obj.sum()
# # sum =obj.sum(2,3)
# print(sum)
# print(obj.sum(2,3,4))
#method overriding
class myclassA:
    def sum(self,a):
       print("this is the A")
class myclassB(myclassA):
    def sum(self,a):
        print("this is the b")
        super().sum(2)
class myclassC(myclassB):
     def sum(self,a):
        print("this is c")
obj = myclassC()

obj.sum(2)
