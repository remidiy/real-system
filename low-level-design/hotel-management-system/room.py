import datetime 

class Room:
    def __init__(self, room_number, style, status, booking_price, is_smoking):
        self.__room_number = room_number
        self.__style = style
        self.__status = status
        self.__booking_price = booking_price
        self.__is_smoking = is_smoking
        self.__keys = []
        self.__room_housekeeping_log = []

    def is_room_available():
         pass

    def checkin():
         pass

    def checkout():
         pass

class RoomKey:
  def __init__(self, key_id, barcode, is_active, is_master):
    self.__key_id = key_id
    self.__barcode = barcode
    self.__issued_at = datetime.date.today()
    self.__is_active = is_active
    self.__is_master = is_master

  def assign_room(self, room):
     pass


class RoomHousekeeping:
  def __init__(self, description, duration, housekeeper):
    self.__description = description
    self.__start_datetime = datetime.date.today()
    self.__duration = duration
    self.__housekeeper = housekeeper

  def add_housekeeping(self, room):
     pass

class RoomBooking:
  def __init__(self, reservation_number, start_date, duration_in_days, booking_status):
    self.__reservation_number = reservation_number
    self.__start_date = start_date
    self.__duration_in_days = duration_in_days
    self.__booking_status = booking_status
    self.__checkin = None
    self.__checkout = None
    self.__guest_id = 0
    self.__room = None
    self.__invoice = None
    self.__notifications = []

  def fetch_details(self, reservation_number):
     pass