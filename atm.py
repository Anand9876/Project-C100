class ATM(object):
  """
    blueprint for Automated Teller Machine
  """

  def __init__(self, cardnumber, pinnumber, cashrequired):
    self.cardnumber= cardnumber
    self.pinnumber = pinnumber
    self.cashrequired= cashrequired

  def insertCard(self):
    print("Please insert your card!")
    card=input('Have you inserted?')
    print(card)

  def readingtheCarddetailes(self):
    print("reading the card detailes and the card number")

  def enteryourpinnumber(self):
    print("Please enter your pin number")
    pinnumber=input('Please enter your pinnumber')
    print(pinnumber)
  def examiningthepinnumber(self):
      print("checking the pinnumber")
  def moneyrequired(self):
      print('Please enter the amount of money that you require')
      amount = input('please enter the amount here!')
      print(amount)
  def message(self):
      print('you got your  $amount ')
      amount=input('Yes or No')
      print(amount)
  def finalmessage(self):
      print('Have you got your money?')
      review=input('enter your answer')
      print(review)
  def visitagain(self):
      print('Visit again!Thank you.')



atm = ATM("1122334455667788", "1234", "10,000/-")

print(atm.insertCard())
print(atm.readingtheCarddetailes())
print(atm.enteryourpinnumber())
print(atm.examiningthepinnumber())
print(atm.moneyrequired())
print(atm.message())
print(atm.finalmessage())
print(atm.visitagain())
