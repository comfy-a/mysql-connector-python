import mysql.connector
from mysql.connector import errorcode

config = {
    'host': '127.0.0.1',
    'user': 'user',
    'password': 'password',
    'database': 'crm'
}

try:
    conn = mysql.connector.connect(**config)
    print("Connection established")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with the user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cursor = conn.cursor()

cursor.execute("SELECT * FROM user;")
rows = cursor.fetchall()
print("Read", cursor.rowcount, "row(s) of data.")

for row in rows:
    print("Data row = (%s, %s, %s, %s)" %(row[0], row[1], row[2], row[3]))

conn.commit()
cursor.close()
conn.close()
print("Done.")

