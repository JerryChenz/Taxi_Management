import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='192.168.1.150',
                                         database='salesdb',
                                         user='root',
                                         password='62355983')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

        cursor.execute("Select * From payments Where driver_id = 'D1'")

        driver_result = cursor.fetchall()

        for x in driver_result:
            print(x)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
