# this is the program for debugging process as your  two operands are 
# gettin from the random library so it might consist of bug so as of mine there is no bugs in this program and it is clear program.
import random
def generaterandom(upper):
    r = random.randint(1,upper)
    return r
def main():
    program=True
    num1 = generaterandom(20)
    num2 = generaterandom(10)
    result = num1*num2
    while program:
        ans = input(" what is "+ str(num1) + "x" + str(num2) +" = ")
        if ans.isdigit():
            if int(ans)==result:
                print("Correct")
                program= False
            else:
                print("Inaccurate")
        else:
            print("Answer must be positive!!!")
            
x =10
for x in range(x):
    main()