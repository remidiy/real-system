class __LockerService(object):
  __instances = None
  
  def __new__(cls):
    if cls.__instances is None:
        cls.__instances = super(__LockerService, cls).__new__(cls)
    return cls.__instances

class LockerService(metaclass=__LockerService):
    def __init__(self):
      self.__locations = {}

class Notification:
    def __init__(self, customer_id, order_id, locker_id, code):
        self.__customer_id = customer_id
        self.__order_id = order_id
        self.__locker_id = locker_id
        self.__code = code
    
    def send():
      pass