import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'pass1234'
)

#prepare a cursor object
cursorObject = dataBase.cursor()

#Crete a database

cursorObject.execute('CREATE DATABASE nigus')

print('all done')