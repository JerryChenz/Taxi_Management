import mysql.connector
from mysql.connector import Error
from hanson_db import MYSQL_HOST, MYSQL_SALES, MYSQL_USER, MYSQL_PW

class Payment:
    # non scheduled deposit #todo change
    # scheduled payment

    def __init__(self, d_Id, pay_Id, pay_Date, pFrom, pTo, paid, bank, discount, repair, notes):
        self.driverId = d_Id
        self.paymentId = pay_Id
        self.paymentDate = pay_Date
        self.paidFrom = pFrom
        self.paidTo = pTo
        self.amountPaid = paid
        self.recevingBank = bank
        self.discount = discount
        self.repair = repair
        self.notes = notes

    def __str__(self):
        return f'payment({self.driverId},{self.paymentId},{self.paymentDate},{self.paidFrom},{self.paidTo},' \
               f'{self.amountPaid},{self.recevingBank},{self.discount},{self.repair},{self.notes})'

    def insert_payment(self):
        try:
            # driver_id, work_date, discount, repair_and_others
            invoice_args = []  # 0 are to hold value of the OUT parameter pProd
            sales_connection = mysql.connector.connect(host=MYSQL_HOST,
                                                       user=MYSQL_USER,
                                                       password=MYSQL_PW,
                                                       database=MYSQL_SALES)
            if sales_connection.is_connected():
                cursor = sales_connection.cursor()
                cursor.callproc('insert_new_payment', (self.driverId, self.paidFrom, self.paidTo, self.paymentId,
                                                       self.paymentDate, self.amountPaid, self.recevingBank,
                                                       self.notes, self.discount, self.repair))
                sales_connection.commit()
                # doc at https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-callproc.html
                print('successfully inserted payment')
        except Error as e:
            print("Failed to execute stored procedure: {}".format(e))
        finally:
            if sales_connection.is_connected():
                cursor.close()
                sales_connection.close()
                print("MySQL connection is closed")


class DepositOnly(Payment):
    def __init__(self, d_Id, pay_Id, pay_Date, paid, bank, notes):
        self.driverId = d_Id
        self.paymentId = pay_Id
        self.paymentDate = pay_Date
        self.amountPaid = paid
        self.recevingBank = bank
        self.notes = notes

    def __str__(self):
        return f'Deposit({self.driverId},{self.paymentId},{self.paymentDate},{self.amountPaid},{self.recevingBank},' \
               f'{self.notes})'

    def insert_deposit(self):
        try:
            # driver_id, work_date, discount, repair_and_others
            invoice_args = []  # 0 are to hold value of the OUT parameter pProd
            sales_connection = mysql.connector.connect(host=MYSQL_HOST,
                                                       user=MYSQL_USER,
                                                       password=MYSQL_PW,
                                                       database=MYSQL_SALES)
            if sales_connection.is_connected():
                cursor = sales_connection.cursor()
                cursor.callproc('insert_new_deposit', (self.driverId, self.paymentId, self.paymentDate, self.amountPaid,
                                                       self.recevingBank, self.notes))
                sales_connection.commit()
                # doc at https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-callproc.html
                print('successfully inserted deposit')
        except Error as e:
            print("Failed to execute stored procedure: {}".format(e))
        finally:
            if sales_connection.is_connected():
                cursor.close()
                sales_connection.close()
                print("MySQL connection is closed")