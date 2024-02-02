import pymysql

# Assuming you have a connection already established
connection = pymysql.connect(host='localhost', user='root', password='oppoA5S912@', database='Studentinfo')

# Create a cursor
cursor = connection.cursor()

# Execute the DROP TABLE query
cursor.execute('create table employee(sid int primary key auto_increment,name VARCHAR(20),email VARCHAR(30),City VARCHAR(30))')
# cursor.execute("Drop table if Exists student")
# Commit the changes to the database
connection.commit()

# Close the cursor and connection when done
cursor.close()
connection.close()
