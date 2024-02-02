#import your database API
# AND create your database connection
import pymysql
def CreateConn():
    return pymysql.connect(host='localhost', user='root', password='oppoA5S912@', database='Studentinfo',autocommit=True)
def ShowAllData():
    conn=CreateConn()
    cursor = conn.cursor()
    cursor.execute("select * from staff")
    result = cursor.fetchall()
    for i in result:
        print(i)
ShowAllData()
def UpdateData(name,email,city,sid):
    conn = CreateConn()
    cursor =conn.cursor()
    args =(name,email,city,sid)
    query = "update staff set name=%s,city=%s,email=%s where sid =%s"
    cursor.execute(query,args)
    conn.commit()
    print("Data Updated")
    conn.close()
    cursor.close()
ShowAllData()

sid = int(input("enter the staff id:"))
n = input("enter the name:")
e = input("enter the email:")
c = input("enter the city:")

UpdateData(n,e,c,sid)
ShowAllData()
