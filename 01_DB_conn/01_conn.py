import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="Himaja",
    password="sravan@12345"
)

print(mydb)

mycursor=mydb.cursor()

#mycursor.execute("CREATE DATABASE mydata")
#mycursor.execute("SHOW DATABASES")

#for x in mycursor:
    #print(x)