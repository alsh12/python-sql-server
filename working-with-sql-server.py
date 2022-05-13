#This is sample example to connect Microsoft SQL Server with Python using pyodbc

import pyodbc


conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=yourservername;" 
                      "Database=yourdatabasename;"
                      'User Id=yourdbuserid;'
                      'Password=yourdbpassword;'
                      "Trusted_Connection=yes;")


cursor = conn.cursor()
cursor.execute('SELECT * from User')

for i in cursor:
    print(i)