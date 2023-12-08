#we are gonnna create a functin aand we call it 
students = { '1': {'name': 'Bob', 'grade': 2.5},
        '2': {'name': 'Mary', 'grade': 3.5},
        '3': {'name': 'David', 'grade': 4.2},
        '4': {'name': 'John', 'grade': 4.1},       
        '5': {'name': 'Alex', 'grade': 3.8}}
def averageGrade(students):
    #This function computes the average grade”
     sum = 0.0 
     for key in students: 
        sum = sum + students[key]['grade'] 
        average = sum/len(students) 
        return average
avg = averageGrade(students)
print ("The average garde is: %0.2f" % (avg))

def displayFruits(fruits=["apple","orange"]): 
    print ("There are %d fruits in the list" % (len(fruits)) )
    for item in fruits:
         print (item)
#Using default arguments
displayFruits()

fruits = ["banana", "pear", "mango"]
displayFruits(fruits) 
#passing by reference
def displayFruits(fruits):
    print ("There are %d fruits in the list" % (len(fruits)))
    for item in fruits:
        if(len(item)== 3):
            print (item )
        print("Adding one more fruit" ,fruits.append('mango'))
        break
fruits = ['banana', 'pear', 'apple']
displayFruits(fruits)
#Adding one more fruit
print( "There are %d fruits in the list" % (len(fruits)))
print(fruits)
#keyword reference
def student(name, **kwargs):
            print ("Student Name: " + name  )
            for key in kwargs:    
                print (key + ": " + kwargs[key])
#calling the function
student(name="kiran",age ="23",place ="lolom")
    
def printStudentRecords(name,age=20,major="CS"):
    print("Name: " + name )
    print ("Age: " + str(age) )
    print( "Major: " + major)

result = printStudentRecords("ram")


