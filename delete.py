import mysql.connector
from mysql.connector import errorcode

config = {
    'host': '127.0.0.1',
    'user': 'root',
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

cursor.execute("DELETE FROM user WHERE name=%(name)s;", {'name': "test2"})
print("Deleted", cursor.rowcount, "row(s) of data.")

conn.commit()
cursor.close()
conn.close()
print("Done.")

