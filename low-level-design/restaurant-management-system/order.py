import datetime
from enums import ReservationStatus

class Order:
  def __init__(self, order_id, status, creation_time, meals, table, waiter, chef):
    self.__order_id = order_id
    self.__status = status
    self.__creation_time = creation_time
    self.__meals = []
    self.__table = table
    self.__waiter = waiter
    self.__chef = chef

  def add_meal(self, meal):
    None

  def remove_meal(self, meal):
    None

class Kitchen:
  def __init__(self, name):
    self.__name = name
    self.__chefs = []

  def assign_chef(self, chef):
    None

class Reservation:
  def __init__(self, id, people_count, notes, customer, checkin_time):
    self.__reservation_id = id
    self.__time_of_reservation = datetime.datetime.now()
    self.__people_count = people_count
    self.__status = ReservationStatus.REQUESTED
    self.__notes = notes
    self.__checkin_time = checkin_time
    self.__customer = customer
    self.__tables = []
    self.__notifications = []

  def update_people_count(self, count):
    None