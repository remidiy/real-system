class Address:
  def __init__(self, street_address, city, state, zip_code, country):
    self.__street_address = street_address
    self.__city = city
    self.__state = state
    self.__zip_code = zip_code
    self.__country = country

class Person:
  def __init__(self, name, address, email, phone_number):
    self.__name = name
    self.__address = address
    self.__email = email
    self.__phone_number = phone_number

class Driver(Person):
  def __init__(self, name, address, email, phone_number, driver_id):
    super().__init__(name, address, email, phone_number)
    self.__driver_id = driver_id

from abc import ABC, abstractmethod

class Account(ABC):
  def __init__(self, name, address, email, phone_number, account_id, password, person):
    super().__init__(name, address, email, phone_number)
    self.__id = account_id
    self.__password = password
    self.__status = None

  @abstractmethod
  def reset_password(self):
    None

class Receptionist(Account):
  def __init__(self, name, address, email, phone_number, account_id, password, person, date_joined, status):
    super().__init__(name, address, email, phone_number, account_id, password, person, status)
    self.__date_joined = date_joined


  def search_customer(self, name):
    None

  def add_reservation(self):
    None

  def cancel_reservation(self):
    None

  def reset_password(self):
    pass
  

class Customer(Account):
  def __init__(self, name, address, email, phone_number, account_id, password, person, license_number, lisense_expiry, status):
    super().__init__(name, address, email, phone_number, account_id, password, person, status)
    self.__license_number = license_number
    self.__lisense_expiry = lisense_expiry

  def add_reservation(self):
    None
    
  def cancel_reservation(self):
    None
    
  def get_reservations(self):
    None

  def reset_password(self):
    pass