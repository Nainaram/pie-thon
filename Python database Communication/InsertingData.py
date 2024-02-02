import pymysql
def CreateConn():
    return pymysql.connect(host='localhost', user='root', password='oppoA5S912@', database='Studentinfo')
    
# #create a cursor
# def CreateTable():
#     conn = CreateConn()
#     cursor = conn.cursor()
#     cursor.execute("create table Staff(sid int primary key auto_increment,name VARCHAR(20),email VARCHAR(30),City VARCHAR(30))")
#     #commiting the changes in database
#     conn.commit()
#     conn.close()
#     cursor.close()
# CreateTable()
#Creating a  function that inserts the data into the database
def InsertData(name,email,city):
    conn = CreateConn()#Creating a connection
    cursor = conn.cursor()
    args =  (name,email,city)
    cursor.execute("insert into staff(name,email,city)values(%s,%s,%s)",args)
    conn.commit()#Saving the data using the commit
    print("DATA INSERTED")
    conn.close()
    cursor.close()
n = input("enter the name:")
e = input("enter the email:")
c = input("enter the city:")
InsertData(n,e,c)
 