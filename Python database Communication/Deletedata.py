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

def DeleteData(sid):
    conn = CreateConn()
    cursor =conn.cursor()
    query = "delete from staff where sid=%s"
    cursor.execute(query,sid)
    conn.commit()
    print("Deleted the data")
    conn.close()
    cursor.close()
ShowAllData()

sid=int(input("enter the staff id:"))
DeleteData(sid)
ShowAllData()
 