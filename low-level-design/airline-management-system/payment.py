# Payment is an abstract class
from abc import ABC, abstractmethod

class Payment(ABC):
  def __init__(self, payment_id, amount, status, timestamp):
    self.__payment_id = payment_id
    self.__amount = amount
    self.__status = status # Refers to the PaymentStatus enum
    self.__timestamp = timestamp

  @abstractmethod
  def make_payment(self):
    pass

class Cash(Payment):
  def __init__(self, payment_id, amount, status, timestamp):
    super().__init__(payment_id, amount, status, timestamp)

  def make_payment(self):
    # functionality
    pass

class CreditCard(Payment):
  def __init__(self, payment_id, amount, status, timestamp, name_on_card, card_number):
    self.__name_on_card = name_on_card
    self.__card_number = card_number
    super().__init__(payment_id, amount, status, timestamp)

  def make_payment(self):
    # functionality
    pass