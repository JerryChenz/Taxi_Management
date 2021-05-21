from add_payment import *

if __name__ == '__main__':
    newPayment = AddPayment()
    newPayment.mainloop()
    print(newPayment.driverId_input.get(),newPayment.paidFrom_input.get(),newPayment.paidTo_input.get()
          ,newPayment.get_newPayId(),newPayment.paymentDate_input.get(),
          newPayment.amountPaid_input.get(), newPayment.receivingBank_input.get())