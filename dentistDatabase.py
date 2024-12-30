import mysql.connector as mysql

#variables
host = "localhost"
user = "root"
password = ""

try:
    db = mysql.connect(host=host,user=user,password=password)
    print("Connected Successfully")
except Exception as e:
    print(e)
    print("Failed to connect")

#Connecting to mysql
try:
    command_handler = db.cursor()
    command_handler.execute("CREATE DATABASE SmileDatabase")
    print("Dentist database has been created")
except Exception as e:
    print("Could not create database")
    print(e)
    
