import mysql.connector
from mysql.connector import Error

MYSQL_HOST = '192.168.1.150'
MYSQL_SALES = 'salesdb'
MYSQL_INVENTORY = 'inventory'
MYSQL_USER = 'root'
MYSQL_PW = '62355983'

def get_newpayid():
    try:
        sales_connection = mysql.connector.connect(host=MYSQL_HOST,
                                                   user=MYSQL_USER,
                                                   password=MYSQL_PW,
                                                   database=MYSQL_SALES)
        if sales_connection.is_connected():
            cursor = sales_connection.cursor()
            cursor.callproc('`p_new_payment_id`')
            # doc at https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-callproc.html

            for result in cursor.stored_results():
                new_payment_id = "".join(result.fetchone())

    except Error as e:
        print("Failed to execute stored procedure: {}".format(e))
    finally:
        if sales_connection.is_connected():
            cursor.close()
            sales_connection.close()
            print("MySQL connection is closed")
            return new_payment_id

def get_invoiceinfo(driver, work_date):
    try:
        # driver_id, work_date, discount, repair_and_others
        invoice_args = [] # 0 are to hold value of the OUT parameter pProd
        sales_connection = mysql.connector.connect(host=MYSQL_HOST,
                                                   user=MYSQL_USER,
                                                   password=MYSQL_PW,
                                                   database=MYSQL_SALES)
        if sales_connection.is_connected():
            cursor = sales_connection.cursor()
            cursor.callproc('`p_invoicedetail`', [driver, work_date,])
            # doc at https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-callproc.html

            for result in cursor.stored_results():
                rlist = result.fetchone()
                invoice_args.append(rlist[0])
                invoice_args.append(rlist[1])

    except Error as e:
        print("Failed to execute stored procedure: {}".format(e))
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