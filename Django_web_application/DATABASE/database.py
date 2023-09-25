# import mysql.connector
# mydb=mysql.connector.connect(
#     host="localhost",
#     username="root",
#     port='3306',
# )
# mycursor=mydb.cursor()
# mycursor.execute("CREATE DATABASE django_web_application")





import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="django_web_application"
)

mycursor = mydb.cursor()
