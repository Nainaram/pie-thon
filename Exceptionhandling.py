#Abnormal situation occur at runtime and stop  the execution of program is called Exception
#two types of error 1.syntax error 2.exception
# syntax error  is also a syntax error
#exception handling  is syntactically correct but code results in error
#user Exception means user generates his custom exception in python in inherited the exception class
# try:
# #the code which is written in try block  can be occur error at runtime
#     a = int(input("Enter the value of A:"))
#     b = int(input("Enter the value of B:"))
#     c = a/b
#     print(c)
# except Exception as e: 
#     #this block will run when  exception occur
#     print("Exception caught: ",e)
# print("BYE") 
# try:
#     x=0
#     print(x/0)
# except NameError:
#     print("variable is not defined")
# except :
#     print("Exception caught")
# print("bye")

# try:
#     x=6
#     print(x)
# except:
#     print("something went wrong")
# else:
#     print("Nothing happened")
# finally:# this will executed every time  if error occur or not 
#     print("work done!!")
# user defined exception can be created  by user 
class MyException(Exception):
    pass

c = 23
if c>4:
    raise MyException("Something went wrong")