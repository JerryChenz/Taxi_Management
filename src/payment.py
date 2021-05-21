class Payment:
  def __init__(self, d_Id, pay_Id, pay_Date, pFrom, pTo, paid, bank):
    self.driverId = d_Id
    self.paymentId = pay_Id
    self.paymentDate = pay_Date
    self.paidFrom = pFrom
    self.paidTo = pTo
    self.amountPaid = paid
    self.recevingBank = bank

class Deposit(Payment):
  def __init__(self, d_Id, pay_Id, pay_Date, paid, bank):
    self.driverId = d_Id
    self.paymentId = pay_Id
    self.paymentDate = pay_Date
    self.amountPaid = paid
    self.recevingBank = bank
