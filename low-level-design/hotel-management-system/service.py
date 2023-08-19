from abc import ABC, abstractmethod
import datetime

class Service(ABC):
  def __init__(self):
    self.__issue_at = datetime.date.today()

  def add_invoice_item(self, invoice):
    None

class Amenity(Service):
  def __init__(self, name, description):
    self.__name = name
    self.__description = description

class RoomService(Service):
  def __init__(self, is_chargeable, request_time):
    self.__is_chargeable = is_chargeable
    self.__request_time = request_time

class KitchenService(Service):
  def __init__(self, description):
    self.__description = description