import pymysql
def CreateConn():
    return pymysql.connect(host='localhost', user='root', password='oppoA5S912@', database='Studentinfo',autocommit=True)
#Creating a ShowAll data function to fetch the data from the database
def ShowAllDatabyId(sid):
    conn=CreateConn()
    cursor = conn.cursor()
    args = (sid)
    cursor.execute("select * from staff where sid = %s",args)
    result = cursor.fetchall()
    for i in result:
        print(i)


sid = int(input("Enter the student id:"))
ShowAllDatabyId(sid)