import mysql.connector

cnx = mysql.connector.connect(
    user='username',
    password='password',
    host='sql-instance-ip',
    database='sample_db'
)
cursor = cnx.cursor()
cursor.execute('SELECT * FROM users')
for row in cursor:
    print(row)
cursor.close()
cnx.close()
