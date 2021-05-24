import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from hanson_db import mysql_host, mysql_salesdb, mysql_user, mysql_pw
import mysql.connector
from mysql.connector import Error
from datetime import datetime
from payment import Payment, deposit_only

class AddPayment(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the addPayment window
        self.title('Add_payment')
        self.iconbitmap('Z:\Taxi Management System\system_files\icons\payment.ico')
        self.geometry("1000x500")

        self.isDeposit = tk.IntVar()  # value to identify if the payment is a deposit only
        self.payId = self.get_newPayId()

        # label
        self.win_label = ttk.Label(self, text="Please enter new payments")
        self.drive_id_label = ttk.Label(self, text="driver_id:")
        self.newPayId_label = ttk.Label(self, text="payment_id:")
        self.newPayId_value_label = ttk.Label(self, text=self.payId)
        self.paidFrom_label = ttk.Label(self, text="Paid_from:")
        self.paidTo_label = ttk.Label(self, text="Paid_from:")
        self.paymentDate_label = ttk.Label(self, text="payment_date:")
        self.amountPaid_label = ttk.Label(self, text="amount_paid:")
        self.receivingBank_label = ttk.Label(self, text="receiving_bank:")
        self.col2Space_label = ttk.Label(self, text="    ").grid(row=0, column=2)
        self.col5Space_label = ttk.Label(self, text="    ").grid(row=0, column=5)

        # Entry
        self.driverId_input = ttk.Entry(self, width=12)
        self.paidFrom_input = ttk.Entry(self, width=12)
        self.paidFrom_input.insert(0, datetime.today().strftime('%Y-%m-%d'))
        self.paidTo_input = ttk.Entry(self, width=12)
        self.paidTo_input.insert(0, "yyyy-mm-dd")
        self.paymentDate_input = ttk.Entry(self, width=12)
        self.paymentDate_input.insert(0, "yyyy-mm-dd")
        self.amountPaid_input = ttk.Entry(self, width=12)
        self.receivingBank_input = ttk.Entry(self, width=12)

        # Radio Button
        self.DepositOnly_button = ttk.Radiobutton(self, text="Deposit Only", variable=self.isDeposit, value=1)
        self.notDeposit_button = ttk.Radiobutton(self, text="Not just Deposit", variable=self.isDeposit, value=2)

        # Button
        self.insert_button = ttk.Button(self, text="Ok")
        self.insert_button['command'] = self.button_okClick
        self.exit_button = ttk.Button(self, text="Exit", command=self.quit)

        # Grid
        self.win_label.grid(row=0, column=0)
        self.drive_id_label.grid(row=1, column=0)
        self.driverId_input.grid(row=1, column=1)
        self.newPayId_label.grid(row=1, column=3)
        self.newPayId_value_label.grid(row=1, column=4)
        self.paidFrom_label.grid(row=2, column=0)
        self.paidFrom_input.grid(row=2, column=1)
        self.paidTo_label.grid(row=2, column=3)
        self.paidTo_input.grid(row=2, column=4)
        self.paymentDate_label.grid(row=3, column=0)
        self.paymentDate_input.grid(row=3, column=1)
        self.receivingBank_label.grid(row=3, column=3)
        self.receivingBank_input.grid(row=3, column=4)
        self.amountPaid_label.grid(row=4, column=0)
        self.amountPaid_input.grid(row=4, column=1)

        self.DepositOnly_button.grid(row=5, column=0)  # todo: add a condition to check if paid_to is entered
        self.notDeposit_button.grid(row=5, column=3)

        self.insert_button.grid(row=10, column=3)
        self.exit_button.grid(row=10, column=4)


    def button_okClick(self):
        response = messagebox.askokcancel("Are you sure?", "It is ok to insert?")
        self.answer = ttk.Label(self, text="")
        if response == True:
            try:
                print(self.driverId_input.get())
                print(datetime.strptime(self.paidFrom_input.get(), '%Y-%m-%d'))
                print(datetime.strptime(self.paidTo_input.get(), '%Y-%m-%d'))
                print(datetime.strptime(self.paymentDate_input.get(), '%Y-%m-%d'))
                print(float(self.amountPaid_input.get()))
                print(self.receivingBank_input)
                self.answer.config(text="new payment added!")
            except ValueError as e:
                self.answer.config(text= "invalid input")
        else:
            self.answer.config(text="operation canceled!")
        self.answer.grid(row=10, column=0)

    def get_newPayId(self):
        try:
            salesdb_connection = mysql.connector.connect(host=mysql_host,
                                                         user=mysql_user,
                                                         password=mysql_pw,
                                                         database=mysql_salesdb)
            if salesdb_connection.is_connected():
                cursor = salesdb_connection.cursor()
                cursor.callproc('`p_new_payment_id`')

                for result in cursor.stored_results():
                    new_payment_id = "".join(result.fetchone())

        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if salesdb_connection.is_connected():
                cursor.close()
                salesdb_connection.close()
                print("MySQL connection is closed")
                return new_payment_id

    def db_insert(self):
        pass




