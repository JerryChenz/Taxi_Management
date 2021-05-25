import mysql.connector
from mysql.connector import Error

mysql_host = '192.168.1.150'
mysql_salesdb = 'salesdb'
mysql_inventorydb = 'inventory'
mysql_user = 'root'
mysql_pw = '62355983'

def get_newpayid():
    try:
        sales_connection = mysql.connector.connect(host=mysql_host,
                                                   user=mysql_user,
                                                   password=mysql_pw,
                                                   database=mysql_salesdb)
        if sales_connection.is_connected():
            cursor = sales_connection.cursor()
            cursor.callproc('`p_new_payment_id`')
            # doc at https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-callproc.html

            for result in cursor.stored_results():
                new_payment_id = "".join(result.fetchone())

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if sales_connection.is_connected():
            cursor.close()
            sales_connection.close()
            print("MySQL connection is closed")
            return new_payment_id

def get_invoiceinfo(driver, work_date):
    try:
        # driver_id, work_date, discount, repair_and_others
        invoice_args = (driver, work_date, 0, 0) # 0 are to hold value of the OUT parameter pProd
        sales_connection = mysql.connector.connect(host=mysql_host,
                                                   user=mysql_user,
                                                   password=mysql_pw,
                                                   database=mysql_salesdb)
        if sales_connection.is_connected():
            cursor = sales_connection.cursor()
            cursor.callproc('`p_invoicedetail`', invoice_args)
            # doc at https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-callproc.html

            for result in cursor.stored_results():
                invoice_args = "".join(result.fetchone())

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if sales_connection.is_connected():
            cursor.close()
            sales_connection.close()
            print("MySQL connection is closed")
            return invoice_args

    def db_insert(payment_object):
        pass
"""
sql_result = get_invoiceinfo('D1', '2021/5/19')
print(sql_result[0])
print(sql_result[1])
print(sql_result[2])
print(sql_result[3])
"""

'''
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
'''