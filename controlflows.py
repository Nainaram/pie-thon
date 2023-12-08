# this file includes all the control flows statements
# a = int(input(" Enter the value of the a:"))
# if( a > 10000):
#     print(" yes a is greated value" + str(a))
# else:
#     print("no this is not sufficient value" + str(a))
    
#nested if esle
# a = int(input(" Enter the value for a:"))
# b = int(input("Enter the second value b:"))
# if(a == b):
#     if(a<=100000):
#         print(" it is in between 10000 and 100000")
#     elif(a<50000):
#         print(" it is in between 10000  and 50000")
#     else:
#         print(a)
# else:
#     print("please enter the sufficient value")
# student = {"name":"ram",'age':21}
# for i in student:
#     print(student)
fruits = ["apple","carrot","veggie"]
i = 1
for item in fruits:
    print ("Fruit-%d:%s" %(i,item) )
    i=i+1
student ={"naam":"ram","age":21,"place":"india"}
for keys in student:
    print("keys -%s:%s" %(keys,student[keys]))
    #while loop 
i = 0
while i <= 100:
    if(i%2==0):
        print (i)
    i=i+1
    if(i == 98):
            break
ii =0
while(ii <=110):
    print(ii)
    ii = ii+10
    fruits2=["apple","orange","banana","mango"] 
for item in fruits2: 
    if item == "banana":
        pass
else: print (item)


        
    
    

    