import mysql.connector
conn = mysql.connector.connect(host='localhost', password = 'admin@123', user='root')

if conn.is_connected():
    print("connected")