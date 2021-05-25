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


class DepositOnly(Payment):
    def __init__(self, d_Id, pay_Id, pay_Date, paid, bank):
        self.driverId = d_Id
        self.paymentId = pay_Id
        self.paymentDate = pay_Date
        self.amountPaid = paid
        self.recevingBank = bank

    def __str__(self):
        return f'Deposit({self.driverId},{self.paymentId},{self.paymentDate},{self.amountPaid},{self.recevingBank})'

