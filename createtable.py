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
    elif err.errno == errcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS user;")
print("Finished dropping table (if existed).")

cursor.execute("CREATE TABLE user (id serial PRIMARY KEY, name VARCHAR(20) NOT NULL, age INTEGER NOT NULL, gender VARCHAR(4) NOT NULL);")
print("Finished creating table")

cursor.execute("INSERT INTO user (name, age, gender) VALUES (%s, %s, %s);", ("test1", 31, "남자"))
print("Inserted", cursor.rowcount, "row(s) of data.")
cursor.execute("INSERT INTO user (name, age, gender) VALUES (%s, %s, %s);", ("test2", 32, "여자"))
print("Inserted", cursor.rowcount, "row(s) of data.")

conn.commit()
cursor.close()
conn.close()
print("Done.")
