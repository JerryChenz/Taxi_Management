import mysql.connector
from mysql.connector import Error

mysql_host = '192.168.1.150'
mysql_salesdb = 'salesdb'
mysql_inventorydb = 'inventory'
mysql_user = 'root'
mysql_pw = '62355983'

try:
    connection = mysql.connector.connect(host=mysql_host,
                                         database=mysql_salesdb,
                                         user=mysql_user,
                                         password=mysql_pw)
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
