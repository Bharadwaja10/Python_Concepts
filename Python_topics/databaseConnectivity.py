import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="967679"
)

mycursor=mydb.cursor()

# Write the query according to your database
query="SELECT * FROM demo1.esd where Age=59"

mycursor.execute(query)

myresult=mycursor.fetchall()

for x in myresult:
    print(x)

mydb.close()