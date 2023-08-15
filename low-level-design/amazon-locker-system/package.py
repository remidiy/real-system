class Item:
  def __init__(self, item_id, quantity):
    self.__item_id = item_id
    self.__quantity = quantity

class Order:
  def __init__(self, order_id, items, delivery_location):
    self.__order_id = order_id
    self.__items = items # List of items
    self.__delivery_location = delivery_location 

class Package:
    def __init__(self, package_id, package_size, order):
        self.__package_id = package_id
        self.__package_size = package_size
        self.__order = order
  
    def pack():
        None

class LockerPackage(Package):
    def __init__(self, code_valid_days, locker_id, package_id, code, package_delivery_time, package_size, order):
        self.__code_valid_days = code_valid_days
        self.__locker_id = locker_id
        self.__package_id = package_id
        self.__code = code
        self.__package_delivery_time = package_delivery_time
        super().__init__(package_id, package_size, order)
  
    def is_valid_code():
        None
    
    def verify_code(code):
        None