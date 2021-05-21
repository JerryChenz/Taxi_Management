from tkinter import *
from tkinter import messagebox
from hanson_db import mysql_host, mysql_salesdb, mysql_user, mysql_pw
import mysql.connector
from mysql.connector import Error
from datetime import datetime
from payment import Payment, Deposit

addPayment_win = Tk()
addPayment_win.title('Add_payment')
addPayment_win.iconbitmap('Z:\Taxi Management System\system_files\icons\payment.ico')

# value to identify if the payment is a deposit only
isDeposit = IntVar()

def okClick():
    response = messagebox.askokcancel("Are you sure?", "It is ok to insert?")
    if response == True:
        successLabel = Label(addPayment_win, text="new payment added!")
    else:
        successLabel = Label(addPayment_win, text="operation canceled!")
    successLabel.grid(row=10, column=0)

def setPayment():
    pass

def db_insert():
    try:
        salesdb_connection = mysql.connector.connect(host=mysql_host,
                                             user=mysql_user,
                                             password=mysql_pw,
                                             database=mysql_salesdb)
        if salesdb_connection.is_connected():
            cursor = salesdb_connection.cursor()
            cursor.execute("Select * From payments Where driver_id = 'D1'")

            driver_result = cursor.fetchall()

            for x in driver_result:
                print(x)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if salesdb_connection.is_connected():
            cursor.close()
            salesdb_connection.close()
            print("MySQL connection is closed")



win_label = Label(addPayment_win, text="Please enter new payments")
drive_id_label = Label(addPayment_win, text="driver_id:")
newPayId_label = Label(addPayment_win, text="payment_id:") #todo: get new pay id
paidFrom_label = Label(addPayment_win, text="Paid_from:")
paidTo_label = Label(addPayment_win, text="Paid_from:")
paymentDate_label = Label(addPayment_win, text="payment_date:")
amountPaid_label = Label(addPayment_win, text="payment_date:")
receivingBank_label = Label(addPayment_win, text="payment_date:")
col2Space_label = Label(addPayment_win, text="    ").grid(row=0, column=2)
col5Space_label = Label(addPayment_win, text="    ").grid(row=0, column=5)


driverId_input = Entry(addPayment_win, width=10)
paidFrom_input = Entry(addPayment_win, width=10)
paidTo_input = Entry(addPayment_win, width=10)
paymentDate_input = Entry(addPayment_win, width=10)
amountPaid_input = Entry(addPayment_win, width=10)
receivingBank_input = Entry(addPayment_win, width=10)

paidFrom_input.insert(0, datetime.today().strftime('%Y-%m-%d'))
paidTo_input.insert(0, "yyyy-mm-dd")
paymentDate_input.insert(0, "yyyy-mm-dd")

DepositOnly_button = Radiobutton(addPayment_win, text="Deposit Only", variable=isDeposit, value=1)
notDeposit_button = Radiobutton(addPayment_win, text="Not just Deposit", variable=isDeposit, value=2)

insert_button = Button(addPayment_win, text="Ok", command=okClick, fg="green")
exit_button = Button(addPayment_win, text="Exit", command=addPayment_win.quit)

# addPayment_win.pack()
win_label.grid(row=0, column=0)
drive_id_label.grid(row=1, column=0)
driverId_input.grid(row=1, column=1)
newPayId_label.grid(row=1, column=3)
paidFrom_label.grid(row=2, column=0)
paidFrom_input.grid(row=2, column=1)
paidTo_label.grid(row=2, column=3)
paidTo_input.grid(row=2, column=4)
paymentDate_label.grid(row=3, column=0)
paymentDate_input.grid(row=3, column=1)
receivingBank_label.grid(row=3, column=3)
receivingBank_input.grid(row=3, column=4)
amountPaid_label.grid(row=4, column=0)
amountPaid_input.grid(row=4, column=1)

DepositOnly_button.grid(row=5, column=0) #todo: add a condition to check if paid_to is entered
notDeposit_button.grid(row=5, column=3)

insert_button.grid(row=10, column=3)
exit_button.grid(row=10, column=4)

addPayment_win.mainloop()