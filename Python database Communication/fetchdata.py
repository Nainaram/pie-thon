import pymysql
def CreateConn():
    return pymysql.connect(host='localhost', user='root', password='oppoA5S912@', database='Studentinfo',autocommit=True)
#Creating a ShowAll data function to fetch the data from the database
def ShowAllData():
    conn=CreateConn()
    cursor = conn.cursor()
    cursor.execute("select * from staff")
    result = cursor.fetchall()
    for i in result:
        print(i)

ShowAllData()