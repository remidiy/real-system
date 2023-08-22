class Airport:
  def __init__(self, name, code, address):
    self.__name = name
    self.__code = code
    self.__address = address
    self.__flights = [] # List of flights

class Aircraft:
  def __init__(self, name, code, model, seatCapacity, seats):
    self.__name = name
    self.__code = code
    self.__models = model
    self.__seatCapacity = seatCapacity
    self.__seats = [] # List of seats

# The Airline is a singleton class that ensures it will have only one active instance at a time
class __Airline(object):
  __instances = None
  
  def __new__(cls):
    if cls.__instances is None:
        cls.__instances = super(__Airline, cls).__new__(cls)
    return cls.__instances

class Airline(metaclass = __Airline):
  def __init__(self, name, code):
    self.__name = name
    self.__code = code
    self.__flights = [] # List of flights
    self.__aircrafts = [] # List of aircrafts
    self.__crew = [] # List of crew
