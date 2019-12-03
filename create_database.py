import mysql.connector
from mysql.connector import errorcode

config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'password'
}

try:
    conn = mysql.connector.connect(**config)
    print("Connection established")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with the user name or password")
    elif err.errno == errcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS crm;")
print("Finished dropping database (if existed).")

cursor.execute("CREATE DATABASE crm")
print("Finished creating database")

conn.commit()
cursor.close()
conn.close()
print("Done.")
