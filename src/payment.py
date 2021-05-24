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

class deposit_only(Payment):
  def __init__(self, d_Id, pay_Id, pay_Date, paid, bank):
    self.driverId = d_Id
    self.paymentId = pay_Id
    self.paymentDate = pay_Date
    self.amountPaid = paid
    self.recevingBank = bank
