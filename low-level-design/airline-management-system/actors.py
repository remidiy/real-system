from abc import ABC, abstractmethod

class Account:
  def __init__(self, status, account_id, username, password):
    self.__status = status # Refers to the AccountStatus enum
    self.__account_id = account_id
    self.__username = username
    self.__password = password

  def reset_password(self):
    pass 

class Passenger:
  def __init__(self, passenger_id, name, date_of_birth, gender, passport_number):
    self.__passenger_id = passenger_id
    self.__name = name
    self.__date_of_birth = date_of_birth
    self.__gender = gender
    self.__passport_number = passport_number

class Person(ABC):
  def __init__(self, name, address, email, phone, account):
    self.__name = name
    self.__address = address
    self.__email = email
    self.__phone = phone
    self.__account = account


class Admin(Person):
  def __init__(self, name, address, email, phone, account):
    super().__init__(name, address, email, phone, account)

  def add_aircraft(self, aircraft):
    pass
  
  def add_flight(self, flight):
    pass
  
  def cancel_flight(self, flight):
    pass

  def assign_crew(self, flight):
    pass

  def block_user(self, user):
    pass

  def unblock_user(self, user):
    pass

class Crew(Person):
  def __init__(self, name, address, email, phone, account):
    super().__init__(name, address, email, phone, account)
  
  def view_schedule(self):
    pass

class FrontDeskOfficer(Person):
  def __init__(self, name, address, email, phone, account):
    super().__init__(name, address, email, phone, account)
  
  def view_itinerary():
    pass

  def create_itinerary():
    pass

  def create_reservation():
    pass

  def assign_seat():
    pass
  
  def make_payment():
    pass

class Customer(Person):
  def __init__(self, name, address, email, phone, account, customer_id):
    self.__customer_id = customer_id
  
    super().__init__(name, address, email, phone, account)
  
  def view_itinerary():
    pass

  def create_itinerary():
    pass

  def create_reservation():
    pass

  def assign_seat():
    pass
  
  def make_payment():
    pass