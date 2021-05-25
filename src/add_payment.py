import tkinter as tk
from tkinter import messagebox
from hanson_db import get_newpayid, get_lastpaid
from datetime import datetime
from payment import Payment, DepositOnly

class AddPayment(tk.Tk):
    """add payment
        mandatory parameters:
            driver_id, payment_date, amount_paid, receiving_bank
        Scenario 1:
        new payment with paid_from, paid_to. Optionally(DB Update on daily_invoice) with discount, repair
        Scenario 2:
        deposit only. It requires an insertion of a respective deposit invoice to daily_invoice table.
    """

    def __init__(self):
        super().__init__()

        # configure the addPayment window
        self.title('Add_payment')
        self.iconbitmap('Z:\Taxi Management System\system_files\icons\payment.ico')
        self.geometry("500x200")

        self.isDeposit = tk.IntVar()  # value to identify if the payment is a deposit only
        self.payId = get_newpayid()

        # label
        self.win_label = tk.Label(self, text="Please enter new payments", borderwidth=1)
        self.drive_id_label = tk.Label(self, text="Driver_id:", borderwidth=1)
        self.newPayId_label = tk.Label(self, text="Payment_id:", borderwidth=1)
        self.newPayId_value_label = tk.Label(self, text=self.payId, borderwidth=1)
        self.paidFrom_label = tk.Label(self, text="Paid_from:", borderwidth=1)
        self.paidTo_label = tk.Label(self, text="Paid_from:", borderwidth=1)
        self.paymentDate_label = tk.Label(self, text="Payment_date:", borderwidth=1)
        self.amountPaid_label = tk.Label(self, text="Amount_paid:", borderwidth=1)
        self.receivingBank_label = tk.Label(self, text="Receiving_bank:", borderwidth=1)
        self.discount_label = tk.Label(self, text="車租減免:", borderwidth=1)
        self.repair_label = tk.Label(self, text="維修:", borderwidth=1)
        self.notes_label = tk.Label(self, text="Notes:", borderwidth=1)
        self.col2Space_label = tk.Label(self, text="    ").grid(row=0, column=2)
        self.col5Space_label = tk.Label(self, text="    ").grid(row=0, column=5)
        self.answer = tk.Label(self, text="")

        # Entry
        self.driverId_input = tk.Entry(self, width=12, borderwidth=1)
        self.paidFrom_input = tk.Entry(self, width=12, borderwidth=1)
        self.paidFrom_input.insert(0, datetime.today().strftime('%Y-%m-%d'))
        self.paidTo_input = tk.Entry(self, width=12, borderwidth=1)
        self.paidTo_input.insert(0, "yyyy-mm-dd")
        self.paymentDate_input = tk.Entry(self, width=12, borderwidth=1)
        self.paymentDate_input.insert(0, datetime.today().strftime('%Y-%m-%d'))
        self.amountPaid_input = tk.Entry(self, width=12, borderwidth=1)
        self.receivingBank_input = tk.Entry(self, width=12, borderwidth=1)
        self.discount_input = tk.Entry(self, width=12, borderwidth=1)
        self.repair_input = tk.Entry(self, width=12, borderwidth=1)
        self.notes_input = tk.Entry(self, width=12, borderwidth=1)

        # Radio Button
        self.depositOnly_button = tk.Radiobutton(self, text="淨按金", variable=self.isDeposit, value=1, command=self.deposit_click)
        self.payment_button = tk.Radiobutton(self, text="普通俾租", variable=self.isDeposit, value=2, command=self.payment_click)

        # Button
        self.ok_button = tk.Button(self, text="Ok")
        self.ok_button['command'] = self.ok_click
        self.exit_button = tk.Button(self, text="Exit", command=self.quit)

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

        self.depositOnly_button.grid(row=5, column=0)
        self.payment_button.grid(row=5, column=3)

        self.discount_label.grid(row=6, column=0)
        self.discount_input.grid(row=6, column=1)
        self.repair_label.grid(row=6, column=3)
        self.repair_input.grid(row=6, column=4)

        self.notes_label.grid(row=8, column=0)
        self.notes_input.grid(row=8, column=1)

        self.ok_button.grid(row=10, column=3, sticky=tk.E)
        self.exit_button.grid(row=10, column=4, sticky=tk.E)

    def deposit_click(self):
        self.paidFrom_input.delete(0, 'end')
        self.paidFrom_input.configure(state="disabled")
        self.paidFrom_input.update()
        self.paidTo_input.delete(0, 'end')
        self.paidTo_input.configure(state="disabled")
        self.paidTo_input.update()
        self.discount_input.delete(0, 'end')
        self.discount_input.configure(state="disabled")
        self.discount_input.update()
        self.repair_input.delete(0, 'end')
        self.repair_input.configure(state="disabled")
        self.repair_input.update()

    def payment_click(self):
        self.paidFrom_input.configure(state="normal")
        self.paidFrom_input.update()
        self.paidTo_input.configure(state="normal")
        self.paidTo_input.update()
        self.discount_input.configure(state="normal")
        self.discount_input.update()
        self.repair_input.configure(state="normal")
        self.repair_input.update()

    def ok_click(self):

        # initial checks on paid date
        arg1 = self.driverId_input.get()
        last_paid = get_lastpaid(arg1)
        response = messagebox.askokcancel("Are you sure ?", f"The driver last paid on {last_paid}. \nIt is ok to insert?")
        if response:
            try:
                # mandatory Variables
                arg2 = self.payId
                arg3 = datetime.strptime(self.paymentDate_input.get(), '%Y-%m-%d')
                arg6 = float(self.amountPaid_input.get())
                arg7 = self.receivingBank_input.get()
                arg10 = self.notes_input.get()

                if self.isDeposit.get() == 1:
                    # deposit_only
                    new_deposit = DepositOnly(arg1, arg2, arg3, arg6, arg7, arg10)
                    print(new_deposit)
                    new_deposit.insert_deposit()
                elif self.isDeposit.get() == 2:
                    # normal_payment"
                    arg4 = datetime.strptime(self.paidFrom_input.get(), '%Y-%m-%d')
                    arg5 = datetime.strptime(self.paidTo_input.get(), '%Y-%m-%d')
                    # Optional Variables
                    if self.discount_input.get() != '':
                        arg8 = float(self.discount_input.get())
                    else:
                        arg8 = 0
                    if self.repair_input.get() != '':
                        arg9 = float(self.repair_input.get())
                    else:
                        arg9 = 0
                    new_payment = Payment(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10)
                    print(new_payment)
                    new_payment.insert_payment()
                else:
                    raise ValueError

                # window response
                self.answer.config(text="new payment added!")

            except ValueError as e:
                self.answer.config(text="invalid input")
        else:
            self.answer.config(text="operation canceled!")
        self.answer.grid(row=10, column=0)
