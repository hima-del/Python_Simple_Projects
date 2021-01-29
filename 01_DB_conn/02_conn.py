import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="Himaja",
    password="sravan@12345",
    database="mydatabase"
)

mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255)")