import enum

class Address:
  def __init__(self, zip_code, street_address, city, state, country):
    self.__zip_code = zip_code
    self.__street_address = street_address
    self.__city = city
    self.__state = state
    self.__country = country

class AccountStatus(enum.Enum):
  ACTIVE = 1 
  DISABLES = 2
  CLOSED = 3
  BLOCKED = 4

class SeatStatus(enum.Enum):
  AVAILABLE = 1 
  BOOKED = 2
  CHANCE = 3

class SeatType(enum.Enum):
  REGULAR = 1 
  ACCESSIBLE = 2
  EMERGENCY_EXIT = 3
  EXTRA_LEG_ROOM = 4

class SeatClass(enum.Enum):
  ECONOMY = 1 
  ECONOMY_PLUS = 2
  BUSINESS = 3
  FIRST_CLASS = 4

class FlightStatus(enum.Enum):
  ACTIVE = 1 
  SCHEDULED = 2
  DELAYED = 3
  LANDED = 4
  DEPARTED = 5
  CANCELED = 6
  DIVERTED = 7
  UNKNOWN = 8

class ReservationStatus(enum.Enum):
  REQUESTED = 1 
  PENDING = 2
  CONFIRMED = 3
  CHECKED_IN = 4
  CANCELED = 5

class PaymentStatus(enum.Enum):
  PENDING = 1 
  COMPLETED = 2
  FAILED = 3
  DECLINED = 4
  CANCELED = 5
  REFUNDED = 6